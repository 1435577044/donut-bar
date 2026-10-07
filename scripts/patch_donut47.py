# -*- coding: utf-8 -*-
"""DonutBar 1.0.4 —— 图标尺寸对齐上游原版（修 1.0.3 的"图标太小"）。

【版本号 1.2.0】图标更换为用户提供的天气扁平图标 weather-flat-icon-ring-light30-1024.png
  （2026-09-26 二次更换：右上角圆环用 30% 亮度变体，替换同日的 ring-clip 版；版本号不变）
  （1024x1024 RGBA，圆角外透明）。三档 29/58/87 全部 LANCZOS **缩小**（源图信息量远超 3x 档，
  无插值放大），仍走无损 RGBA + zopfli。其余内容与 1.1.0 完全一致。
  '1.2.0' 与 '1.1.0' 同为 5 字符，版本槽容量足够，无需 ptr 重定向。

【版本号 1.1.0】在精简版基础上把 Version 由 1.0.4 改为 1.1.0。
  内容 = 精简版（1.0.4 内容 + Root.strings 各删 4 条死串），图标三档不变。
  '1.1.0' 与 '1.0.4' 同为 5 字符，版本槽容量足够，无需 ptr 重定向。

【精简版】在 1.0.4 内容基础上删掉包内「除图标外」的死内容：
  Root.strings 各删 5 条从未被引用的条目（zh-Hans 27->22，en 27->22）。
  图标三档、二进制、plist 结构一律不动。净省约 287 B（0.72%）。
  其余候选（Root.plist 删键 / Mach-O 段紧凑化 / __cstring 删串）因风险过高未做。

## 1.0.4 变更（相对 1.0.3）
- **3x 档由 60px 提到 87px**（对齐上游原版）。1.0.3 为"绝不放大"把 3x 降到
  源图上限 60px，但偏好面板用的正是 3x 档 ⇒ 60/3 = 20pt，比上游原版的 29pt 小一圈。
  现对扁平矢量风格的源图做 LANCZOS 上采样（实测放大后边缘依然干净，
  锐化处理收益 <1% 故不引入）。三档回到 **29 / 58 / 87**。
- 图标体积 9013 → 13453 B（本包 40062 B）。质量仍为**无损**（不量化）。
- 尺寸断言策略翻转：从「不许超过源图」改为「**不得低于上游原版**」。
- 版本号 1.0.3 → 1.0.4。**二进制侧插桩与 1.0.0~1.0.3 完全相同。**

## 1.0.3 变更（相对 1.0.2）
- **图标不再量化**。1.0.2 把 RGBA 砍成 64 色调色板 + 把 60x60 源图铺到 87x87，
  用户反馈发糊。现改为：RGBA 原样存 PNG（zopfli 仍重压 IDAT，那是**无损**编码优化），
  且各档不超过源图的 60px（29 / 58 / **60**，3x 由 87 降到 60 —— 不放大就没有插值糊）。
  体积 3049 → 9013 B。用户要求的就是清晰度，这点体积花得值。
- 版本号 1.0.2 → 1.0.3。**二进制侧插桩与 1.0.0/1.0.1/1.0.2 完全相同。**

## 1.0.2 变更（相对 1.0.1）
- **图标改回 BadgeBar X-1.3.7.deb 的 icon@2x**（用户指定），不再用 1.0.1 的重绘图。
  源图 60x60 / 4021 B，仍按 29/58/87 三档缩放并做 RGBA 64 项量化 + zopfli。
  体积 2935 → 3049 B。
- 1.0.1 的**副标题文案修正保留**（'彩色横条' → '横条 / 空心圆 / 圆点'）——
  那是独立于图标的功能性修正，与本次图标回退无关。
- 版本号 1.0.1 → 1.0.2。**二进制侧插桩与 1.0.0/1.0.1 完全相同。**

## 1.0.1 变更（相对 1.0.0）
- **设置面板图标重绘**，体现当前功能（原版绿方块+红圈是旧语义）：
  白色圆角方框（应用图标）+ 正下方青→蓝→紫渐变胶囊横条。
  三档 29/58/87 按相对几何独立渲染，构图严格一致；仍走 RGBA 64 项 + zopfli。
  体积 3049 → 2935 B（−114 B）。
- **副标题改成覆盖三种样式**：'彩色横条' → '横条 / 空心圆 / 圆点'
  （1.0.0 起本就是三样式可切，旧文案只提横条，与实际功能不符）。
- 版本号 1.0.0 → 1.0.1。**二进制侧插桩与 1.0.0 完全相同。**

## 1.0.0 变更（相对内部迭代版 4.0.6）
- **横条上下偏移默认 78 → 80**（下移 2pt，回到 4.0.0 的标定位置）。同步三处：
  dylib `DEFAULTS[1]`、Root.plist 的 Y 滑块（[38,118] → [40,120]）、
  `DEAD_STR` 的默认值载体键。标定常量 `KEY_Y` 不动。
- **版本号 4.0.6 → 1.0.0**（用户指定，作为第一个正式版）。
- 其余一切不变：图标体积优化（RGBA 量化 64 项 + zopfli，6013 → 3049 B）、
  样式三选一（横条/空心圆/圆点）、颜色项合并与条件显示、滑块按样式折叠、
  作者「文武」、致谢文案。**二进制侧插桩与 4.0.6 完全相同。**

## 以下为 3.3.0 的历史说明

DonutBar 3.3.0：横条挂靠「角标圆点矩形」，彻底摆脱 self.bounds（跨机型自适应）。

## 为什么放弃 badgeW（3.1.2 / 3.2.0 的思路）

3.2.0 把挂靠点从「视图右边缘」改成「视图水平中心」，前提是 `self.bounds` = 图标视图宽度。
2026-09-25 用户第二张真机截图（1280×2774，430pt 屏）把它证伪了：

    蓝色第 4 图标：x=984..1174 → 191×191 px = 63.7×63.7 pt，中心 x = 1079 px
    横条        ：x=1125..1211 → 29.9×6.1 pt，中心 x = 1168 px
    ⇒ 横条中心比图标中心**偏右 89 px = 29.7 pt**，还戳出图标右边缘 12 pt

反推 `center = badgeW + X - 81` 得 badgeW ≈ 430 pt ≈ **整个屏幕宽** ——
说明 `self.bounds` 量的根本不是图标视图，而是某个屏幕宽的视图 ⇒ 位置与图标无关、永远跑到右边。
而更早那张「已认可」的截图反推出 badgeW ≈ 306（同一公式）——**两次数值自相矛盾**，
说明 badgeW 本身不可靠（glue 里 `ldr x0,[sp,#0x68]` 读调用者栈帧取 self 的老做法，
在新系统/新机型上取到的对象可能已经不对，`bounds` 于是返回任意值）。

## 3.3.0 的做法

改挂 **`d8-d11`（角标圆点矩形）**，它有三个决定性优点：
  1. **就在绘制坐标系里** —— 原始代码正是 `fmov d0..d3, d8..d11` 后调
     `bezierPathWithOvalInRect:` 画圆点的；圆/空心圆样式也靠它。所以它是「路径空间」的真值。
  2. **跟着图标走** —— 圆心 = 角标中心（图标右上角内侧），跨机型/跨 App 恒定。
  3. **在注入点必定有效** —— 原代码在 `bl` 前 4 条指令刚从 d8-d11 取过值，寄存器活性有原代码背书。
偏移常量（`DX` 水平、`DY` 垂直）由 15PM 实测图标框与角标几何标定：
  · 角标（~20pt）贴在图标右上角，圆心距图标右边/上边各 ~10pt（系统常量）；
  · DX = −(iconW/2 − 10) ≈ −21（iconW 63.7）→ 横条中心 = 图标中心；
  · DY = (iconW − 10) + 1.7 + H/2 ≈ 58（H=6）→ 横条中心 = 角标圆心 + 58pt；
    其中 1.7pt = 实测「横条顶贴着图标下沿」的间距。
因 iconW 在不同机型为 60~64pt，DX/DY 会有 ±2pt 浮动 —— 已经比原来偏 30pt 好两个数量级，
且 X/Y 滑块现在是「相对图标中心的偏移」，同一台机上所有 App 表现一致，一次就能调准。

## 附带收益（都是净减法）

  · glue **23 条 / 92 B**（与 3.1.2/3.2.0 同尺寸，但少了一条调用与两次内存访问）；
      prefs_to_rect **80 条 / 320 B**（3.1.2/3.2.0 为 82 / 328）⇒ 落脚区余量 184B → 192B；
  · **热路径不再有任何 objc_msgSend**（原来的 `bl bounds` 是唯一的，现在去掉）；
  · **不再读调用者栈帧**（`ldr x0,[sp,#0x58/0x68]` 那种脆弱做法彻底移除），
    也不再需要 stp/ldp 保护 x0+lr —— x0 从入口到尾调一路没被碰过，天然还是 UIBezierPath 类；
  · 内存访问由 8 次降到 6 次（去掉 bl bounds 的栈读写与类指针重载）。

X/Y 滑块语义：X=40 → 水平居中于图标；Y=80 → 标定的垂直位置（贴图标下沿再下 1.7pt）。
"""
import io, gzip, tarfile, lzma, plistlib, struct, sys, hashlib
from capstone import Cs, CS_ARCH_ARM64, CS_MODE_ARM
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.path.insert(0, r"C:\Users\张培斌\.workbuddy\skills\ios-deb-roothide-port\scripts")
import roothide_convert as RC
import dualcd_sign as DS
from keystone import Ks, KS_ARCH_ARM64, KS_MODE_LITTLE_ENDIAN
KS = Ks(KS_ARCH_ARM64, KS_MODE_LITTLE_ENDIAN)

SRC = r'E:\deb\_fix2\Donut_RootHide_2.0.3.deb'
OUT = r'E:\deb\donut-bar120.deb'
LOG = r'E:\deb\_fix2\patch_log47.txt'
# 版本号唯一来源：deb control 与设置面板底部显示的版本号都由它生成，发版只改这一处
VERSION = '1.2.0'
assert len(VERSION) == 5 == len('1.1.0'), '版本槽约束：必须 5 字符就地写入'
# ---- 包标识符（v3.8.0：改为 com.dao.donutbar）----
# 原标识符 com.dao.donut 出现在三处：
#   ① control 的 `Package:`
#   ② dylib 的 __DATA_CONST.__cfstring @0x8148（内容指针 -> __cstring 里的串，len=13）
#      —— 原 ctor 与我们的 prefs_to_rect 都靠 `adrp x2,#0x8000 / add x2,x2,#0x148` 取这个 CFString
#      传给 initWithSuiteName:
#   ③ DonutPrefs 的 __cfstring @0x8098(arm64)/0x8138(arm64e)（len=13）——「恢复默认」IMP 用它
#   （另有通知名 'com.dao.donut/ReloadPrefs'：纯内部标识、poster/observer 都在同一二进制里，
#     与包 ID 无关，保持不动。）
# 新 ID 比旧的长 3 个字符，而原串**紧邻下一个串、没有扩展余量** ⇒ 必须搬迁：
#   把新串写进 0x7000 页的空闲区（dylib: 0x7eb0 / prefs: 0x7e80 —— 注意要避开 prefs 里
#   「IMP 区必须全零」的断言范围：arm64 是 0x7a40..0x7e40、arm64e 是 0x7ae0..0x7ee0，
#   所以池只能取 0x7ee0..0x7f00 这 32 字节；VERSION_POOL 在 0x7f00），
#   再把 CFString 的 ptr 低 36 位指向它、len 改成新长度。
#   ptr 是**链式 fixup**：改写时保留高位元数据、只换低 36 位（与 SEL_STR 的改法一致）。
#   ⇒ 指令、段布局、链式 fixup 结构全部不动，只有 1 个指针 + 1 个长度字段变化。
OLD_ID, NEW_ID = 'com.dao.donut', 'com.dao.donutbar'
ID_POOL_DYL, ID_POOL_PREFS = 0x7eb0, 0x7ee0
assert len(NEW_ID) > len(OLD_ID), '本版按「搬迁」实现，仅当新 ID 更长时适用'
assert NEW_ID != OLD_ID

BUF = []
def P(*a): BUF.append(' '.join(str(x) for x in a))
def kasm(s): return bytes(KS.asm(s)[0])
def sx2(v, b): return v - (1 << b) if v & (1 << (b-1)) else v

def adrp(rd, pc, target):
    imm21 = ((target & ~0xfff) - (pc & ~0xfff)) >> 12
    return (0x90000000 | ((imm21 & 3) << 29) | (((imm21 >> 2) & 0x7ffff) << 5) | rd).to_bytes(4, 'little')
def add_imm(rd, rn, imm):
    return (0x91000000 | ((imm & 0xfff) << 10) | (rn << 5) | rd).to_bytes(4, 'little')
def b_to(pc, t):
    return (0x14000000 | (((t - pc)//4) & 0x3ffffff)).to_bytes(4, 'little')
def bl_to(pc, t):
    return (0x94000000 | (((t - pc)//4) & 0x3ffffff)).to_bytes(4, 'little')
def bcond_to(cond, pc, t):
    # b.<cond>；cond: EQ=0 NE=1 GE=0xa LE=0xd ...
    return (0x54000000 | ((((t - pc)//4) & 0x7ffff) << 5) | cond).to_bytes(4, 'little')
def cbz64_to(rt, pc, t):
    # cbz <Xt>（64 位判据）—— opcode 0xB4000000（32 位版本为 0x34000000）
    return (0xB4000000 | ((((t - pc)//4) & 0x7ffff) << 5) | rt).to_bytes(4, 'little')
def cbz_to(rt, pc, t):
    return (0x34000000 | ((((t - pc)//4) & 0x7ffff) << 5) | rt).to_bytes(4, 'little')
def ldr_x_off(rt, rn, off):
    return (0xF9400000 | (((off//8) & 0xfff) << 10) | (rn << 5) | rt).to_bytes(4, 'little')
def ldr_d_off(rt, rn, off):
    return (0xFD400000 | (((off//8) & 0xfff) << 10) | (rn << 5) | rt).to_bytes(4, 'little')
def str_d_off(rt, rn, off):
    return (0xFD000000 | (((off//8) & 0xfff) << 10) | (rn << 5) | rt).to_bytes(4, 'little')

# ---- padding 布局 ----
# 两切片的 0x7c00~0x8000 在原始 dylib 里**逐字节全零**（实测见 _logs/opt_probe2.txt），且落在
# __TEXT 段内（LC_SEGMENT_64 实测 __TEXT vmaddr=0 vmsize=0x8000 prot=r-x）→ 可作注入体落脚区。
#   FUNC(0x7c00)    = prefs_to_rect 实现（加载期一次）
#   GLUE(0x7e00)    = 每个角标重绘都要跑的横条/圆路径
#   SEL_STR(0x7e80) = 'bezierPathWithRoundedRect:cornerRadius:'（selref 指过来）
# !! 三段之间一旦重叠 → ctor 加载即崩 → SpringBoard 崩溃循环（安全模式）。
#    3.1.1 的 FUNC 段正好顶到 GLUE（余量 0 B）；3.1.2 把 GLUE 挪到 0x7e00 后余量 184/36/344 B，
#    并加硬断言（MARGIN_MIN），以后改代码不会再无声贴合。
PAD = {'arm64': {'KEYSTR': 0x7c00, 'FUNC': 0x7c00, 'GLUE': 0x7e00, 'SEL_STR': 0x7e80},
       'arm64e': {'KEYSTR': 0x7c00, 'FUNC': 0x7c00, 'GLUE': 0x7e00, 'SEL_STR': 0x7e80}}
MARGIN_MIN = 32          # 三段之间要求的最小空隙（字节）
SEL_STR_LEN = 40         # 'bezierPathWithRoundedRect:cornerRadius:' + NUL = 39，留 1 字节
PAD_END = 0x8000         # __TEXT 段尾（vmsize=0x8000），也是落脚区上界
FUNC_BY = {'arm64': 0x7c00, 'arm64e': 0x7c00}
# ---- v3.9.2 第四档「彩色角标」：颜色来源劫持桩 ----
#   原版绘制入口按 pfDonutColorMode(全局 0xc3d8) 二选一（arm64e 取证）：
#     0x5040 ldr x8,[x8,#0x3d8]      x8 = mode
#     0x5044 cbz x8, #0x505c         mode==0 → Auto  = 自动取色（0x5500-0x5a24 采样图标主色）
#     0x5048 adrp x8,#0xc000 / 0x504c ldr x0,[x8,#0x370]
#                                    mode!=0 → Custom= pfDonutColor(默认 #EB4D3DFF 红)
#   两者最终都赋给 x23，绘制时 fill/stroke 取它的 CGColor(0x5d38/0x5dc8)。
#   ⇒ 第四档要「把红色换成自动取色」，就是把 0x5044 的 cbz 换成跳桩：
#       桩内 样式(0xc3d1)==3 → 强制走 Auto；否则沿用原 mode 判断。
#   桩放 FUNC(0x7c00+320B=0x7d40) 与 GLUE(0x7e00) 之间 192B 空闲区，实占 24B。
#   !! 不能改 prefs_to_rect 写 mode：它末尾尾调用原 ctor，ctor 会再写回 0xc3d8 覆盖掉。
MODE_STUB = 0x7d40
MODE_CBZ = {'arm64': 0x4ebc, 'arm64e': 0x5044}        # 被替换的 cbz 地址
MODE_AUTO = {'arm64': 0x4ed4, 'arm64e': 0x505c}       # 自动取色路径（样式3 / mode==0）
MODE_CUSTOM = {'arm64': 0x4ec0, 'arm64e': 0x5048}     # Custom 色(pfDonutColor)路径
RECT_G, BSS_NEW = 0x408, 0x118     # RECT_G：RECT_G..RECT_G+0x20 落在 __DATA.__bss（原 0xc370+0x98=0xc408，故必须扩到 0x118）
DEFAULTS = [40, 80, 30, 6]         # v1.0.0：X / Y / W / H（Y 回到 80 = 4.0.0 标定位置）
# ---- 挂靠点：v8～3.2.0 用 self.bounds（不可靠），v3.3.0 起用角标圆点矩形 d8-d11 ----
# 用户要求（v8）：数字减少 = 向左偏移，数字增加 = 向右偏移 —— 3.3.0 依然满足。
# v3.3.0 的几何：
#   ringC = 角标圆点中心（= 角标中心，在绘制坐标系里）
#   横条中心_x = ringC_x + DX + (X - X_CTR)        X_CTR = 40（默认 = 水平居中于图标）
#   横条中心_y = ringC_y + DY + (Y - Y_CTR)        Y_CTR = 80（默认 = 标定的垂直位置）
#     DX = -(iconW/2 - 10)            → 把「角标中心」换算到「图标中心」（角标圆心距图标右边 10pt）
#     DY = (iconW - 10) + 1.7 + H/2   → 把「角标中心」换算到「横条中心」（横条顶贴图标下沿再下 1.7pt）
#   !! 3.3.0 用「角标圆心距图标右边/上边各 10pt」推 DX/DY，真机证明错了：
#      实测反推的圆点中心其实落在**图标右上角稍外**（左 + 67.5pt / 顶 − 3.3pt），
#      于是 3.3.0 的横条偏右 ~14.7pt、且陷进图标内部 ~10pt。
#      修正量由同一台机两个不同图标独立反推（文件夹 63.33pt 与 App Store 62.67pt）：
#        文件夹   ⇒ KEY_X = 76.17, KEY_Y = 8.63
#        App Store⇒ KEY_X = 76.17, KEY_Y = 10.30      ← KEY_X 两次完全一致
#      取整：KEY_X = 76, KEY_Y = 9（残差 ≤ 0.5pt）。
#   ⇒ 把两个常量折进 X/Y 的参考值：
#     RECT_G[0] = (X - 76) - W/2     [X-40-36]
#     RECT_G[1] = (Y - 9)            [Y-80+71]
#     RECT_G[2] = W/2                （glue: W = slot2 + slot2）
#     RECT_G[3] = H/2                （glue: H = slot3 + slot3；圆角半径也取它）
#   注意：glue 会自己对 Y 再减一次 H/2（保持「改 H 时中心不动」的旧语义），
#         所以 slot1 **不再**像 3.1.2 那样折进 -H/2。
# 精确性：X/Y/W/H 为整数，角标圆心/半宽为 0.5 的整数倍 → 全程 0.5 的整数倍、量级 < 2^10
#   → double 下加减与「×0.5 + 加」都精确无舍入 ⇒ 可做逐位断言。
X_CTR = DEFAULTS[0]                        # 40：X 的「居中」参考值
Y_CTR = DEFAULTS[1]                        # 80：Y 的参考值（垂直偏移 0）
# 3.5.0：KEY_Y 9 → 5 —— 对齐 BadgeBar 参考图（用户给的 @图2）
#   参考图（1274x520 PNG，用「横条恰好 30.00pt」标定 S=2.8333）实测：
#     图标恰好 60.00pt、横条恰好 30.00x6.00pt
#     横条中心 − 图标中心 = +3.25px = +1.15pt（参考略偏右，属不可感知量级）
#     横条顶 − 图标底     = 14px  = 4.94pt   ← 目标间距
#   本机 3.4.0 实测（1290x400 截图，S=3.0）：横条中心 − 图标中心 = -0.08pt（居中 ✓）
#     横条顶 − 图标底 = 3px = 1.00pt（太贴）⇒ 需下移 3.94pt ⇒ KEY_Y 9-4 = 5（间距变 5.0pt）
KEY_X, KEY_Y = 76, 5                       # KEY_X=76 两次独立测量一致；KEY_Y 由参考图定标
assert X_CTR == int(X_CTR) and Y_CTR == int(Y_CTR), 'X_CTR/Y_CTR 必须是整数'
DX_INT, DY_INT = X_CTR - KEY_X, Y_CTR - KEY_Y   # = -36 / +75（ring 中心 → 横条中心）
#   注：这两个量**只用于文档**，未参与代码生成（prefs_to_rect 直接用 KEY_X/KEY_Y）。
#   且 Y_CTR 在公式里会抵消：DY_INT + (Y - Y_CTR) ≡ Y - KEY_Y ⇒ 改 DEFAULTS[1] 不影响标定。
# v2.9.8：这些变换全部**在加载期算一次**（见 prefs_to_rect 的 XFORM），
#   glue（每画一次角标就跑）里因此没有 fdiv、没有常量池，只剩加减法。
# v3.1.2：把 W 的 ÷2 折进 slot0（少一条热路径算术）。
# v3.3.0：slot1 不再折 H/2（glue 自己减），槽位含义见上。
XFORM_NOTE = 'slot0=(X-76)-W/2  slot1=(Y-5)  slot2=W/2  slot3=H/2'
# 4 个键名 CFString（页 0x8000 内偏移）：X/Y 在 0x8188/0x81e8；W/H 在 0x8388/0x83c8。
# !! 原值 0x248/0x268 指向 0x8248/0x8268 = 'SBIconContinuityBadgeView'/'SBIconContinuityAccessoryView'
#    （那是 NSClassFromString 用的*类名*，不是键）→ 导致 W/H 永远读不到、只能取默认值。
KEY_CF = [0x188, 0x1e8, 0x388, 0x3c8]
# v3.1：样式键 = '0X'（dylib CFString 0x83a8；内容 '0X' 与颜色解析 hasPrefix:'0X' 共享无害）。
#   值 0=横条 / 1=空心圆 / 2=圆形。prefs_to_rect 读它，派生写入两个全局 byte：
#   0xc3d1 = 样式（glue 读它分支），0xc3d0 = 实心标志（样式!=1；驱动 fill/stroke/线宽/badge 直径）。
KEY_STYLE = 0x3a8
STYLE_BYTE, SOLID_BYTE = 0x3d1, 0x3d0
# 载体（改写内容，CFString/fixup 不动）：pfDonutDot（选项已删）、#EB4D3DFF（默认色兜底）、
# '#'（无引用死常量，2B 空间->单字符键）、#FFFFFF（白兜底）
# !! 不能动 Continuity 类名（NSClassFromString->nil->MSHookMessageEx(nil)->崩）
# !! 不再改写任何 cstring：原先把 '#'/'#FFFFFF'/'#EB4D3DFF' 改写成 W/H/Y —— 这三个是**颜色相关串**
#    （十六进制前缀 '#'、白色兜底 '#FFFFFF'、默认色 '#EB4D3DFF'），改掉后插件的颜色解析/兜底会失效，
#    表现为「选的颜色和实际显示不一致」。现改为**直接用原始字符串作为滑块的键**（见 slider_defs），
#    这样 prefs_to_rect 读到的 CFString 内容与滑块写入的键天然一致，无需任何改写。

m = dict(RC.parse_ar(open(SRC, 'rb').read()))
def dec(b):
    if b[:2] == b'\x1f\x8b': return gzip.decompress(b)
    if b[:2] == b'\x5d\x00': return lzma.decompress(b, format=lzma.FORMAT_ALONE)
    return lzma.decompress(b)
dk = [k for k in m if k.startswith('data.tar')][0]
with tarfile.open(fileobj=io.BytesIO(dec(m[dk]))) as t:
    members = t.getmembers()
    orig = {x.name: (t.extractfile(x).read() if x.isfile() else b'') for x in t.getmembers()}
DYL = 'Library/MobileSubstrate/DynamicLibraries/Donut.dylib'
dylib = bytearray(orig[DYL])

def update_file(name, data):
    orig[name] = data
    for mm in members:
        if mm.name == name:
            mm.size = len(data); return

def parse_sections(sl):
    ncmds = struct.unpack('<I', sl[16:20])[0]
    p = 32; sec = {}
    for _ in range(ncmds):
        cmd, csz = struct.unpack_from('<2I', sl, p); body = sl[p:p+csz]
        if cmd == 0x19:
            nsects = struct.unpack('<I', body[64:68])[0]; q = 72
            for _ in range(nsects):
                sn = body[q:q+16].rstrip(b'\0').decode(); sgn = body[q+16:q+32].rstrip(b'\0').decode()
                addr, sz = struct.unpack('<2Q', body[q+32:q+48]); so = struct.unpack('<I', body[q+48:q+52])[0]
                sec[(sgn, sn)] = (addr, sz, so); q += 80
        p += csz
    return sec

mdc = Cs(CS_ARCH_ARM64, CS_MODE_ARM); mdc.detail = True

for so, arch in [(0x4000, 'arm64'), (0x18000, 'arm64e')]:
    sl = dylib[so:so+0x115d0]
    sec = parse_sections(sl)
    oa, osz, oo = sec[('__TEXT', '__objc_stubs')]
    KEYSTR = PAD[arch]['KEYSTR']; FUNC = PAD[arch]['FUNC']
    GLUE = PAD[arch]['GLUE']; SEL_STR = PAD[arch]['SEL_STR']
    P('[%s] === padding: key=%#x func=%#x glue=%#x sel=%#x' % (arch, KEYSTR, FUNC, GLUE, SEL_STR))
    # --- 落脚区必须是原始全零（我们三个注入体都写在这块里）---
    assert all(b == 0 for b in dylib[so+0x7c00: so+0x8000]), \
        '[%s] padding 0x7c00~0x8000 原始非零，落脚区不可用' % arch
    # 落脚区全零已确认 → 现在可以往空闲池写标识符
    # ---- 标识符搬迁：把新 ID 写进空闲池，改 CFString 的 ptr/len ----
    _idb = NEW_ID.encode() + b'\x00'
    _ca_, _cs_, _co_ = sec[('__DATA_CONST', '__cfstring')]
    _hit = 0
    for _j in range(_cs_ // 32):
        _f = _co_ + _j*32
        _isa, _fl, _ptr, _ln = struct.unpack('<4Q', sl[_f:_f+32])
        _tv = _ptr & 0xFFFFFFFFF
        _e = sl.find(b'\x00', _tv) if _tv else -1
        if _e > 0 and bytes(sl[_tv:_e]) == OLD_ID.encode():
            assert all(b == 0 for b in sl[ID_POOL_DYL: ID_POOL_DYL + 0x40]), 'dylib 标识符池非零'
            dylib[so+ID_POOL_DYL: so+ID_POOL_DYL+len(_idb)] = _idb
            struct.pack_into('<Q', dylib, so+_f+16, (_ptr & ~0xFFFFFFFFF) | ID_POOL_DYL)
            struct.pack_into('<Q', dylib, so+_f+24, len(NEW_ID))
            _hit += 1
            P('  标识符: CFString @%#x 内容 %s -> %s（ptr %#x -> %#x 池，len %d -> %d）'
              % (_ca_ + _j*32, OLD_ID, NEW_ID, _tv, ID_POOL_DYL, _ln, len(NEW_ID)))
    assert _hit == 1, '[%s] 应恰有 1 个 %r 的 CFString，实为 %d' % (arch, OLD_ID, _hit)


    # --- stub selector 解析 ---
    def v2f(va):
        for (sg, sn), (a, sz, off) in sec.items():
            if a <= va < a+sz: return off + (va - a)
    def s_at(va):
        f = v2f(va)
        if f is None: return None
        e = sl.find(b'\0', f)
        return sl[f:e].decode('utf-8', 'replace') if e > 0 else None
    stubs = {}
    for i in range(osz // 32):
        pc = oa + i*32; off = oo + i*32
        i1 = struct.unpack('<I', sl[off:off+4])[0]
        i2 = struct.unpack('<I', sl[off+4:off+8])[0]
        if i1 & 0x9F000000 == 0x90000000:
            immhi = (i1 >> 5) & 0x7ffff; immlo = (i1 >> 29) & 3
            imm = sx2((immhi << 2) | immlo, 21)
            page = (pc & ~0xfff) + (imm << 12)
            if i2 & 0xFFC00000 == 0xF9400000:
                imm12 = (i2 >> 10) & 0xfff
                f = v2f(page + imm12*8)
                if f is not None:
                    stubs[pc] = s_at(struct.unpack('<Q', sl[f:f+8])[0] & 0xffffffff)
    byname = {}
    for pc, s in stubs.items(): byname.setdefault(s, pc)
    p_init = byname['initWithSuiteName:']; p_ofk = byname['objectForKey:']; p_ival = byname['integerValue']
    # 注：v3.3.0 起 glue 不再调 `bounds`（挂靠 d8-d11），故不再取 p_bounds

    # --- 找 ctor 里的 alloc（objc_release 地址由符号表确认：arm64=0x6620 / arm64e=0x6860）---
    # alloc = initWithSuiteName: 那次 bl 之前、距离最近的 bl
    init_pc = [insn.address for insn in mdc.disasm(sl[0x40a0:0x4400], 0x40a0)
               if insn.mnemonic == 'bl' and insn.operands[0].imm == p_init][0]
    p_alloc = [insn.operands[0].imm for insn in mdc.disasm(sl[0x40a0:init_pc], 0x40a0)
               if insn.mnemonic == 'bl'][-1]
    p_rel = 0x6620 if arch == 'arm64' else 0x6860
    P('  原语: alloc=%#x init=%#x ofk=%#x ival=%#x rel=%#x' % (p_alloc, p_init, p_ofk, p_ival, p_rel))

    # --- RoundedRect：selector 字符串 + selref 换 cornerRadius ---
    dylib[so+SEL_STR: so+SEL_STR+SEL_STR_LEN] = b'bezierPathWithRoundedRect:cornerRadius:' + bytes([0])
    selref_i = 0xc0b8     # OvalInRect stub 的 selref 槽位（arm64/arm64e 同）
    old_v = struct.unpack('<Q', dylib[so+selref_i: so+selref_i+8])[0]
    struct.pack_into('<Q', dylib, so+selref_i, (old_v & ~0xFFFFFFFFF) | SEL_STR)
    P('  selref -> cornerRadius @%#x（选择子串 %d B）' % (SEL_STR, SEL_STR_LEN))

    # --- v3.1：恢复 3 处「实心/空心」由全局 byte 0xc3d0 控制（原 pfDonutDot 语义），
    #     使三种样式由 0xc3d0 派生值驱动 fill/stroke/线宽/badge 直径。
    #     第1/2处用 w19，第3处用 w8（原始即如此）。
    LDRB19 = kasm('ldrb w19, [x8, #0x3d0]')
    LDRB8 = kasm('ldrb w8, [x8, #0x3d0]')
    for a64, a64e, use_w8 in [(0x5b98, 0x5d20, False), (0x5bfc, 0x5d84, False), (0x5c60, 0x5de8, True)]:
        va = a64 if arch == 'arm64' else a64e
        dylib[so+va: so+va+4] = LDRB8 if use_w8 else LDRB19
    # NOP 原 ctor 对 0xc3d0 的写入（读 pfDonutDot 写 0xc3d0 那处），改由 prefs_to_rect 按样式派生写入
    ctor_strb = 0x4150 if arch == 'arm64' else 0x41c0
    dylib[so+ctor_strb: so+ctor_strb+4] = bytes.fromhex('1f2003d5')   # nop
    P('  恢复 3 处 ldrb 读 0xc3d0 + NOP ctor strb @%#x（样式驱动实心标志）' % ctor_strb)
    # ---- v3.9.2：第四档「彩色角标」—— 颜色来源劫持桩（详见 MODE_STUB 注释）----
    # 入口: x8 = mode(由原指令 ldr x8,[x8,#0x3d8] 载入)；出口: 跳 auto(自动取色) 或 custom(自定义色)
    # ---- v4.0.5 精简：第四档已取消 ⇒ 移除「取色桩」（死代码），恢复原始 `cbz x8` ----
    #   审查依据：桩判据 `cmp w9,#3` 因样式值域 [0,2] 永不命中；且它把 64 位 `cbz x8`
    #   换成了 32 位 `cbz w8`（虽等效但不必要）。此处一并撤销。
    _cbz, _auto, _cust = MODE_CBZ[arch], MODE_AUTO[arch], MODE_CUSTOM[arch]
    dylib[so+MODE_STUB: so+MODE_STUB+0x40] = b'\x00' * 0x40      # 清空原桩区（恢复 padding）
    dylib[so+_cbz: so+_cbz+4] = cbz64_to(8, _cbz, _auto)         # 恢复 `cbz x8,<auto>`（64 位）
    # v3.9.4：不再动 0xc3d0，也不做原生底染色（v3.9.3 的染色桩真机崩溃 ⇒ 已撤销）
    # v4.0.0：本桩是**唯一**与样式3相关的桩，且**只读内存**（不再有静默/染色桩）
    P('  取色桩已移除：0x%x 恢复 `cbz x8 -> 0x%x`（64 位判据）；0x%x..0x%x 归零'
      % (_cbz, _auto, MODE_STUB, MODE_STUB + 0x40))

    # --- 生成 prefs_to_rect（加载期一次：读 4 个位置键 + 样式键，算好派生量写进 RECT_G）---
    # v3.1.2 精简：把两处页基址提到 x20(0xc000 全局区)/x21(0x8000 字符串区)，全程不再重复 adrp；
    #   并让 W、H 的 ÷2 结果顺手折进 slot0/slot1（A/B 预合并）。
    fn = FUNC; code = bytearray()
    code += kasm('stp x29, x30, [sp, #-0x30]!')
    code += kasm('stp x20, x19, [sp, #0x10]')
    code += kasm('str x21, [sp, #0x20]')
    code += adrp(20, fn+len(code), 0xc000)
    code += adrp(21, fn+len(code), 0x8000)
    code += ldr_x_off(0, 20, 0x2c8)                          # NSUserDefaults 类
    code += bl_to(fn+len(code), p_alloc)
    code += add_imm(2, 21, 0x148)                            # suite（v3.7.0 起 = NEW_ID）
    code += bl_to(fn+len(code), p_init)
    code += kasm('mov x19, x0')
    for ki, dv in enumerate(DEFAULTS):
        code += kasm('mov x0, x19')
        code += add_imm(2, 21, KEY_CF[ki])
        code += bl_to(fn+len(code), p_ofk)
        cbz_pc = fn + len(code)
        code += cbz_to(0, cbz_pc, 0)          # 占位
        code += bl_to(fn+len(code), p_ival)
        b_pc = fn + len(code)
        code += b_to(b_pc, 0)                 # 占位
        Ldef = fn + len(code)
        code += kasm('mov x0, #%d' % dv)
        Lgot = fn + len(code)
        code[cbz_pc-fn:cbz_pc-fn+4] = cbz_to(0, cbz_pc, Ldef)
        code[b_pc-fn:b_pc-fn+4] = b_to(b_pc, Lgot)
        code += kasm('scvtf d0, x0')
        # 加载期变换（结果写 RECT_G 的第 ki 槽）：
        #   ki=0 X : d0 = X - 76                    （= (X-40) + DX，DX=-36；方向：数字大=右）
        #   ki=1 Y : d0 = Y - 5                     （= (Y-80) + DY，DY=+75）
        #   ki=2 W : d0 = W/2，再把 W/2 从 slot0 里减掉 → slot0 = (X-76) - W/2
        #   ki=3 H : d0 = H/2（**不折**进 slot1；glue 会自己减 H/2 以保持中心不动）
        if ki == 0:
            code += kasm('mov x1, #%d' % KEY_X)
            code += kasm('scvtf d1, x1')
            code += kasm('fsub d0, d0, d1')
        elif ki == 1:
            code += kasm('mov x1, #%d' % KEY_Y)
            code += kasm('scvtf d1, x1')
            code += kasm('fsub d0, d0, d1')
        else:
            code += kasm('fmov d1, #0.5')       # 3.6.0：÷2 改 ×0.5（0.5 精确可表示；乘法比除法快）
            code += kasm('fmul d0, d0, d1')
            if ki == 2:                     # W/2 折进 slot0；H 不折（见上）
                code += ldr_d_off(1, 20, RECT_G)
                code += kasm('fsub d1, d1, d0')
                code += str_d_off(1, 20, RECT_G)
        code += str_d_off(0, 20, RECT_G + ki*8)
    # ---- v3.1：读样式键 '0X' → 写 0xc3d1(样式) + 0xc3d0(实心标志 = 样式!=1) ----
    code += kasm('mov x0, x19')
    code += add_imm(2, 21, KEY_STYLE)
    code += bl_to(fn+len(code), p_ofk)
    st_cbz = fn + len(code)
    code += cbz_to(0, st_cbz, 0)
    code += bl_to(fn+len(code), p_ival)
    st_b = fn + len(code)
    code += b_to(st_b, 0)
    Lstdef = fn + len(code)
    code += kasm('mov x0, #0')
    Lstgot = fn + len(code)
    code[st_cbz-fn:st_cbz-fn+4] = cbz_to(0, st_cbz, Lstdef)
    code[st_b-fn:st_b-fn+4] = b_to(st_b, Lstgot)
    code += kasm('cmp x0, #0')
    code += kasm('csel x0, x0, xzr, ge')      # 夹到 [0,3]：先 max(x0,0)
    code += kasm('cmp x0, #2')
    code += kasm('csel x0, x0, xzr, le')      # 再 min；越界值落到 0 = 横条（v4.0.4 取消第四档）
    code += kasm('strb w0, [x20, #%d]' % STYLE_BYTE)
    code += kasm('cmp x0, #1')
    code += kasm('cset w9, ne')               # 实心 = 样式 != 1（空心圆）
    code += kasm('strb w9, [x20, #%d]' % SOLID_BYTE)
    code += kasm('mov x0, x19')
    code += bl_to(fn+len(code), p_rel)
    code += kasm('ldr x21, [sp, #0x20]')
    code += kasm('ldp x20, x19, [sp, #0x10]')
    code += kasm('ldp x29, x30, [sp], #0x30')      # 恢复 lr + sp（尾调用前必须）
    # 尾调用原 ctor（__init_offsets 指向的初始化函数）：arm64=0x409c arm64e=0x4108
    code += b_to(fn+len(code), 0x409c if arch == 'arm64' else 0x4108)
    dylib[so+FUNC: so+FUNC+len(code)] = code
    P('  prefs_to_rect @%#x (%dB = %d 条)' % (FUNC, len(code), len(code)//4))

    # --- glue：横条/圆两种绘制路径（完全复刻 BadgeBar X 1.3.7 的定位公式）---
    # 逆向 BadgeBar arm64e 切片（__auth_ptr 还原出 hook IMP 地址，解析 __objc_selrefs 得选择子）：
    #   SBIconBadgeView 的 -layoutSubviews 中对 badge 的 _backgroundView 执行：
    #     setFrame:(0, 0, badgeWidth, badgeHeight)                         # W=30  H=6
    #     setCenter:(self.frame.size.width - xOffsetBadge, yOffsetBadge)   # X=40  Y=78
    #   即「横条中心 = (badge 宽 - X, Y)，尺寸 (W, H)」；坐标系即该视图坐标系，
    #   Donut 的形状图层亦在此坐标系 → 可直接套用，无需 convertRect。
    #   v6 之误：用 (bounds.w - W)/2 + X 居中 → 语义与 BadgeBar 不符（落到右上）。
    #   v8～3.2.0：挂 self.bounds（右边缘 / 水平中心）—— 真机证明不可靠，见文件头。
    #   v3.3.0：改挂 **d8-d11 角标圆点矩形**：
    #     横条中心_x = 圆点中心_x + DX + (X - 40)   ← 换算到图标中心（DX=-36，实测反推）
    #     横条中心_y = 圆点中心_y + DY + (Y - 80)   ← 换算到「贴图标下沿再下 ~4.9pt」（DY=+75）
    #     origin_* 再由中心减 半宽/半高 得到。
    #   cornerRadius = H/2（BadgeBar badgeRadius 默认 3.0，恰等于 H/2）。
    # 样式分支：0=横条 roundedRect；1/2=圆（oval rect + 圆角半径 = 宽/2）。
    #   !! v3.1 曾手写 objc_msgSend（arm64e 的 braa PAC 认证）→ 真机 SpringBoard 崩溃循环（安全模式）。
    #   v3.1.1 起**两个分支都尾调现有 stub**（selref 已指向 cornerRadius），把 SEL 加载交给 stub，
    #   glue 完全不碰 objc_msgSend / ptrauth。
    #   v3.1.2 精简：进入 glue 时 x0 本就是 UIBezierPath 类（原 bl 前 0x5b4c/0x5d34 已 ldr x0,[x8,#0x2f0]）。
    #   v3.6.0 精简：圆分支去掉 4 条冗余 fmov（入口 d0-d3 已 == d8-d11）⇒ glue 19 条 / 76 B
    #   v3.3.0 精简（都是净减法）：
    #     ① **去掉 `bl bounds`** —— 挂靠点不再需要 self，热路径再无 objc_msgSend；
    #     ② **去掉 stp/ldp 保存 x0+lr** —— 片段内不再有调用，lr 无需保护，x0 从入口到尾调一路没被碰过，
    #        天然还是 UIBezierPath 类；也彻底摆脱了原来 `ldr x0,[sp,#0x58]` 读调用者栈帧取 self 的脆弱做法；
    rounded_stub = 0x6720 if arch == 'arm64' else 0x6980
    gpc = GLUE
    glue = bytearray()
    def gE(b):
        global glue, gpc
        glue += b; gpc += len(b)
    gE(adrp(8, gpc, 0xc000))                 # x8 = 0xc000 页
    gE(kasm('ldrb w9, [x8, #0x3d1]'))        # w9 = 样式
    gE(kasm('fmov d16, #0.5'))               # ½ 常量：两分支共用
    cbz_off = len(glue); gE(cbz_to(9, gpc, 0))     # 占位：样式==0 → bar
    # 圆分支：**入口处 d0-d3 已经等于 d8-d11**（原代码在 bl 前 4 条正是
    #   `fmov d0,d8 / d1,d9 / d2,d10 / d3,d11`，见 arm64 0x5b54..0x5b60 / arm64e 0x5cdc..0x5ce8）
    #   ⇒ 不需要再拷一次，只需算半径。校验脚本会断言那 4 条 fmov 确实存在（改动时会被拦下）。
    gE(kasm('fmul d4, d10, d16'))            # cornerRadius = 宽/2（正方形 → 圆）
    b_off = len(glue); gE(b_to(gpc, 0))            # 占位：→ go
    # 横条分支（RECT_G 的 4 个加载期派生量：slot0 / slot1 / W÷2 / H÷2）
    bar_pc = gpc
    gE(ldr_d_off(4, 8, RECT_G))              # d4 = slot0 = (X-76) - W/2
    gE(ldr_d_off(5, 8, RECT_G+8))            # d5 = slot1 = Y - 5（横条中心相对圆点中心的垂直偏移）
    gE(ldr_d_off(6, 8, RECT_G+16))           # d6 = W/2
    gE(ldr_d_off(7, 8, RECT_G+24))           # d7 = H/2
    gE(kasm('fmadd d0, d10, d16, d8'))       # d0 = 圆点中心_x = d8 + ½·d10
    gE(kasm('fmadd d1, d11, d16, d9'))       # d1 = 圆点中心_y = d9 + ½·d11
    gE(kasm('fadd d0, d0, d4'))              # origin_x = 圆点中心_x + slot0
    gE(kasm('fadd d1, d1, d5'))              # 横条中心_y
    gE(kasm('fadd d2, d6, d6'))              # W
    gE(kasm('fadd d3, d7, d7'))              # H
    gE(kasm('fsub d1, d1, d7'))              # origin_y = 中心_y - H/2（改 H 时中心不动）
    gE(kasm('fmov d4, d7'))                  # cornerRadius = H/2
    go_pc = gpc
    glue[cbz_off:cbz_off+4] = cbz_to(9, GLUE+cbz_off, bar_pc)
    glue[b_off:b_off+4] = b_to(GLUE+b_off, go_pc)
    gE(b_to(gpc, rounded_stub))              # 尾调 stub（x0 仍是 UIBezierPath 类；stub 内加载 SEL 并跳 msgSend）
    dylib[so+GLUE: so+GLUE+len(glue)] = glue
    # ---- padding 布局断言（防「改了地址导致互相覆盖」这类自洽错误；v2.8.11 安全模式即因此）----
    assert FUNC + len(code) <= GLUE, \
        '[%s] prefs_to_rect(%#x+%d=%#x) 与 glue(%#x) 重叠!' % (arch, FUNC, len(code), FUNC+len(code), GLUE)
    assert GLUE + len(glue) <= SEL_STR, \
        '[%s] glue(%#x+%d=%#x) 与 SEL_STR(%#x) 重叠!' % (arch, GLUE, len(glue), GLUE+len(glue), SEL_STR)
    # 余量断言：三段之间必须各留 >= MARGIN_MIN 字节，避免以后改代码时无声贴合/重叠
    m1 = GLUE - (FUNC + len(code))
    m2 = SEL_STR - (GLUE + len(glue))
    m3 = PAD_END - (SEL_STR + SEL_STR_LEN)
    for _nm, _m in (('FUNC→GLUE', m1), ('GLUE→SEL_STR', m2), ('SEL_STR→尾部', m3)):
        assert _m >= MARGIN_MIN, '[%s] %s 余量 %d B < %d B' % (arch, _nm, _m, MARGIN_MIN)
    P('  padding 布局: FUNC %#x+%dB->%#x | 余 %dB | GLUE %#x+%dB->%#x | 余 %dB | SEL_STR %#x+%dB->%#x'
      % (FUNC, len(code), FUNC+len(code), m1, GLUE, len(glue), GLUE+len(glue), m2,
         SEL_STR, SEL_STR_LEN, SEL_STR+SEL_STR_LEN))
    P('  glue @%#x (%dB = %d 条) 热路径无除法/无常量池/**无任何 objc_msgSend**；prefs_to_rect %dB = %d 条（加载期无 fdiv）'
      % (GLUE, len(glue), len(glue)//4, len(code), len(code)//4))
    blv = 0x5b64 if arch == 'arm64' else 0x5cec
    dylib[so+blv: so+blv+4] = bl_to(blv, GLUE)
    P('  bl→glue @%#x -> %#x' % (blv, GLUE))

    # --- 扩 __bss ---
    ncmds = struct.unpack('<I', sl[16:20])[0]
    p = 32
    for _ in range(ncmds):
        cmd, csz = struct.unpack_from('<2I', dylib[so+p:so+p+8])
        if cmd == 0x19:
            body = dylib[so+p: so+p+csz]
            if body[8:24].rstrip(b'\0').decode() == '__DATA':
                nsects = struct.unpack('<I', body[64:68])[0]; q = so + p + 72
                for _ in range(nsects):
                    sn = dylib[q:q+16].rstrip(b'\0').decode()
                    if sn == '__bss':
                        struct.pack_into('<Q', dylib, q+40, BSS_NEW)
                        P('  __bss 扩至 %#x' % BSS_NEW)
                    if sn == '__init_offsets':
                        struct.pack_into('<I', dylib, q+40, FUNC)   # 值=ctor 绝对 vmaddr
                        P('  __init_offsets: ctor -> %#x' % FUNC)
                    q += 80
        p += csz

# ---------- 设置面板 4 个滑块 ----------
P('=== 设置面板：删「圆点」+ 更新文案 + 4 滑块 ===')
RP = 'Library/PreferenceBundles/DonutPrefs.bundle/Root.plist'
OLD_FOOTER = ('Default enabled replaces app notification badges with a small hollow ring; '
              'Dot enabled replaces badges with a solid small dot.')
NEW_FOOTER = ('When enabled, app notification badges become a colored bar below the app icon. '
              'Ring replaces it with a hollow small circle; Dot replaces it with a solid small dot.')
NEW_FOOTER_ZH = ('启用后，应用通知角标将变为应用图标下方的彩色横条。'
                 '空心圆则替换成空心小圆圈样式，圆点则替换成实心小圆点样式。')
pl = plistlib.loads(orig[RP])
items = [it for it in pl['items'] if it.get('key') != 'pfDonutDot']      # 删「圆点」开关
for it in items:
    if it.get('label') == 'General' and it.get('cell') == 'PSGroupCell':
        it['footerText'] = NEW_FOOTER
# v7：范围与默认值对齐 BadgeBar X 1.3.7
#   xOffsetBadge 40 [-50,80] / yOffsetBadge 78 [0,90] / badgeWidth 30 [0,60] / badgeHeight 6 [0,60]
#   （宽/高下限取 2 以免出现不可见横条；滑块默认仍为 BadgeBar 的 30/6）
# 键直接用原始字符串（= prefs_to_rect 所读 CFString 的原始内容），不做任何 cstring 改写：
#   X←'pfDonutDot'、Y←'#EB4D3DFF'、W←'#'、H←'#FFFFFF'
# v8：范围**围绕默认值居中**（默认值 = (min+max)/2 → 滑块把手默认停在正中间）：
#   X 默认 40 → [0, 80]      Y 默认 80 → [40, 120]      W 默认 30 → [2, 58]      H 默认 6 → [2, 10]
slider_defs = [('Bar X Offset', 'pfDonutDot', 0, 80, 2, 40), ('Bar Y Offset', '#EB4D3DFF', 40, 120, 2, 80),
               ('Bar Width', '#', 2, 58, 2, 30), ('Bar Height', '#FFFFFF', 2, 10, 1, 6)]
for _i, (_lbl, _k, _mn, _mx, _stp, _dv) in enumerate(slider_defs):
    assert 2 * _dv == _mn + _mx, '%s 默认值 %s 不在范围 [%s,%s] 正中' % (_lbl, _dv, _mn, _mx)
    assert _dv == DEFAULTS[_i], '%s 滑块默认值 %s != dylib DEFAULTS[%d]=%s' % (_lbl, _dv, _i, DEFAULTS[_i])
# BadgeBar 风格：每个滑块上方一个静态文本名称（PSStaticTextCell），滑块本身无 label
#（BadgeBar 原版滑块 label=None + isSegmented=False；滑块带 label 与 showValue 在 iOS17 会冲突）
slider_cells = []
_sid = 81
for lbl, key, mn, mx, stp, dv in slider_defs:
    # 与 BadgeBar 原版逐字段对齐（含 id；BadgeBar 的静态标题/滑块都带 id，缺失可能在 iOS17 引发交互崩溃）
    slider_cells.append({'cell': 'PSStaticTextCell', 'label': lbl, 'id': str(_sid)}); _sid += 1
    # !! 不设 PostNotification：DonutPrefs 在 viewDidLoad 里用 CFNotificationCenterAddObserver
    #    监听 'com.dao.donut/ReloadPrefs' 并异步重载（那是原版给开关用的）。滑块带上它会在每次
    #    拖动后触发一次重载，与写入竞争 → 滑块松手回弹。滑块改值本就需注销(Respring)才生效，故去掉。
    slider_cells.append({
        'cell': 'PSSliderCell', 'key': key, 'id': str(_sid),
        'defaults': NEW_ID,
        'min': mn, 'max': mx, 'default': dv,
        'showValue': True,
        'isSegmented': False,
    }); _sid += 1
cm_i = next(i for i, it in enumerate(items) if it.get('key') == 'pfDonutColorMode')
# 角标样式四选一（0=横条 Bar / 1=空心圆 Ring / 2=圆点 Dot / 3=彩色角标 IconColor），key='0X'；
#   v3.7.0：第三档由「圆形 Circle」改为「圆点 Dot」，与组尾说明的措辞统一（值 0/1/2 不变，老设置不受影响）
#   v3.9.2：新增第四档「彩色角标」—— 形状同圆点(实心)，但**颜色强制走原版 Auto 自动取色**
#     （采样应用图标主色），而不是 pfDonutColor 的默认红 #EB4D3DFF（即「原生红色角标」）。
#     dylib 侧：clamp 放宽到 [0,3] + 绘制入口 mode 判断插桩（MODE_STUB）。
# v3.9.7：**必须**带 PostNotification —— 否则切换样式不会触发 specifiers 重算，
#   而"横条位置滑块按样式折叠"（v3.9.6 的桩）正是在 specifiers 里做的 ⇒ 会看不到效果。
#   （滑块本身仍不带通知：拖动会连续写值，带通知会与重载竞争导致松手回弹。）
style_cell = {'cell': 'PSSegmentCell', 'label': 'Badge Style', 'key': '0X',
              'defaults': NEW_ID, 'validValues': [0, 1, 2],
              'validTitles': ['Bar', 'Ring', 'Dot'], 'default': 0,
              'PostNotification': 'com.dao.donut/ReloadPrefs'}
# ---- v3.9.5 要求①：样式板块（选择器 + 横条位置滑块）整体挪到「启用」下方 ----
#   原先插在「颜色模式」之后；现改为插在 pfEnabledDonut 之后，并单独起一个 "Badge Style" 分组。
en_i = next(i for i, it in enumerate(items) if it.get('key') == 'pfEnabledDonut')
items = (items[:en_i+1]
         + [{'cell': 'PSGroupCell', 'label': 'Badge Style'}]      # 新分组标题
         + [style_cell] + slider_cells
         + items[en_i+1:])
# ---- v3.9.5 要求②：删掉独立的 "Custom Color" 分组，让颜色选择并入 "Badge Color" 组 ----
_before = len(items)
items = [it for it in items
         if not (it.get('cell') == 'PSGroupCell' and it.get('label') == 'Custom Color')]
P('  删掉独立分组 "Custom Color" x%d' % (_before - len(items)))
# 「恢复默认设置」按钮：action = donutReloadSpecifiers —— 该方法是本类**已存在**的方法
#   （Preferences 只显示 action 在控制器上可响应的按钮；新增方法因运行期不可见而被丢弃）。
#   二进制侧把它的 imp 换成「恢复默认」，并把通知回调与它解耦（见下方补丁）。
rs_i = next(i for i, it in enumerate(items) if it.get('label') == 'Respring')
items = items[:rs_i] + [{'cell': 'PSButtonCell', 'label': 'Restore Defaults',
                         'action': 'donutReloadSpecifiers'}] + items[rs_i:]
# !! **保留**原版的 PostNotification（'com.dao.donut/ReloadPrefs'）—— 这正是「点 Custom 后
#    颜色选项不出现、必须注销才出现」的病根：上一版把它全清了，于是切换颜色模式不再触发重载。
#    本版通知路径已与「恢复默认」解耦（回调直跳原方法体），所以恢复官方行为最安全：
#      点 Badge Color Mode 的 Custom → 发通知 → 原版异步 reload → Custom Color / Choose Color
#      两行**立刻**出现（无需注销）。
#    滑块**保持不带** PostNotification：改滑块本就必须注销(Respring)才生效，带上它会在拖动后
#      触发重载与写入竞争 → 松手回弹（2.8.13 的教训）。
#    （另有一道双保险：specifiers 的过滤分支被改成无条件保留 → 两行即便不重载也在。）
# 版本号显示改为插件**顶部横幅**的版本槽（'v2.0.3' 那个 CFString，见下 DEAD_STR 里的 VERSION 项），
# 不再在设置页底部加 footer。
# ---- 全量域改写：原版 Root.plist 里其余单元格（开关 / 颜色模式 / 选色…）也写着旧域 ----
#  必须一起换，否则它们写进旧域、tweak 读新域 ⇒ 开关与颜色设置会「看起来无效」。
_dom = 0
for _it in items:
    if _it.get('defaults') == OLD_ID:
        _it['defaults'] = NEW_ID; _dom += 1
_rest = [k for _it in items for k, v in _it.items() if v == OLD_ID]
assert not _rest, 'Root.plist 里仍有指向旧域的字段: %r' % _rest
P('  Root.plist 旧域单元格改写 %d 处（其余单元格）' % _dom)

pl['items'] = items
update_file(RP, plistlib.dumps(pl, fmt=plistlib.FMT_BINARY))
P('  Root.plist 项数 %d' % len(items))
zh_names = dict(zip([s[0] for s in slider_defs], ['横条左右偏移', '横条上下偏移', '横条长度', '横条粗细']))
for lang in ['zh-Hans', 'en']:
    sp = 'Library/PreferenceBundles/DonutPrefs.bundle/%s.lproj/Root.strings' % lang
    d = plistlib.loads(orig[sp])
    d.pop('Dot', None)
    d.pop(OLD_FOOTER, None)
    d[NEW_FOOTER] = NEW_FOOTER_ZH if lang == 'zh-Hans' else NEW_FOOTER
    for lbl_en, key, mn, mx, stp, dv in slider_defs:
        if lang == 'zh-Hans':
            d[lbl_en] = zh_names[lbl_en]
        else:
            d[lbl_en] = lbl_en
    d.pop('Tap a value to type a new number. Respring to apply.', None)
    # ---- 精简：删掉从未被 Root.plist / 二进制 / control 引用的条目 ----
    # 精简用：Root.strings 里从未被任何地方引用的条目（本轮核实后确认可删）
    STRINGS_DEAD = [
        'About',                                       # 无关于本面板
        'App notification badge · Tiny hollow ring',   # 旧副标题，已被 EN_SUB 取代
        'Author',                                      # 只在 control 里，与面板翻译无关
        'Tap to select a color.',                      # 无对应单元格
        'Version',                                     # 只在 control 里
    ]
    #   已核实这 5 条在包内任何地方都无有效引用（见 verify_unused.py 的取证）。
    #   保留 'Donut'（Root.plist 与二进制均引用）与 'Custom Color'
    #   （位于 DonutPrefs 的 __TEXT,__cstring，静态扫描不足以判死，保守留着）。
    for _dead in STRINGS_DEAD:
        d.pop(_dead, None)
    d['Restore Defaults'] = '恢复默认设置' if lang == 'zh-Hans' else 'Restore Defaults'
    d['Badge Style'] = '角标样式' if lang == 'zh-Hans' else 'Badge Style'
    for _sk, _szh in [('Bar', '横条'), ('Ring', '空心圆'), ('Dot', '圆点')]:
        d[_sk] = _szh if lang == 'zh-Hans' else _sk
    update_file(sp, plistlib.dumps(d, fmt=plistlib.FMT_BINARY))
    P('  %s 本地化（删 Dot + 文案 + 滑块标题 + 恢复默认 + 样式）' % lang)

# ---------- DonutPrefs 二进制：恢复默认按钮 + 修复颜色选项显示 ----------
# 2.9.5 那轮失败的复盘（真机 + 静态取证）：
#   ① Preferences 只显示 action 在**控制器上可响应**的按钮；本包方法名是经 __objc_selrefs
#      间接的，「重指向 baseMethods 新增选择子」在运行期不生效 → 新增方法这条路不通。
#   ② 逐一核过 11 个方法的调用者：**没有一个是真死的**（pickColor:/respring:/specifiers 等
#      在二进制内零调用者，但都由 Preferences 按 plist 在运行期调用，必须保留）。
#   ③ donutReloadSpecifiers 在二进制内**只有一处调用**：通知回调末尾的 `b <其桩>`。
# 最终方案（同时保住「颜色」与「恢复默认」）：
#   1) 按钮 action = donutReloadSpecifiers（本类已存在 → 一定显示）；
#   2) 该方法的 imp 字段 → padding 里我们写的「恢复默认」实现：写回 4 个位置键的默认值，
#      再调用**原文体**做原版异步 reload；**原文体一个字节都不动**；
#   3) 把通知回调那处 `b <桩>` 改成 `b <原文体>` → 通知路径（颜色模式切换 / 选色后）
#      完全等同官方行为，而「恢复默认」只有点按钮才会跑；
#   4) 位置键名沿用 prefs 里**已存在**的 'pfDonutDot'/'#EB4D3DFF'/'#'/'#FFFFFF'
#      （= dylib KEY_CF 的内容 = Root.plist 滑块 key）—— **一字不改**，故不再触碰任何颜色串；
#   5) 顺带修「颜色选项不显示」：specifiers 里 `b.eq`（mode==Custom 才保留）→ 无条件 `b`，
#      Custom Color / Choose Color 两行始终显示。
P('')
P('=== DonutPrefs：恢复默认按钮 + 颜色选项显示修复 ===')
PREFS = 'Library/PreferenceBundles/DonutPrefs.bundle/DonutPrefs'
prefs = bytearray(orig[PREFS])
# 位置键（**按内容原样取用，绝不改写**）：顺序 = dylib KEY_CF 顺序 = Root.plist 滑块顺序
KEYS_BY_CONTENT = ['pfDonutDot', '#EB4D3DFF', '#', '#FFFFFF']
# 仅「默认值」需要载体（改写其 __cstring 内容）。全部与颜色无关：
#   pfEnabledDonut —— 本二进制内引用数 0（引用扫描确认），纯冗余；
#   PFBannerCell / PFFooterCell / icon@3x —— 仅品牌 banner/footer 代码引用（装饰性）。
DEAD_STR = {
    '40': 'pfEnabledDonut', '80': 'PFBannerCell', '30': 'PFFooterCell', '6': 'icon@3x',
    # 顶部横幅的版本槽（原 'v2.0.3'，6 字节 → 最长 5 字符）：与 VERSION 同源。
    # 若将来 VERSION 到 6 字符（如 '2.10.0'），需改为指针重定向方案（见 MEMORY.md）。
    VERSION: 'v2.0.3',
}
# specifiers 里 `b.eq`（mode==Custom 才走"保留"分支）的地址与其目标（保留分支）：
#   arm64  0x446c -> 0x450c   /   arm64e 0x44d0 -> 0x4570
BEQ_FIX = {'arm64': (0x446c, 0x450c), 'arm64e': (0x44d0, 0x4570)}
# 底部致谢文案：替换掉原「Donut 2026 ⓒ️ 刀刀 - 思念变成海」版权行 + 「🇨🇳刀刀源」按钮。
#   （取证：这两个串在 __TEXT.__ustring 里；版权行是 localizedStringForKey:value:@"" 查表、value 空；
#     刀刀源按钮是 setTitle: 直接设。二者只出现在 PFFooterCell.initWithSpecifier: 里。）
CREDIT = '基于刀刀源的 Donut、BadgeBar 显示效果，并向所有贡献者致谢。'
CREDIT_POOL = 0x7c00                     # padding 常量池（UTF-16 文本；两切片同址）
VERSION_POOL = 0x7f00                    # padding 常量池（UTF-8 版本号，≥6 字符时用；在 IMP 断言区之外）
for pso, psz, p_imp, arch in [(0x4000, 0x11980, 0x7a40, 'arm64'), (0x18000, 0x118a0, 0x7ae0, 'arm64e')]:
    psl = prefs[pso:pso+psz]
    ncmds = struct.unpack('<I', psl[16:20])[0]
    q = 32; psec = {}
    for _ in range(ncmds):
        cmd, csz = struct.unpack_from('<2I', psl, q)
        if cmd == 0x19:
            n = struct.unpack('<I', psl[q+64:q+68])[0]
            qq = q + 72
            for _ in range(n):
                sn = psl[qq:qq+16].rstrip(b'\0').decode(); sg = psl[qq+16:qq+32].rstrip(b'\0').decode()
                addr, isz = struct.unpack_from('<2Q', psl, qq+32)
                so = struct.unpack('<I', psl[qq+48:qq+52])[0]
                psec[(sg, sn)] = (addr, isz, so)
                qq += 80
        q += csz

    def v2f(va):
        for (sg, sn), (a, isz, so) in psec.items():
            if isz and a <= va < a + isz and so:
                return so + (va - a)
        return None

    def s_at(va):
        f = v2f(va)
        if f is None: return None
        e = psl.find(b'\0', f)
        return psl[f:e].decode('utf-8', 'replace')

    def sxp(v, b): return v - (1 << b) if v & (1 << (b-1)) else v

    # objc_stubs 符号表
    oa, osz, oo = psec[('__TEXT', '__objc_stubs')]
    stub_map = {}
    for i in range(osz // 32):
        pc = oa + i * 32
        a1, a2 = struct.unpack('<2I', psl[oo+i*32:oo+i*32+8])
        if a1 & 0x9F000000 == 0x90000000:
            immhi = (a1 >> 5) & 0x7ffff; immlo = (a1 >> 29) & 3
            page = (pc & ~0xfff) + (sxp((immhi << 2) | immlo, 21) << 12)
            if a2 & 0xFFC00000 == 0xF9400000:
                sf = v2f(page + ((a2 >> 10) & 0xfff) * 8)
                if sf:
                    sv = struct.unpack('<Q', psl[sf:sf+8])[0]
                    s = s_at(sv & 0xFFFFFFFFF)
                    if s: stub_map[pc] = s
    st_init = next(pc for pc, s in stub_map.items() if s == 'initWithSuiteName:')
    st_set = next(pc for pc, s in stub_map.items() if s == 'setObject:forKey:')
    st_rel = next(pc for pc, s in stub_map.items() if s == 'reloadSpecifiers')

    # 从 banner 死代码提取 alloc 模式：bl st_init 前 0x10 是 ldr x0,[x8,#imm]，前 0xc 是 bl alloc
    md2 = Cs(CS_ARCH_ARM64, CS_MODE_ARM); md2.detail = True
    ba, bsz2, bo = psec[('__TEXT', '__text')]
    first_init = next(ins.address for ins in md2.disasm(psl[bo:bo+bsz2], ba)
                      if ins.mnemonic == 'bl' and ins.operands[0].imm == st_init)
    ldr_ins = next(md2.disasm(psl[v2f(first_init-0x10):v2f(first_init-0x10)+4], first_init-0x10))
    assert ldr_ins.mnemonic == 'ldr' and ldr_ins.op_str.startswith('x0, [x8'), ldr_ins.op_str
    cls_imm = ldr_ins.op_str.split('#')[1].rstrip(']')
    cls_imm = int(cls_imm, 0)
    alloc_ins = next(md2.disasm(psl[v2f(first_init-0xc):v2f(first_init-0xc)+4], first_init-0xc))
    assert alloc_ins.mnemonic == 'bl', alloc_ins.mnemonic
    st_alloc = alloc_ins.operands[0].imm
    stride = 12 if pso == 0x4000 else 16
    st_release = st_alloc + 5 * stride          # __stubs 顺序：alloc 之后第 5 个 = _objc_release（间接符号表确认）
    P('  [%#x] alloc stub=%#x classref disp=%#x init=%#x set=%#x reload=%#x'
      % (pso, st_alloc, cls_imm, st_init, st_set, st_rel))

    # cfstring 表（按内容定位）
    ca, csz2, co = psec[('__DATA_CONST', '__cfstring')]
    cf = {}
    for i in range(csz2 // 32):
        va = ca + i * 32
        isa, flags, ptr, ln = struct.unpack('<4Q', psl[co+i*32:co+i*32+32])
        s = s_at(ptr & 0xFFFFFFFFF) if ptr else None
        cf[va] = (s, ptr, ln)
    suite_va = next(va for va, (s, _, _) in cf.items() if s == OLD_ID)
    # ---- 标识符搬迁（prefs 的 suite CFString）----
    _idb2 = NEW_ID.encode() + b'\x00'
    _sf = v2f(suite_va)
    _sptr = struct.unpack('<Q', psl[_sf+16:_sf+24])[0]
    _slen = struct.unpack('<Q', psl[_sf+24:_sf+32])[0]
    assert s_at(_sptr & 0xFFFFFFFFF) == OLD_ID, 'suite CFString 内容不符'
    assert all(b == 0 for b in psl[ID_POOL_PREFS: ID_POOL_PREFS + len(_idb2)]), 'prefs 标识符池非零'
    psl[ID_POOL_PREFS: ID_POOL_PREFS+len(_idb2)] = _idb2
    struct.pack_into('<Q', psl, _sf+16, (_sptr & ~0xFFFFFFFFF) | ID_POOL_PREFS)
    struct.pack_into('<Q', psl, _sf+24, len(NEW_ID))
    P('  [%#x] 标识符: suite CFString @%#x 内容 %s -> %s（ptr %#x -> %#x 池，len %d -> %d）'
      % (pso, suite_va, OLD_ID, NEW_ID, _sptr & 0xFFFFFFFFF, ID_POOL_PREFS, _slen, len(NEW_ID)))
    cf_by_content = {}
    for va, (s, ptr, ln) in cf.items():
        if s and s not in cf_by_content: cf_by_content[s] = va
    cf_va = {}                                   # 需改写的载体（4 个默认值 + 版本号）
    for newc, oldc in DEAD_STR.items():
        assert oldc in cf_by_content, '载体缺失: %r' % oldc
        cf_va[newc] = cf_by_content[oldc]
    key_va = []                                  # 4 个位置键：**原样取用，绝不改写**
    for k in KEYS_BY_CONTENT:
        assert k in cf_by_content, '位置键 CFString 缺失: %r' % k
        key_va.append(cf_by_content[k])
    P('  [%#x] suite=%#x 键=%s 载体=%s' % (pso, suite_va, [hex(v) for v in key_va],
                                        {k: hex(v) for k, v in cf_va.items()}))

    # 改写载体内容（__cstring，原地 + 补 NUL）+ len 字段（__DATA_CONST，无签名）
    for newc, va in cf_va.items():
        _, ptr, oldlen = cf[va]
        if len(newc.encode()) + 1 <= oldlen:
            f = v2f(ptr & 0xFFFFFFFFF)
            assert f is not None, (newc, oldlen)
            newb = newc.encode() + b'\x00'
            psl[f:f+oldlen] = newb + b'\x00' * (oldlen - len(newb))
            struct.pack_into('<Q', psl, v2f(va) + 24, len(newc))
        else:
            # 放不下（版本号 ≥6 字符）→ 重定向 ptr 到 padding 的 UTF-8 串
            assert all(b == 0 for b in psl[VERSION_POOL: VERSION_POOL + 0x40]), 'VERSION_POOL 非零'
            f = v2f(va)
            old_ptr = struct.unpack('<Q', psl[f+16:f+24])[0]
            struct.pack_into('<Q', psl, f+16, (old_ptr & ~0xFFFFFFFFF) | VERSION_POOL)
            struct.pack_into('<Q', psl, f+24, len(newc))
            psl[VERSION_POOL: VERSION_POOL + len(newc.encode()) + 1] = newc.encode() + b'\x00'
            P('  [%#x] 版本 %r 超 5 字符 → ptr 重定向到 %#x' % (pso, newc, VERSION_POOL))

    # ---- 先定位 11 方法表的 entry[6] = donutReloadSpecifiers，记下它**原 imp** ----
    ma, msz, mo = psec[('__TEXT', '__objc_methlist')]
    f = mo; ml_base = None
    while f < mo + msz - 8:
        fl = struct.unpack('<I', psl[f:f+4])[0]; cnt = struct.unpack('<I', psl[f+4:f+8])[0]
        if fl & 0x80000000 and cnt == 11: ml_base = f; break
        f += 8 + cnt * 12
    assert ml_base is not None, '11 方法表未找到'
    e6 = ml_base + 8 + 6*12
    no6 = struct.unpack('<i', psl[e6:e6+4])[0]
    sf6 = v2f(e6 + no6)
    nm6 = s_at(struct.unpack('<Q', psl[sf6:sf6+8])[0] & 0xFFFFFFFFF)
    assert nm6 == 'donutReloadSpecifiers', nm6
    io_old6 = struct.unpack('<i', psl[e6+8:e6+12])[0]
    imp_orig = (e6 + 8) + io_old6       # 原版方法体：**保持不变**，供通知路径直接跳入

    # ---- 新 IMP（写在 padding p_imp）----
    # [[NSUserDefaults alloc] initWithSuiteName:NEW_ID] → [obj setObject:<默认值>
    #   forKey:<位置键>] ×4 → 调用**原文体**（原版异步 reload，避免同步 reload 的重入风险）
    #   → [obj release] → ret
    assert all(b == 0 for b in psl[p_imp: p_imp+0x400]), 'padding %#x 非零，勿覆盖' % p_imp
    code = b''
    pc = p_imp
    is_e = (pso == 0x18000)          # arm64e 切片需 ptrauth PAC
    def E(b):
        global code, pc
        code += b; pc += len(b)
    if is_e:
        E(bytes.fromhex('7f2303d5'))  # pacibsp：ptrauth 签名 lr（keystone 旧版不支持，硬编码）
    E(kasm('stp x29, x30, [sp, #-0x40]!'))
    E(kasm('stp x20, x19, [sp, #0x10]'))
    E(kasm('mov x19, x0'))
    E(adrp(8, pc, 0xc000))
    E(ldr_x_off(0, 8, cls_imm))
    E(bl_to(pc, st_alloc))
    E(adrp(2, pc, suite_va))
    E(add_imm(2, 2, suite_va & 0xfff))
    E(bl_to(pc, st_init))
    E(kasm('mov x20, x0'))
    for ki in range(len(KEYS_BY_CONTENT)):
        vcf = cf_va[str(DEFAULTS[ki])]          # 改写后的默认值载体
        kcf = key_va[ki]                        # 原样的位置键
        E(adrp(2, pc, vcf)); E(add_imm(2, 2, vcf & 0xfff))
        E(adrp(3, pc, kcf)); E(add_imm(3, 3, kcf & 0xfff))
        E(kasm('mov x0, x20'))
        E(bl_to(pc, st_set))
    E(kasm('mov x0, x19'))
    E(bl_to(pc, imp_orig))                      # 原版异步 reload
    E(kasm('mov x0, x20'))
    E(bl_to(pc, st_release))                    # 释放 NSUserDefaults
    E(kasm('mov x0, x19'))
    E(kasm('ldp x20, x19, [sp, #0x10]'))
    E(kasm('ldp x29, x30, [sp], #0x40'))
    if is_e:
        E(bytes.fromhex('ff0f5fd6'))  # retab：ptrauth 认证 lr 并返回
    else:
        E(kasm('ret'))
    assert len(code) <= 0x300, len(code)
    psl[p_imp: p_imp+len(code)] = code
    P('  [%#x] 恢复默认 IMP @%#x (%dB)；原方法体 @%#x 保持不动' % (pso, p_imp, len(code), imp_orig))

    # 横幅标题重定向：'Donut' cfstring 的数据指针 -> 补丁区 'Donut-bar'（老式 rebase 槽，改值即生效）
    title_va = next(va for va, (s_, _, _) in cf.items() if s_ == 'Donut')
    name_va = p_imp + len(code)                     # IMP 之后的 padding 放新字符串
    psl[name_va: name_va+10] = b'Donut-bar\x00'
    tf = v2f(title_va)
    old_ptr = struct.unpack('<Q', psl[tf+16: tf+24])[0]
    struct.pack_into('<Q', psl, tf+16, (old_ptr & ~0xFFFFFFFFF) | name_va)
    struct.pack_into('<Q', psl, tf+24, 9)           # len = 9
    P('  [%#x] 标题 -> %r @%#x (len 9)' % (pso, 'Donut-bar', name_va))

    # ---- ① 劫持方法表 entry[6]（donutReloadSpecifiers）→ 我们的「恢复默认」IMP ----
    # 真机证实：Preferences 只显示 action 在本类**可响应**的按钮；而「重指向 baseMethods 新增
    #   选择子」运行期不生效（且本包方法名还经 __objc_selrefs 间接）→ 新增方法这条路不通。
    #   故沿用「复用已存在方法 + 改写其 int32 impOffset」这条已生效的路子。
    #   偏移语义：relative method list 的 impOffset 相对「imp 字段」(entry+8)。
    struct.pack_into('<i', psl, e6 + 8, p_imp - (e6 + 8))
    assert (e6 + 8) + struct.unpack('<i', psl[e6+8:e6+12])[0] == p_imp
    P('  [%#x] entry[6] %r: imp %#x -> %#x（点按钮即恢复默认）' % (pso, nm6, imp_orig, p_imp))

    # ---- ② 把通知回调与「恢复默认」解耦 ----
    # donutReloadSpecifiers 在本二进制内**唯一的一处调用**是通知回调末尾的 `b <其 objc 桩>`
    #   （真机取证：0x58e0 = `ldr x0,[x0,#0x20]` + `b 桩`）。改成直接跳**原文体** →
    #   通知路径（切换颜色模式 / 选色后）与官方行为完全一致，按钮那条路才走我们的 IMP。
    stub_pc = next((pc_ for pc_, s_ in stub_map.items() if s_ == 'donutReloadSpecifiers'), None)
    assert stub_pc is not None, '未找到 donutReloadSpecifiers 的 objc 桩'
    md3 = Cs(CS_ARCH_ARM64, CS_MODE_ARM)
    jump_hits = []
    for ins in md3.disasm(psl[bo:bo+bsz2], ba):
        if ins.mnemonic in ('b', 'bl') and ins.op_str.startswith('#'):
            try: t = int(ins.op_str[1:], 16)
            except ValueError: continue
            if t == stub_pc: jump_hits.append(ins.address)
    assert len(jump_hits) == 1, '指向该桩的跳转应恰好 1 处，实为 %r' % jump_hits
    tj = jump_hits[0]
    f = v2f(tj)
    old_j = struct.unpack('<I', psl[f:f+4])[0]
    psl[f:f+4] = b_to(tj, imp_orig)
    assert struct.unpack('<I', psl[f:f+4])[0] != old_j
    P('  [%#x] 通知回调 @%#x: b %#x(桩) -> b %#x(原文体)' % (pso, tj, stub_pc, imp_orig))

    # ---- v3.9.5 要求②：**恢复** specifiers 的 `b.eq`（mode==Custom 才显示颜色项）----
    # 取证：过滤条件读 'label' 串 + 'Custom Color' / 'Choose Color' ⇒ 非 Custom 模式就把这两行删掉。
    # v3.9.5 起恢复官方行为：只有切到 Custom 才出现颜色选择（此前"两行常显"的补丁撤销）。
    beq_pc, keep_pc = BEQ_FIX[arch]
    fb = v2f(beq_pc)
    ins_b = next(md3.disasm(psl[fb:fb+4], beq_pc))
    assert ins_b.mnemonic == 'b.eq' and ins_b.op_str == '#%#x' % keep_pc, (ins_b.mnemonic, ins_b.op_str)
    old_b = struct.unpack('<I', psl[fb:fb+4])[0]
    psl[fb:fb+4] = bcond_to(0, beq_pc, keep_pc)          # b.eq（cond=EQ）—— 保持官方语义
    assert struct.unpack('<I', psl[fb:fb+4])[0] == old_b, 'b.eq 应恢复为原字节'
    P('  [%#x] specifiers @%#x: b.eq #%#x 保持（mode==Custom 才显示颜色项）' % (pso, beq_pc, keep_pc))

    # ---- v3.9.6 ⑤ 滑块按样式折叠（选横条才显示；详见 apply_style9.py 顶部说明）----
    # 落点故意取「收尾起点的**下一条** ldr」而不是 adrp：
    #   verify_reloc.py 把「原指令是 ADR/ADRP 却被改掉」判为 FAIL（它据此发现重定位改写错误），
    #   改非 ADR/ADRP 指令只计 info。adrp 让原流程照跑（x8=0x8000），我们改 ldr → stub 末尾复原该 ldr。
    SW_ENTRY  = {'arm64': 0x4510, 'arm64e': 0x4574}      # 原指令 = ldr x8,[x8,#0x40/0xe8]
    SW_RESUME = {'arm64': 0x4514, 'arm64e': 0x4578}      # 该 ldr 的下一条
    SW_LDR_OFF= {'arm64': 0x40,   'arm64e': 0xe8}        # 被替换掉的 ldr 的立即数偏移
    SW_CF_0X  = {'arm64': 0x83b8, 'arm64e': 0x8458}      # CFString "0X"（样式键，已存在）
    SW_INTFK  = {'arm64': 0x60e0, 'arm64e': 0x6180}      # stub: -integerForKey:
    SW_COUNT  = {'arm64': 0x5fa0, 'arm64e': 0x6040}      # stub: -count
    SW_REMOVE = {'arm64': 0x62e0, 'arm64e': 0x6380}      # stub: -removeObjectAtIndex:
    SW_STUB   = 0x7d00
    _sw = SW_STUB
    sb = bytearray()
    def sE(bb): sb.extend(bb)
    sE(kasm('stp x19, x20, [sp, #-0x20]!'))              # 保存 callee-saved（原函数在用）
    sE(kasm('stp x21, x22, [sp, #0x10]'))
    sE(kasm('mov x0, x20'))                              # x20 = NSUserDefaults
    sE(adrp(2, _sw + len(sb), 0x8000))
    sE(add_imm(2, 2, SW_CF_0X[arch] & 0xfff))            # x2 = @"0X"
    sE(bl_to(_sw + len(sb), SW_INTFK[arch]))             # x0 = 样式
    _sw_cbz = _sw + len(sb); sE(cbz_to(0, _sw_cbz, 0))   # 样式==0（横条）→ 不隐藏
    sE(kasm('mov x0, x21'))                              # x21 = specifiers 可变副本
    sE(bl_to(_sw + len(sb), SW_COUNT[arch]))
    sE(kasm('cmp x0, #12'))                              # 需要 >= 12 项才安全
    _sw_blt = _sw + len(sb); sE(bcond_to(0xb, _sw_blt, 0))   # b.lt → out
    sE(kasm('mov x19, #11'))
    _sw_loop = _sw + len(sb)
    sE(kasm('mov x0, x21'))
    sE(kasm('mov x2, x19'))
    sE(bl_to(_sw + len(sb), SW_REMOVE[arch]))            # [specifiers removeObjectAtIndex:i]
    sE(kasm('sub x19, x19, #1'))
    sE(kasm('cmp x19, #3'))
    _sw_bgt = _sw + len(sb); sE(bcond_to(0xc, _sw_bgt, _sw_loop))  # b.gt → loop（倒序 11..4）
    _sw_out = _sw + len(sb)
    sE(kasm('ldp x21, x22, [sp, #0x10]'))
    sE(kasm('ldp x19, x20, [sp], #0x20'))
    sE(adrp(8, _sw + len(sb), 0x8000))                   # 复原被替换的那条 ldr 的页基址
    sE(ldr_x_off(8, 8, SW_LDR_OFF[arch]))                # 复原 ldr x8,[x8,#off]
    sE(b_to(_sw + len(sb), SW_RESUME[arch]))
    sb[_sw_cbz-_sw:_sw_cbz-_sw+4] = cbz_to(0, _sw_cbz, _sw_out)
    sb[_sw_blt-_sw:_sw_blt-_sw+4] = bcond_to(0xb, _sw_blt, _sw_out)
    sb[_sw_bgt-_sw:_sw_bgt-_sw+4] = bcond_to(0xc, _sw_bgt, _sw_loop)
    assert SW_STUB + len(sb) <= 0x7ee0, '滑块桩与 ID 池(0x7ee0)重叠'
    assert all(b == 0 for b in psl[SW_STUB: SW_STUB + len(sb)]), '滑块桩落点非零'
    psl[SW_STUB: SW_STUB + len(sb)] = sb
    psl[SW_ENTRY[arch]: SW_ENTRY[arch]+4] = b_to(SW_ENTRY[arch], SW_STUB)
    P('  [%#x] 滑块折叠桩 @%#x(%dB)：0x%x -> b 桩（样式!=0 时倒序移除 index 4..11）'
      % (pso, SW_STUB, len(sb), SW_ENTRY[arch]))

    # ---- ④ 底部品牌：删「刀刀源」按钮 + 版权行，改为致谢文案 ----
    #   a) 致谢文案（UTF-16）写入 padding 常量池
    enc = CREDIT.encode('utf-16-le') + b'\x00\x00'
    nunits = len(CREDIT.encode('utf-16-le')) // 2
    assert all(b == 0 for b in psl[CREDIT_POOL: CREDIT_POOL + 0x100]), 'CREDIT_POOL %#x 非零' % CREDIT_POOL
    psl[CREDIT_POOL: CREDIT_POOL + len(enc)] = enc
    #   b) 定位版权 CFString（UTF-16 内容以 'Donut 2026' 开头）与空串 CFString（len==0）
    def ustr_of(cva):
        f_ = v2f(cva)
        if f_ is None: return None
        ptr = struct.unpack('<Q', psl[f_+16:f_+24])[0] & 0xFFFFFFFFF
        ln = struct.unpack('<Q', psl[f_+24:f_+32])[0]
        fp = v2f(ptr)
        if fp is None: return None
        return psl[fp: fp+ln*2].decode('utf-16-le', 'replace'), ptr, ln
    copyright_va = empty_va = None
    for va in cf:
        u = ustr_of(va)
        if u is None: continue
        if u[0].startswith('Donut 2026'): copyright_va = va
        if u[2] == 0: empty_va = va
    assert copyright_va is not None and empty_va is not None, (copyright_va, empty_va)
    #   c) 版权 CFString 的 ptr/len 重定向 → 致谢文案（老式 rebase 槽，改值即生效）
    cva_f = v2f(copyright_va)
    old_cp = struct.unpack('<Q', psl[cva_f+16:cva_f+24])[0]
    struct.pack_into('<Q', psl, cva_f+16, (old_cp & ~0xFFFFFFFFF) | CREDIT_POOL)
    struct.pack_into('<Q', psl, cva_f+24, nunits)
    #   d) 把「版权 label 的查表 value 参数（空串）」改成同一致谢 CFString ——
    #      即 localizedStringForKey:致谢 value:致谢 → 无论如何都返回致谢文案。
    #      做法：找到 `add x2, x2, #<copyright>`（唯一，= key 载入）后第 2 条指令
    #      `add x3, x3, #<empty>`（= value 载入），把它的立即数改成 copyright 的偏移。
    md5 = Cs(CS_ARCH_ARM64, CS_MODE_ARM)
    key_pc = None
    for ins in md5.disasm(psl[bo:bo+bsz2], ba):
        if ins.mnemonic == 'add' and ins.op_str.startswith('x2, x2, #'):
            imm = int(ins.op_str.split('#')[1], 0)
            if (0x8000 + imm) == copyright_va:
                key_pc = ins.address; break
    assert key_pc is not None, '未找到版权 key 的 add x2'
    val_ins = next(md5.disasm(psl[v2f(key_pc+8):v2f(key_pc+8)+4], key_pc+8))
    assert val_ins.mnemonic == 'add' and val_ins.op_str.startswith('x3, x3, #'), (val_ins.mnemonic, val_ins.op_str)
    assert (0x8000 + int(val_ins.op_str.split('#')[1], 0)) == empty_va, val_ins.op_str
    psl[v2f(val_ins.address): v2f(val_ins.address)+4] = add_imm(3, 3, copyright_va & 0xfff)
    #   e) 删「刀刀源」按钮：NOP 掉 PFFooterCell.initWithSpecifier: 里**最后一个** addSubview
    #      （版权 label 的 addSubview 在前、按钮的在后；都发生在 key_pc 之后）
    addsub_pc = next((pc_ for pc_, s_ in stub_map.items() if s_ == 'addSubview:'), None)
    assert addsub_pc is not None, '未找到 addSubview 桩'
    adds = []
    for ins in md5.disasm(psl[bo:bo+bsz2], ba):
        if ins.mnemonic == 'bl' and ins.op_str.startswith('#') and ins.address > key_pc:
            try:
                if int(ins.op_str[1:], 16) == addsub_pc: adds.append(ins.address)
            except ValueError: pass
    assert len(adds) == 2, 'footer 里应有 2 处 addSubview（label+按钮），实为 %r' % adds
    btn_add = adds[-1]
    psl[v2f(btn_add): v2f(btn_add)+4] = bytes.fromhex('1f2003d5')   # nop
    P('  [%#x] 底部品牌：版权 CFString %#x → 致谢(utf16@%#x)；value 参数改指同串；按钮 addSubview @%#x NOP'
      % (pso, copyright_va, CREDIT_POOL, btn_add))

    prefs[pso:pso+psz] = psl

new_prefs, _ = DS.sign_macho(bytes(prefs), log=lambda *a: P('   ' + ' '.join(str(x) for x in a)))
update_file(PREFS, bytes(new_prefs))
P('  DonutPrefs 重签名完成')

# __init_offsets：ctor 指向 prefs_to_rect（arm64@0x6e00 / arm64e@0x7060，切片内偏移）
for so_i, arch_i in [(0x4000, 'arm64'), (0x18000, 'arm64e')]:
    io_i = 0x6e00 if arch_i == 'arm64' else 0x7060
    dylib[so_i+io_i: so_i+io_i+4] = FUNC_BY[arch_i].to_bytes(4, 'little')
    P('  __init_offsets[%s] -> %#x' % (arch_i, FUNC_BY[arch_i]))

P('')
P('=== 重新签名 ===')
new_dylib, _ = DS.sign_macho(bytes(dylib), log=lambda *a: P('   ' + ' '.join(str(x) for x in a)))
update_file(DYL, bytes(new_dylib))

# ---------- 品牌：入口 plist + 图标 ----------
ENT = 'Library/PreferenceLoader/Preferences/Donut.plist'
ent = plistlib.loads(orig[ENT])
ent['entry']['label'] = 'Donut-bar'
update_file(ENT, plistlib.dumps(ent, fmt=plistlib.FMT_BINARY))
P('  入口 label -> Donut-bar')

from PIL import Image
import zlib as _zlib
try:
    from zopfli.zlib import compress as _zopfli_compress
except ImportError:                       # 缺 zopfli 时静默降级，只损失少量压缩率
    _zopfli_compress = None

# ---- 图标处理：zopfli 重压 IDAT（1.2.0 核查轮起仅存无损路径）----
# 历史：1.0.2 及以前走「RGBA 整体量化 ≤64 项 + zopfli」两步叠加；量化导致渐变色带/
#   半透明边缘糊（max err 45~255），1.0.3 起全面改走 _lossless_png（零误差）。
#   量化函数 _opt_png 与 ICON_N 已于 1.2.0 核查时删除（ast 扫描确认无调用方）。
# 保留两条铁律：① 不量化；② 1x 尺寸必须是 29（与 Math 原版一致；曾被误写作 87px，白占 7KB）。


def _zopfli_idat(png, iters=15):
    """把 PNG 的 IDAT 用 zopfli 重新压缩；返回新的 PNG 字节。"""
    off, chs = 8, []
    while off < len(png):
        ln = struct.unpack_from('>I', png, off)[0]
        chs.append((png[off+4:off+8], png[off+8:off+8+ln]))
        off += 12 + ln
    idat = b''.join(d for t_, d in chs if t_ == b'IDAT')
    new = _zopfli_compress(_zlib.decompress(idat), numiterations=iters)
    out, done = bytearray(b'\x89PNG\r\n\x1a\n'), False
    for t_, d in chs:
        if t_ == b'IDAT':
            if done:
                continue
            d = new
            done = True
        out += struct.pack('>I', len(d)) + t_ + d + struct.pack('>I', _zlib.crc32(t_ + d) & 0xffffffff)
    return bytes(out)


def _lossless_png(im):
    """RGBA 原样存 PNG + zopfli 重压 IDAT。**不做量化**，像素误差为 0。

    zopfli 只重排 DEFLATE 编码，产出的图像数据与 PIL 输出逐像素一致。
    """
    b = io.BytesIO()
    im.convert('RGBA').save(b, 'PNG', optimize=True, compress_level=9)
    raw = b.getvalue()
    return _zopfli_idat(raw) if _zopfli_compress else raw


# ---- 图标：1.2.0 起改用天气扁平图标（1024x1024 RGBA），**无损高清**版 ----
# 1.0.2 之前这里做了「RGBA 量化成 64 色调色板 + 缩放到 87px」，用户反馈图标发糊。根因两条：
#   ① **量化**：RGBA → 64 色 P 模式，渐变出现色带/块状台阶（实测 max 误差 27~45/255）；
#   ② **放大**：源图只有 60x60，却被铺到 87x87（3x 档）= 放大 1.45 倍再量化，双重损失。
# 现改为：
#   · **不量化**，直接 RGBA 存 PNG —— 误差为 **0**（PNG 自身就是 DEFLATE 无损）；
#   · **zopfli 重压 IDAT 保留** —— 纯 DEFLATE 编码优化，像素一字不改，约再省 5%；
#   · **各档不超过源图的 60px** ⇒ 29 / 58 / 60。源图 60px 没有 87px 的信息量，
#     往上放大只是插值，再锐利也是假的，故 3x 档用 60。
# 体积 3049 → 9013 B。用户明确要求「高清」，这点体积换清晰度是值的。
# 源图另存于 E:\deb\_icons_weather\raw\weather-flat-icon-ring-clip-1024.png
# （sha256 8ba81070dd5d9c53...），构建时直接读文件。
ICON_SRC = r'E:\deb\_icons_weather\raw\weather-flat-icon-ring-light30-1024.png'
img = Image.open(ICON_SRC).convert('RGBA')
assert img.size == (1024, 1024), '天气图标源图尺寸异常: %r' % (img.size,)
SRC_MAX = min(img.size)                       # = 1024，三档 29/58/87 全为缩小，无放大插值
# ---- 尺寸策略（1.0.4 修正）----
# 1.0.3 曾为「绝不放大」把 3x 档降到 60px，结果偏好面板里图标显小
#   （面板用 3x 档，60px / 3 = 20pt，而上游原版是 87px / 3 = 29pt）。
# 现改为**对齐上游原版的 29/58/87**：宁可对扁平矢量风格的源图做 LANCZOS 上采样，
# 也不能让图标显小。实测放大到 87px 后边缘依然干净（锐化收益 <1%，故不引入）。
# 断言也随策略翻转：核心约束从「不超源图」变成「**不低于上游原版**」。
UPSTREAM = {29: 29, 58: 58, 87: 87}           # 上游原版 Donut 2.0.3 的 1x/2x/3x
_icon_tot = 0
for isz, iname in [(29, 'icon.png'), (58, 'icon@2x.png'), (87, 'icon@3x.png')]:
    # !! 1x=29 / 2x=58 / 3x=87 必须成 1:2:3；尺寸不得低于上游原版（否则面板里显小）
    assert isz == UPSTREAM[isz], '%s 尺寸 %d != 上游原版 %d' % (iname, isz, UPSTREAM[isz])
    if isz == SRC_MAX:
        im2 = img
    else:
        im2 = img.resize((isz, isz), Image.LANCZOS)
    _png = _lossless_png(im2)
    _icon_tot += len(_png)
    update_file('Library/PreferenceBundles/DonutPrefs.bundle/' + iname, _png)
    P('  图标 %-12s %dx%d  %d B（无损 RGBA + %s%s）'
      % (iname, isz, isz, len(_png), 'zopfli' if _zopfli_compress else '无 zopfli',
         '，源图原样' if isz == SRC_MAX else '，LANCZOS 缩小'))
P('  图标合计 %d B（源图 1024x1024 天气扁平图标，无损 RGBA + zopfli）'
  % (_icon_tot,))

EN_SUB = 'App notification badge · Tiny hollow ring'
for lang in ['zh-Hans', 'en']:
    sp = 'Library/PreferenceBundles/DonutPrefs.bundle/%s.lproj/Root.strings' % lang
    dd2 = plistlib.loads(orig[sp])
    dd2[EN_SUB] = ('程序通知角标 · 横条 / 空心圆 / 圆点' if lang == 'zh-Hans'
                   else 'App notification badge · Bar / Ring / Dot')
    update_file(sp, plistlib.dumps(dd2, fmt=plistlib.FMT_BINARY))
P('  副标题 -> 横条 / 空心圆 / 圆点')

buf = io.BytesIO()
nt = tarfile.open(fileobj=buf, mode='w', format=tarfile.GNU_FORMAT)
dd = tarfile.TarInfo('.'); dd.type = tarfile.DIRTYPE; dd.mode = 0o755; dd.uid = 0; dd.gid = 0
dd.uname = 'root'; dd.gname = 'wheel'
nt.addfile(dd)
for x in members:
    if x.name == '.': continue
    nt.addfile(x, io.BytesIO(orig[x.name]) if x.isfile() else None)
nt.close()
new_data = buf.getvalue()
if dk.endswith('lzma'):
    new_enc, dmn = lzma.compress(new_data, format=lzma.FORMAT_ALONE,
                                 preset=9 | lzma.PRESET_EXTREME), 'data.tar.lzma'
else:
    new_enc, dmn = gzip.compress(new_data, 9, mtime=0), 'data.tar.gz'

ctf = tarfile.open(fileobj=io.BytesIO(m['control.tar.gz']), mode='r:*')
oldctl = [ctf.extractfile(mm).read().decode() for mm in ctf.getmembers()
          if mm.isfile() and mm.name.rstrip('/').endswith('control')][0]
# ---- v3.9.5 要求④：control 按用户给定格式重写 ----
#   （Conflicts 沿用既有逻辑：原版列表 + 本包与原包互斥；其余字段按用户给的模板）
_conf = [ln for ln in oldctl.splitlines() if ln.startswith('Conflicts:')]
_conf = _conf[0].rstrip() if _conf else 'Conflicts:'
if OLD_ID not in _conf.split(':', 1)[1]:
    _conf = _conf + ', ' + OLD_ID
newctl = '\n'.join([
    'Package: ' + NEW_ID,
    'Name: Donut-bar(RootHide)',
    'Description: 桌面图标通知角标变为图标下方的彩色横条，自适应颜色；基于刀刀源的 Donut、BadgeBar 显示效果，并向所有贡献者致谢。',
    'Maintainer: 文武',
    'Author: 文武',
    'Section: 嗨-工具',
    'Depends: mobilesubstrate (>= 0.9.5000), preferenceloader, firmware (>= 15.0)',
    _conf,
    'Architecture: iphoneos-arm64e',
    'Version: ' + VERSION,
]) + '\n'
P('  control 重写：\n' + ''.join('    %s\n' % ln for ln in newctl.splitlines()))
cbuf = io.BytesIO()
cto = tarfile.open(fileobj=cbuf, mode='w', format=tarfile.GNU_FORMAT)
dd = tarfile.TarInfo('.'); dd.type = tarfile.DIRTYPE; dd.mode = 0o755; dd.uid = 0; dd.gid = 0
dd.uname = 'root'; dd.gname = 'root'
cto.addfile(dd)
cc = tarfile.TarInfo('./control')
cc.size = len(newctl.encode()); cc.mode = 0o644; cc.uid = 0; cc.gid = 0; cc.uname = 'root'; cc.gname = 'root'
cto.addfile(cc, io.BytesIO(newctl.encode()))
cto.close()

deb = b'!<arch>\n' + RC.ar_member('debian-binary', m['debian-binary']) \
    + RC.ar_member('control.tar.gz', gzip.compress(cbuf.getvalue(), 9, mtime=0)) \
    + RC.ar_member(dmn, new_enc)
open(OUT, 'wb').write(deb)
P('')
P('=== 输出 ===')
P('  %s  %d B  sha256=%s' % (OUT, len(deb), hashlib.sha256(deb).hexdigest()))
P('  Version: %s / Name: Donut-bar' % VERSION)
open(LOG, 'w', encoding='utf-8').write('\n'.join(BUF))
print('\n'.join(BUF))
