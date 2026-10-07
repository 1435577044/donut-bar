# Donut-bar v1.2.0 归档说明

**日期**：2026-09-26（light30 图标变体 + 同日代码核查轮 + 21:56 重建导出图标）
**deb**：`donut-bar120.deb` — 36,748 B
**sha256**：`43a749e25109a0785eda1c90f68b51e9756d76cf2732121a14b92f12302df57c`

## icons/ —— 插件三档图标（从本 deb 内直接导出）

| 文件 | 用途 | 尺寸 | 大小 |
|---|---|---|---|
| `icons/icon.png` | 1x | 29×29 RGBA | 1,434 B |
| `icons/icon@2x.png` | 2x | 58×58 RGBA | 3,379 B |
| `icons/icon@3x.png` | 3x（设置面板实际显示档） | 87×87 RGBA | 5,254 B |

均由 light30 源图 LANCZOS 缩小 + 无损 RGBA + zopfli 生成，与包内逐字节一致。

## 代码核查轮（2026-09-26 21:45，用户指令「检查代码、删除无用代码」）

### 包内容层（10 个文件）——未删任何内容，全部有据
- Root.strings 两语言各 23 条：20 条被 Root.plist 引用；3 条候选逐一排除：
  - `Custom Color`：**DonutPrefs 二进制中出现 x2**，有运行时引用 → 保留
  - `Donut`：两个二进制各 x2，可能被运行时查找 → 保留
  - 副标题串：用户此前明确保留
- Root.plist 18 项结构完整；折叠 stub 依赖区 index 4..11 配对正确（static+slider ×4，id 81..88）
- slider 默认值 X=40[0,80] / Y=80[40,120] / W=30[2,58] / H=6[2,10] 与 dylib DEFAULTS 一致

### 构建脚本层——删除唯一死代码
- 删 `_opt_png()`：64 色量化旧路径，1.0.3 起被 `_lossless_png` 取代，ast 扫描确认无调用方
- 删 `ICON_N = 64`：仅被 `_opt_png` 默认参数引用
- 复扫：patch_donut47.py 函数 18 / 变量 92 / import 18，**未引用 0**
- **产物逐字节不变**：清理前后 sha256 均为 43a749e2...，重建幂等一致

## 1.2.0 主体变更（相对 1.1.0）

1. **图标更换**：`weather-flat-icon-ring-light30-1024.png`（1024×1024 RGBA，
   sha256 `8ba81070...`，右上角圆环 30% 亮度变体；首版 ring-clip 已换下）。
   三档 29/58/87 全为 LANCZOS 缩小，无损 RGBA + zopfli；图标合计 13,453 → 10,067 B。
2. **版本号 1.1.0 → 1.2.0**：同 5 字符，版本槽就地写入，无 ptr 重定向。
3. 其余内容（dylib 插桩 / plists / 双语言 strings / control）与 1.1.0 逐字节一致。

## 验证汇总

- `verify_v120b.py`：FAIL 0 / 18（图标像素与源图独立 LANCZOS 缩放逐像素一致）
- `audit.py`：FAIL 0 / WARN 1（Depends 无 rootless-compat，历史固有项）
- 幂等：多次重建 sha256 一致（含 21:56 重建）
- 脚本链：`make_v120c.py` → `patch_donut47.py` → `verify_v120b.py`

## icon-src/

- `weather-flat-icon-ring-light30-1024.png` —— **实际使用**的源图
- `weather-flat-icon-ring-clip-1024.png` —— 首版源图（留档）
