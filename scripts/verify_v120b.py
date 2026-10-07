# -*- coding: utf-8 -*-
"""1.2.0 版本包验证（图标更换版）。

核心断言：
  ① 版本号已全面改为 1.2.0：control 的 Version、DonutPrefs 两处版本串（未走 ptr 重定向）；
  ② 与 1.1.0 相比，差异恰好 = 3 个图标 + DonutPrefs（版本串+CDHash），无其他文件差异；
  ③ 图标三档 29/58/87、RGBA，且像素与「1024 源图独立 LANCZOS 缩放」一致（构建可复现）；
  ④ 二进制侧（Donut.dylib / Donut.plist / Root.plist / 入口 plist）与 1.1.0 逐字节相同；
  ⑤ 面板 20 条必需文案两语言齐全；
  ⑥ DonutPrefs 差异全在允许区（4 个 CDHash 槽 + 2 处版本串字节），长度不变。
"""
import io, sys, gzip, lzma, tarfile, hashlib, plistlib

sys.path.insert(0, r"C:\Users\张培斌\.workbuddy\skills\ios-deb-roothide-port\scripts")
import roothide_convert as RC
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
FAIL, OK = [], []

NEW = r'E:\deb\donut-bar120.deb'
BASE = r'E:\deb\_release\1.1.0\donut-bar110.deb'
ICON_SRC = r'E:\deb\_icons_weather\raw\weather-flat-icon-ring-light30-1024.png'
IP = 'Library/PreferenceBundles/DonutPrefs.bundle/'
ICONS = [(29, 'icon.png'), (58, 'icon@2x.png'), (87, 'icon@3x.png')]
PN = IP + 'DonutPrefs'
SLOT_LEN = {0x1550d: 20, 0x1580e: 32, 0x2942d: 20, 0x2972e: 32}
VER_SLOTS = (0xb63a, 0x1f6da)


def xar(p):
    m = dict(RC.parse_ar(open(p, 'rb').read()))
    dk = next(k for k in m if k.startswith('data.tar'))
    d = m[dk]
    dd = gzip.decompress(d) if d[:2] == b'\x1f\x8b' else lzma.decompress(d, format=lzma.FORMAT_ALONE)
    files = {}
    with tarfile.open(fileobj=io.BytesIO(dd)) as t:
        for x in t.getmembers():
            if x.isfile():
                files[x.name] = t.extractfile(x).read()
    cf = {}
    with tarfile.open(fileobj=io.BytesIO(gzip.decompress(m['control.tar.gz']))) as t:
        for x in t.getmembers():
            if x.isfile():
                cf[x.name] = t.extractfile(x).read()
    return files, cf


fn, cn = xar(NEW)
fb, cb = xar(BASE)

raw = open(NEW, 'rb').read()
print('%-22s %6d B  sha256=%s' % ('donut-bar120.deb', len(raw), hashlib.sha256(raw).hexdigest()))
print('%-22s %6d B  （对照基线）' % ('donut-bar110.deb', len(open(BASE, 'rb').read())))
print()

print('== ① 版本号已改为 1.2.0 ==')
t = cn['./control'].decode()
ver = [x for x in t.splitlines() if x.startswith('Version:')][0]
if ver == 'Version: 1.2.0':
    OK.append('control Version=1.2.0'); print('  [OK]   control: %s' % ver)
else:
    FAIL.append('control 版本号是 %s' % ver); print('  [FAIL] control: %s' % ver)

pa, pb = fn[PN], fb[PN]
c_new, c_old = pa.count(b'1.2.0\x00'), pa.count(b'1.1.0\x00')
if c_new == 2 and c_old == 0:
    OK.append('DonutPrefs 版本串 1.2.0 x2')
    print('  [OK]   DonutPrefs 版本串 1.2.0 出现 %d 次（两切片各一），1.1.0 残留 %d' % (c_new, c_old))
else:
    FAIL.append('DonutPrefs 版本串异常：1.2.0 x%d / 1.1.0 x%d' % (c_new, c_old))
    print('  [FAIL] DonutPrefs 1.2.0 x%d / 1.1.0 x%d' % (c_new, c_old))

for off in VER_SLOTS:
    print('  [--]   版本串槽 @%#x  1.1.0=%r  1.2.0=%r' % (off, pb[off - 4:off + 1], pa[off - 4:off + 1]))

print()
print('== ② 与 1.1.0 相比差异恰好 = 3 图标 + DonutPrefs ==')
diff = []
for k in sorted(set(fb) | set(fn)):
    if k not in fb or k not in fn:
        FAIL.append('文件增删 %s' % k); print('  [FAIL] 文件增删 %s' % k); continue
    if fb[k] != fn[k]:
        diff.append(k)
expect = sorted([PN] + [IP + n for _, n in ICONS])
if diff == expect:
    OK.append('差异恰为图标+DonutPrefs')
    print('  [OK]   差异 = 3 个图标 + DonutPrefs，其余 %d 个文件逐字节相同' % (len(fn) - 4))
else:
    FAIL.append('差异超出预期：%s' % diff); print('  [FAIL] 预期 %s，实际 %s' % (expect, diff))

print()
print('== ③ 图标三档尺寸/模式/像素一致性 ==')
src = Image.open(ICON_SRC).convert('RGBA')
for isz, n in ICONS:
    im = Image.open(io.BytesIO(fn[IP + n]))
    ok_sz = im.size == (isz, isz)
    ok_md = im.mode == 'RGBA'
    ref = src.resize((isz, isz), Image.LANCZOS)
    ok_px = list(im.convert('RGBA').getdata()) == list(ref.getdata())
    if ok_sz and ok_md and ok_px:
        OK.append('%s %dx%d 像素一致' % (n, isz, isz))
        print('  [OK]   %-14s %dx%d %s  %d B  像素=源图LANCZOS缩小' % (n, isz, isz, im.mode, len(fn[IP + n])))
    else:
        FAIL.append('%s 尺寸/模式/像素不符 (%r %s px=%s)' % (n, im.size, im.mode, ok_px))
        print('  [FAIL] %-14s size=%r mode=%s 像素一致=%s' % (n, im.size, im.mode, ok_px))
tot = sum(len(fn[IP + n]) for _, n in ICONS)
print('  [--]   图标合计 %d B（1.1.0 为 13453 B）' % tot)

print()
print('== ④ 二进制侧与 1.1.0 逐字节相同 ==')
for k in ('Library/MobileSubstrate/DynamicLibraries/Donut.dylib',
          'Library/MobileSubstrate/DynamicLibraries/Donut.plist',
          IP + 'Root.plist',
          'Library/PreferenceLoader/Preferences/Donut.plist'):
    if fb.get(k) == fn.get(k):
        OK.append('%s 相同' % k.split('/')[-1])
        print('  [OK]   %-56s 相同 (%d B)' % (k.split('/')[-1], len(fn[k])))
    else:
        FAIL.append('%s 不同' % k)
        print('  [FAIL] %s' % k)

print()
print('== ⑤ 面板 20 条必需文案两语言齐全 ==')
rp = plistlib.loads(fn[IP + 'Root.plist'])
need = set()
for it in rp['items']:
    for k in ('label', 'footerText'):
        if k in it:
            need.add(it[k])
    for s in it.get('validTitles', []):
        need.add(s)
for lang in ('zh-Hans', 'en'):
    d = plistlib.loads(fn[IP + '%s.lproj/Root.strings' % lang])
    missing = [k for k in need if k not in d]
    if missing:
        FAIL.append('%s 缺失 %r' % (lang, missing))
        print('  [FAIL] %-8s 缺失 %r' % (lang, missing))
    else:
        OK.append('%s 文案齐全' % lang)
        print('  [OK]   %-8s %d 条文案齐全（条目数 %d）' % (lang, len(need), len(d)))

print()
print('== ⑥ DonutPrefs 差异全在允许区 ==')
allowed = set()
for off in VER_SLOTS:
    allowed |= set(range(off - 4, off + 1))
for off, ln in SLOT_LEN.items():
    allowed |= set(range(off, off + ln))
if len(pa) != len(pb):
    FAIL.append('DonutPrefs 长度变了'); print('  [FAIL] 长度 %d -> %d' % (len(pb), len(pa)))
else:
    dif = set(i for i in range(len(pa)) if pa[i] != pb[i])
    outside = sorted(dif - allowed)
    print('  差异 %d 字节（允许区 %d 字节）' % (len(dif), len(allowed)))
    for nm, off, ln in (('arm64  SHA-1  CDHash', 0x1550d, 20), ('arm64  SHA-256 CDHash', 0x1580e, 32),
                        ('arm64e SHA-1  CDHash', 0x2942d, 20), ('arm64e SHA-256 CDHash', 0x2972e, 32)):
        if pa[off:off + ln] != pb[off:off + ln]:
            OK.append(nm); print('  [OK]   %s @%#x 整块 %dB 已更新' % (nm, off, ln))
        else:
            FAIL.append('%s 未变' % nm); print('  [FAIL] %s @%#x 未变' % (nm, off))
    if outside:
        FAIL.append('允许区外 %d 字节')
        print('  [FAIL] 允许区外：%s' % ' '.join('%#x' % x for x in outside[:20]))
    else:
        OK.append('差异全在允许区'); print('  [OK]   全部差异都在允许区之内')

print()
print('== ⑦ control 除 Version 外与 1.1.0 相同 ==')
dn = [x for x in t.splitlines() if not x.startswith('Version:')]
ds = [x for x in cb['./control'].decode().splitlines() if not x.startswith('Version:')]
if dn == ds:
    OK.append('control 除 Version 外相同'); print('  [OK]   除 Version 外逐行相同')
else:
    FAIL.append('control 非 Version 字段有变化')
    print('  [FAIL] 差异：%s' % [x for x in dn if x not in ds])

print()
print('=' * 64)
print('FAIL %d / 断言 %d' % (len(FAIL), len(OK) + len(FAIL)))
for f in FAIL:
    print('  !', f)
sys.exit(1 if FAIL else 0)
