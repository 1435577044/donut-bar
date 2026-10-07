# Donut-bar

把 iOS 桌面图标的通知角标（badge）换成**图标下方的彩色横条 / 空心小圆 / 实心小圆点**，颜色自动跟随 App 图标主色提取。

- **包标识**：`com.dao.donutbar`
- **当前版本**：1.2.0
- **目标环境**：iPhone 15 Pro Max（A17 Pro / arm64e）、iOS 17.2.1、Relaxin（RootHide 隐根）
- **安装方式**：Sileo / Filza 安装 `releases/1.2.0/donut-bar120.deb`，安装后需 Respring
- **设置面板**：设置 → Donut-bar

## 功能

| 项 | 说明 |
|---|---|
| Badge Style | 三选一：Bar（横条）/ Ring（空心圆）/ Dot（实心圆点） |
| Bar X / Y Offset | 横条相对图标中心的偏移，X=40 水平居中、Y=80 为标定位置 |
| Bar Width / Height | 横条尺寸，默认 30 × 6 pt，圆角 = H/2 |
| Badge Color Mode | Auto（自动取图标主色）/ Custom（手动选色，取色器内可调色） |
| 改设置需 Respring | tweak 仅在加载期读取偏好，改完必须 Respring 生效 |
| 恢复默认 | Actions → Restore Defaults 一键复位四个滑块 |

横条挂靠「角标圆点矩形」（d8-d11 寄存器）而非 `self.bounds`——后者在新机型上量到的是整个屏幕宽，导致横条位置飘到屏幕右侧。详见 `docs/DonutBar_3.3.0_横条位置重构报告.html`。

## 版本历史

| 版本 | 变更 |
|---|---|
| 1.2.0 | 更换图标为天气扁平图标（1024×1024，三档 LANCZOS 缩小、无损 RGBA + zopfli）；构建链删除死代码（`_opt_png` / `ICON_N`） |
| 1.1.0 | 包内精简：Root.strings 两语言各删 4 条从未被引用的死串（27 → 23 条） |
| 1.0.0 | 首个正式版：横条 Y 默认 80；样式三选一；颜色项合并与条件显示；滑块按样式折叠 |
| 3.x | 内部迭代：横条挂靠点从 self.bounds 改为角标矩形，解决跨机型位置漂移 |

完整清单见 `releases/1.2.0/MANIFEST.md`。

## 目录结构

```
releases/1.2.0/            成品 deb、三档插件图标、归档说明
  donut-bar120.deb         可直接安装的隐根包（36,748 B）
  icons/                   icon.png 29 / icon@2x.png 58 / icon@3x.png 87（RGBA）
  MANIFEST.md              变更明细、验证结果、脚本链
scripts/                   可复现构建链（Python 3.13 + Pillow + zopfli）
  patch_donut47.py         主构建脚本（逆向改写 + 双 CodeDirectory 重签 + 打包）
  make_v120c.py            由上一版脚本派生（清理死代码）的生成器
  verify_v120b.py          18 项断言的包验证脚本
  patch_log47.txt          最近一次构建的完整日志
docs/                      技术报告与排查指引
```

## 构建链

```bash
python make_v120c.py        # 从上一版脚本派生 patch_donut47.py（含 ast 语法自检）
python patch_donut47.py     # 构建 donut-bar120.deb（确定性：同参数重跑 sha256 一致）
python verify_v120b.py      # FAIL 0 / 18 才算通过
```

构建依赖：`Pillow`、`zopfli`。脚本内的二进制改写与重签逻辑基于 `ios-deb-roothide-port` 技能中的
`roothide_convert.py` / `dualcd_sign.py` / `audit.py`。

### 包内签名

隐根包使用**现代双 CodeDirectory**（`SHA-1 CD 0x20400` + `Requirements` + `SHA-256 CD 0x20400`）。
上游老包多为单 SHA-1 / version `0x20001`，在 iOS 16+ 上会被 AMFI 判为
`code signature invalid (errno=1)`，表现为**插件静默不加载**。详见
`docs/BadgeBarX_签名问题根因与修复报告.html`。

## 免责声明

本项目为个人学习与自用性质的 iOS 越狱插件改作，**不授予任何许可**，仅供使用者在自己设备上安装研究。
代码与二进制中包含对第三方作品（Donut、BadgeBar X）的逆向分析与改写，
相关权利归各自作者所有；分发或再发布前请自行确认已获得原作者授权，并自行承担风险。
插件以 Root 环境加载，无任何网络请求，不收集任何数据。

## 致谢

- **Donut / BadgeBar / Donut-bar** 的显示效果与全部贡献者（刀刀源）
- 桌面插件维护者 文武

## 环境风险提示

- iOS 14.5 起 Apple 不再支持 legacy ABI；本包 arm64e 切片为**新 ABI**，正常加载。
- 注入目标是 SpringBoard：若二进制被改坏会直接导致进不了系统，出问题时用 Filza 删除
  `.jbroot/` 下对应 dylib 与 plist 可恢复到安全模式。排查流程见
  `docs/BadgeBarX_崩溃循环根因与救援指引.html`（见 `_fix` 目录历史文档）。