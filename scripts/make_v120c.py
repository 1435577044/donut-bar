# -*- coding: utf-8 -*-
"""从 patch_donut46.py 派生 patch_donut47.py：删除死代码（1.2.0 核查轮）。

删除项（ast 扫描确认的唯一死代码）：
  - _opt_png()        64 色量化旧路径，1.0.3 起被 _lossless_png 取代，无调用方
  - ICON_N = 64       仅被 _opt_png 默认参数引用
  - 量化时代的注释块  改写为「仅存无损路径」+ 保留两条铁律
不变：VERSION 1.2.0 / OUT / 图标源 light30。预期产物与 patch_donut46 逐字节一致
（sha256 43a749e2...），即纯脚本卫生清理，不影响包内容。
"""
import io, ast

SRC = r'E:\deb\_fix2\patch_donut46.py'
DST = r'E:\deb\_fix2\patch_donut47.py'

s = io.open(SRC, encoding='utf-8').read()


def rep(old, new, why):
    global s
    assert old in s, '锚点未找到: %s' % why
    assert s.count(old) == 1, '锚点不唯一(%d 次): %s' % (s.count(old), why)
    s = s.replace(old, new)
    print('  [rep] %s' % why)


# 1. 注释块 + ICON_N 常量删除/改写
rep(
    "# ---- 图标瘦身：RGBA 四维量化 + zopfli 重压 IDAT ----\n"
    "# 背景：PNG 自身已压缩 ⇒ tar/lzma 对它几乎无效 ⇒ 图标占了 deb 近 19%，是唯一可压的项。\n"
    "# 两步叠加（实测见 apply_style22.py 文档头）：\n"
    "#   ① RGBA **整体**量化成 ≤ICON_N 项（颜色与 alpha 一起算）。旧法「ncol 色 × nal 档 alpha」\n"
    "#      最多 ncol*nal 项，且 alpha 被独立砍档 ⇒ 半透明边缘误差极大（实测 max err 255）；\n"
    "#      整体量化在同一体积下 max err 仅 45。\n"
    "#   ② zopfli 重压 IDAT —— 像素数据一字不改，纯 DEFLATE 编码优化（无损，约再省 5%）。\n"
    "# 另：1x 尺寸必须是 29（与 Math 原版一致；曾被误写作 87px，白占 7KB）。\n"
    "ICON_N = 64\n",
    "# ---- 图标处理：zopfli 重压 IDAT（1.2.0 核查轮起仅存无损路径）----\n"
    "# 历史：1.0.2 及以前走「RGBA 整体量化 ≤64 项 + zopfli」两步叠加；量化导致渐变色带/\n"
    "#   半透明边缘糊（max err 45~255），1.0.3 起全面改走 _lossless_png（零误差）。\n"
    "#   量化函数 _opt_png 与 ICON_N 已于 1.2.0 核查时删除（ast 扫描确认无调用方）。\n"
    "# 保留两条铁律：① 不量化；② 1x 尺寸必须是 29（与 Math 原版一致；曾被误写作 87px，白占 7KB）。\n",
    '量化注释块 + ICON_N')

# 2. _opt_png 函数整体删除（定义 + 与上一函数之间的两个空行）
rep(
    "def _opt_png(im, sz, n=ICON_N):\n"
    "    img = im.resize((sz, sz), Image.LANCZOS)\n"
    "    q = img.quantize(colors=n, method=Image.FASTOCTREE, dither=Image.NONE)\n"
    "    b = io.BytesIO()\n"
    "    q.save(b, 'PNG', optimize=True, compress_level=9)\n"
    "    raw = b.getvalue()\n"
    "    return _zopfli_idat(raw) if _zopfli_compress else raw\n\n\n",
    "",
    '_opt_png 函数')

# 3. LOG 改名（VERSION/OUT/图标源不变）
rep(r"LOG = r'E:\deb\_fix2\patch_log46.txt'",
    r"LOG = r'E:\deb\_fix2\patch_log47.txt'",
    'LOG -> 47')

ast.parse(s)
# 自检：死代码的定义形式确实已不在（注释里允许出现名字）
assert 'def _opt_png' not in s and 'ICON_N =' not in s and 'n=ICON_N' not in s, '死代码未删净'
io.open(DST, 'w', encoding='utf-8').write(s)
print('OK -> %s (%d B)' % (DST, len(s.encode('utf-8'))))
