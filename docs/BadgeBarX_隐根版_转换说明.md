# BadgeBar X 1.3.7 → 隐根（RootHide / roothide）版转换说明

**推荐安装的产出文件**：`xyz.cypwn.badgebarx_1.3.7-roothide2_iphoneos-arm64e.deb`（168,652 字节）
**早前一版**：`xyz.cypwn.badgebarx_1.3.7-roothide_iphoneos-arm64e.deb`（168,534 字节，未声明 `rootless-compat`）
**源文件**：`BadgeBar X-1.3.7.deb`（有根格式，XinaA15 适配版）
**转换 / 审计日期**：2026-09-21

> 两个包的 **二进制载荷完全相同**（`data.tar.gz` 字节级一致），差别只在 `control` 的
> `Depends` 和 `Version`。v2 补上了 `rootless-compat`，原因见第五节。

---

## 一、先澄清概念：隐根 ≠ 无根

| 格式 | 说明 | 基础路径 | deb 架构字段 |
|---|---|---|---|
| 有根 Rootful | 传统越狱，直接改系统分区 | `/` | `iphoneos-arm` |
| 无根 Rootless | Dopamine / palera1n 等，固定前缀 | `/var/jb` | `iphoneos-arm64` |
| **隐根 Roothide** | 在 rootless 基础上再隐藏，jbroot 路径**每次越狱随机** | **直接布局（同有根）** | **`iphoneos-arm64e`** |

隐根（RootHide）的核心特点（据 RootHide 官方开发者文档）：

- jbroot 挂在随机路径下（形如 `/var/containers/Bundle/Application/.jbroot-XXXXXXXXXXXXXXXX/`），**不可硬编码**；
- 包内**目录布局与有根包完全一致**，由 dpkg 自动把文件装进随机 jbroot；
- 动态库一律用 `@loader_path/.jbroot/<原绝对路径>` 链接；
- 每个含 Mach-O 的目录里有一个 `.jbroot` 符号链接指向 jbroot，由 dpkg 自动生成。

> ⚠️ 架构字段叫 `iphoneos-arm64e`，但**和设备 CPU 无关**，只是 roothide 的格式标记；
> 真正的 arm64e 切片才需要 arm64e 硬件。本例二进制本来就带 arm64 + arm64e 双切片，天然兼容。

> 所以本次转换**没有动包内目录结构**，改的是架构字段、动态库链接路径和硬编码字符串。

---

## 二、逐项改动清单

| # | 对象 | 改动前 | 改动后 |
|---|---|---|---|
| 1 | control `Architecture` | `iphoneos-arm` | **`iphoneos-arm64e`** |
| 2 | control `Depends` | `…, org.thebigboss.libcolorpicker, xinaa15` | 移除 `xinaa15`；v2 追加 `rootless-compat` |
| 3 | control `Version` | `1.3.7` | `1.3.7-roothide` / `1.3.7-roothide2` |
| 4 | control `Description` | 单行 | 补充隐根移植说明 |
| 5 | 新增 `postinst` | — | 兜底创建 `.jbroot` 符号链接（失败不影响安装，`exit 0`） |
| 6 | `BadgeBar.dylib` 链接 | `/var/lib/libcolorpicker.dylib` | `@loader_path/.jbroot/usr/lib/libcolorpicker.dylib` |
| 7 | `BadgeBar.dylib` 链接 | `/var/LIY/Frameworks/Cephei.framework/Cephei` | `@loader_path/.jbroot/Library/Frameworks/Cephei.framework/Cephei` |
| 8 | `BadgeBar.dylib` 链接 | `/var/LIY/Frameworks/CydiaSubstrate.framework/CydiaSubstrate` | `@loader_path/.jbroot/usr/lib/libsubstrate.dylib` |
| 9 | `BadgeBarPrefs` 链接 | `/var/lib/libcolorpicker.dylib`<br>`/var/LIY/…/Cephei.framework/Cephei`<br>`/var/LIY/…/CepheiPrefs.framework/CepheiPrefs` | 同上，均改为 `@loader_path/.jbroot/…` |
| 10 | 硬编码字符串 | `/var/LIY/MobileSubstrate/DynamicLibraries/ColorBadges.dylib` | `/var/jb/Library/MobileSubstrate/DynamicLibraries/ColorBadges.dylib` |
| 11 | 硬编码字符串 | `/var/LIY/MobileSubstrate/DynamicLibraries/Snowboard.dylib`<br>`…/SnowBoard.dylib` | `/var/jb/Library/MobileSubstrate/DynamicLibraries/…` |
| 12 | 硬编码字符串 | `/var/LIY/PreferenceBundles/BadgeBarPrefs.bundle/banner.png`<br>`…/icon@2x.png` | `/var/jb/Library/PreferenceBundles/BadgeBarPrefs.bundle/…` |
| 13 | 硬编码字符串 | `/var/bin/killall`（注销用） | `/var/jb/usr/bin/killall` |
| 14 | **未改动** | `/var/mobile/Library/Preferences/com.jannikcrack.badgebarprefs.plist` | 保持原样 —— 隐根对该路径做重定向，本就正确 |

---

## 三、二进制层面做了什么

源包是 arm64 + arm64e 双架构 fat Mach-O，两个切片都做了处理。

1. **重写 `LC_LOAD_DYLIB`**
   新路径比旧路径长（如 `CydiaSubstrate` 58 字节 → `libsubstrate.dylib` 47 字节，`Cephei` 42 → 62 字节），
   利用加载命令区之后 21–25 KB 的全零空隙扩展命令区（`sizeofcmds` 同步更新），无需移动任何数据。

2. **字符串重定位**
   新字符串比旧的长，原位替换会踩掉后面的字符串，因此把新串写进上述空隙，再回填引用：
   - `__DATA,__cfstring` 里的 cstr 指针（每 32 字节一条，改 +16 偏移的指针字段）；
   - `__text` 里的 `ADR` 指令（PC 相对，重编码 imm21）。

   ⚠️ 一个坑：**arm64e 切片的数据指针带高位标签**，如 `0x001000000000bbb2`（低位才是真实地址）。
   按精确值匹配会全部漏掉，必须按低位掩码（`0xFFFFFFFFF`）匹配、保留高位置。
   本次共修复 **26 处引用**（两个二进制 × 两个切片）。

3. **重新签名**
   源包被 Sudo 改路径时没有重新签名，ldid 的页面哈希本来就是失效的
   （arm64 切片 18 页里 5 页不匹配）。本次按原 CodeDirectory 结构（SHA1 / pageSize 4K / 18 页）
   重算了 code slot 哈希，产出包**签名 100% 有效**。

4. **未改动**：功能代码、`BadgeBar.plist` 注入过滤器、`Root.plist`、图片资源、文件权限、包标识。

---

## 四、二次审计结果（指令级，全部通过）

对产出包做了独立于转换脚本的第二轮审计（`_convert\audit.py` + `_convert\audit2.py`）：

| 检查项 | 结果 |
|---|---|
| deb 结构（ar 成员名、control.tar.gz、data.tar.gz） | ✅ 与原包同格式 |
| 加载命令链完整性（`ncmds` / `cmdsize` 链 / `sizeofcmds`） | ✅ 两切片均一致 |
| 新字符串落点是否在已映射段内 | ✅ 均落在 `__TEXT` 段内 |
| 原空隙是否为全零（确认没覆盖有效数据） | ✅ 全零 |
| **补丁后 `ADR` 指令解码是否精确指向新串** | ✅ 4 处全部命中，内容正确 |
| 旧 `/var/LIY` 字符串是否仍被指针/指令引用 | ✅ 无残留引用（仅保留原串，无引用） |
| `__cfstring` 指针高位（arm64e 标签位）是否被破坏 | ✅ 保留 |
| 代码签名页面哈希 | ✅ dylib 18/18+18/18，prefs 13/13+13/13 |
| 非 Mach-O 文件中的 `/var/LIY` 残留 | ✅ 无 |
| 注入过滤器 `BadgeBar.plist` | ✅ `Bundles = (com.apple.springboard)` |
| 设置入口 `BadgeBarPrefs.plist` / `Info.plist` | ✅ bundle 与可执行名一致（`BadgeBarPrefs` / `BDBRootListController`） |

**唯一有意保留的旧路径**：`/var/mobile/Library/Preferences/com.jannikcrack.badgebarprefs.plist`（第 14 项）。

> 补充说明：`__gcc_except_tab` 段里有一处字节恰好形似 `ADRP` 指向旧字符串所在页，属于数据段误判，
> 不是真实取址指令（该段已按整段扫描确认无真实引用）。

---

## 五、依赖：需要什么、从哪来（已逐个下载源码包核实）

`Depends` 最终为：

```
mobilesubstrate, preferenceloader, ws.hbang.common (>= 1.14),
org.thebigboss.libcolorpicker, rootless-compat
```

隐根官方源 `https://roothide.github.io/` 上的对应关系（已下载 deb 解包验证文件实体）：

| 声明依赖 | 隐根源上的实际包 | 版本 | 是否提供本插件链接的文件 |
|---|---|---|---|
| `mobilesubstrate` | **`ellekit`** | 1.2-1 | ✅ `usr/lib/libsubstrate.dylib → libellekit.dylib`（符号链接）<br>ElleKit 声明 `Provides: mobilesubstrate (= 99)`，所以这条依赖照写即可 |
| `preferenceloader` | `preferenceloader` | 2.2.8 | ✅ 设置页入口就靠它 |
| `ws.hbang.common` | `ws.hbang.common`（Cephei） | 2.0-29 | ✅ `Library/Frameworks/Cephei.framework/Cephei`<br>✅ `Library/Frameworks/CepheiPrefs.framework/CepheiPrefs` |
| `org.thebigboss.libcolorpicker` | **`ws.hbang.alderis`**（Alderis Color Picker） | 1.2.3-8+debug | ✅ `usr/lib/libcolorpicker.dylib`<br>Alderis 声明 `Provides: org.thebigboss.libcolorpicker (= 99.0)` |
| **`rootless-compat`**（v2 新增） | `rootless-compat` | 2.0 | ✅ 见下方说明 |

### 为什么 v2 必须补 `rootless-compat`

roothide 的 Bootstrap 源码里**主动删除 `/var/jb`**（`Bootstrap/bootstrap.m`）：

```objc
if (lstat("/var/jb", &st) == 0) {
    // remove /var/jb to avoid incorrect library loading via @rpath
    ASSERT([fm removeItemAtPath:@"/var/jb" error:nil]);
}
```

而本插件仍有 4 处运行时路径指向 `/var/jb`（第 10–13 项：ColorBadges/SnowBoard 探测、
设置页 banner/icon、注销用的 `killall`）。

`rootless-compat`（"Compat Layer for Rootless Tweaks"，包内只有
`usr/lib/DynamicPatches/AutoPatches.dylib`）就是把这些 `/var/jb` 路径在运行时补回来的官方方案 ——
它本身依赖 `com.roothide.patchloader`。

**结论**：不装 `rootless-compat` 不会有致命问题（核心的角标替换不依赖这 4 条路径），
但以下功能会静默失效：设置页顶部的 banner/图标、Respring 按钮、与 ColorBadges / SnowBoard 的兼容探测。
v2 已把它写进 `Depends`，Sileo 会自动装上。

### 不需要的

- ~~`xinaa15`~~：XinaA15 专属包，隐根环境不存在，已移除。
- 不需要 `firmware` 显式声明（Cephei 2.0-29 自带 `firmware (>= 15.0)`）。

---

## 六、安装

1. 把 **v2** deb（`…-roothide2_iphoneos-arm64e.deb`）传到设备（AirDrop / Filza / 文件 App 均可）；
2. 用 Sileo / Zebra 打开并安装（也可 `dpkg -i`）；
3. **注销（Respring）** 后生效。

依赖会由 Sileo 自动安装：`ellekit`、`preferenceloader`、`ws.hbang.common`、`ws.hbang.alderis`、`rootless-compat`。

---

## 七、注意事项与已知限制

1. **Bootstrap 半越狱（Bootstrap + Serotonin）** 下，本插件注入 SpringBoard，
   必须先启用 **SpringBoard 注入** 才能看到效果。
2. 若安装后插件"没反应"，按顺序排查：
   - `ls -la <jbroot>/Library/MobileSubstrate/DynamicLibraries/` 看有没有 `.jbroot` 符号链接，
     没有就手动建：`ln -s ../../.. <jbroot>/Library/MobileSubstrate/DynamicLibraries/.jbroot`
     （`postinst` 已做兜底，正常不会遇到）；
   - 确认 `usr/lib/libsubstrate.dylib`、`Library/Frameworks/Cephei.framework/Cephei`、
     `usr/lib/libcolorpicker.dylib` 三者都存在；
   - 确认 `rootless-compat` 已安装（`/var/jb` 路径依赖它）。
3. **未做真机验证。** 本次为离线静态转换 + 离线静态审计：deb 结构、Mach-O 加载命令、
   指针与指令引用、代码签名哈希均已程序化校验通过，但最终加载行为需在隐根设备上实测。
4. 包标识沿用 `xyz.cypwn.badgebarx`，版本 `1.3.7-roothide2` 高于原 `1.3.7`，
   在 Sileo 里会显示为可升级项。
5. 不影响使用的历史遗留（源包自带，未改动）：
   - 两个二进制的 `LC_UUID` 是全零（技术上不唯一，但源包如此且可正常加载）；
   - 原 `/var/LIY/…` 字符串仍留在 `__cstring` 中（已无任何引用，属死数据）。
6. **与 `Pastel`、`Dotto+` 冲突**（源包 `Conflicts` 声明，同类外观插件，共用会打架）。

---

## 八、卸载 / 回滚

```sh
# 卸载
dpkg -r xyz.cypwn.badgebarx
# 回滚到原包（注意：原包是 XinaA15 有根格式，隐根环境装不了）
dpkg -i "BadgeBar X-1.3.7.deb"
```

---

## 九、自行复核

转换与审计脚本全部留档，可复现、可审计（`E:\deb\_convert\`）：

| 文件 | 作用 |
|---|---|
| `roothide_convert.py` | 隐根转换主脚本（含完整补丁逻辑与自检） |
| `convert_log.txt` | 转换逐项日志 |
| `audit.py` | 审计 ①：结构 / 加载命令 / 签名 / 字节差异 / 高位破坏统计 |
| `audit2.py` | 审计 ②：指令级（ADR / ADRP+ADD / 指针残留、新串落点、命令链完整性） |
| `verify.py` | 独立校验（重新解包 + 重算签名 + 列路径） |
| `sigcheck.py` | ldid 签名结构分析 |
| `depcheck.py` / `depfiles.py` | 依赖解析（拉取隐根源 Packages + 下载依赖 deb 验证文件实体） |
| `makedeb2.py` | 生成补了 `rootless-compat` 的 v2 包（data 字节级复用） |
| `compat.py` | 核实 `rootless-compat` 内容与 roothide 源码中的 `/var/jb` 处理 |

校验重点：

- `control` 的 `Architecture: iphoneos-arm64e`、`Depends` 含 `rootless-compat`；
- 两个二进制的 `LC_LOAD_DYLIB` 全部为 `@loader_path/.jbroot/...`（系统库除外）；
- 代码签名页面哈希全部匹配；
- 包内路径与权限与原包一致。
