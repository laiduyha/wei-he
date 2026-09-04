#!/usr/bin/env python3
"""Sinh toàn bộ icon cho 维河.

Đây là nguồn duy nhất của mọi tệp trong `assets/favicon/` — sửa ở đây rồi chạy
lại, đừng chỉnh tay PNG/SVG.

    python3 tools/make-icons.py

Icon là chính bức sông núi `assets/images/bio-photo.jpeg` (ảnh đại diện của
site), đặt trong một ô vuông bo góc trên nền giấy be của skin "sunrise" — cùng
màu nền và cùng kiểu bo tròn với bộ icon cũ khi launcher ốp mặt nạ lên, chỉ khác
là ruột icon giờ là ảnh thật chứ không phải tranh vẽ lại.

Mỗi cỡ chỉ khác nhau ở độ thụt của ảnh so với mép khung:

  * `any` (android-chrome, apple-touch-icon, icon.svg): thụt nhẹ, ảnh chiếm gần
    hết khung, viền giấy mảnh quanh ngoài.
  * `maskable`: thụt sâu để cả ô ảnh lọt trong vòng an toàn (bán kính 40% kể
    từ tâm) — launcher cắt tròn hay bo góc thế nào thì phần nhìn thấy vẫn là
    giấy bao quanh ảnh, không cắt vào ảnh.
  * favicon 16/32/48: thụt đúng một hai điểm ảnh, và làm nét nhẹ vì thu từ
    1536px xuống 16px thì ảnh nhoè hết.

Riêng `safari-pinned-tab.svg` là bóng một màu, không thể là ảnh, nên vẫn giữ
hình núi đá vôi vẽ tay từ bộ cũ (phần hình học ở dưới chỉ phục vụ tệp này).
"""

import base64
import io
import math
import os
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFilter

# ---------------------------------------------------------------------- màu
# theo đúng bảng màu skin "sunrise" của minimal-mistakes
PAPER = (232, 213, 183)  # $background-color #e8d5b7
INK = (14, 36, 49)  # $dark-gray       #0e2431

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PHOTO = os.path.join(ROOT, "assets", "images", "bio-photo.jpeg")
OUT = os.path.join(ROOT, "assets", "favicon")
STALE = ["browserconfig.xml"]

# (độ thụt mỗi bên, bán kính bo góc) tính theo cạnh khung
ANY = (0.06, 0.20)
MASKABLE = (0.18, 0.15)
SMALL = (1 / 16, 0.22)  # 16px: thụt 1px; 32px: 2px; 48px: 3px

# vòng an toàn của maskable: bán kính 0.4 kể từ tâm (spec W3C)
SAFE_R = 0.40


# ------------------------------------------------------------------- ảnh
def load_photo():
    im = Image.open(PHOTO).convert("RGB")
    w, h = im.size
    s = min(w, h)  # cắt vuông từ tâm, phòng khi đổi ảnh không vuông
    return im.crop(((w - s) // 2, (h - s) // 2, (w - s) // 2 + s, (h - s) // 2 + s))


def rounded_mask(side, radius):
    """Mặt nạ ô ảnh: vuông bo góc, cùng cỡ với ô ảnh."""
    m = Image.new("L", (side, side), 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, side - 1, side - 1], radius=radius, fill=255)
    return m


def compose(photo, px, spec, ss=4, sharpen=False):
    """Ảnh trong ô bo góc trên nền giấy.

    Vẽ ở ss lần kích thước rồi thu bằng LANCZOS để mép bo góc mịn; ảnh cũng thu
    thẳng từ bản gốc xuống cỡ đích, không qua bước trung gian.
    """
    pad, rad = spec
    size = px * ss
    inset = round(pad * size)
    side = size - 2 * inset
    tile = photo.resize((side, side), Image.LANCZOS)
    if sharpen:
        tile = tile.filter(ImageFilter.UnsharpMask(radius=2, percent=80, threshold=2))

    img = Image.new("RGB", (size, size), PAPER)
    img.paste(tile, (inset, inset), rounded_mask(side, round(rad * size)))
    return img.resize((px, px), Image.LANCZOS)


def check_maskable(spec, limit=SAFE_R):
    """Điểm xa tâm nhất của ô ảnh là tâm cung bo góc cộng bán kính bo."""
    pad, rad = spec
    half = 0.5 - pad
    corner = math.hypot(half - rad, half - rad) + rad
    return corner, limit


# --------------------------------------------------------------------- SVG
def fmt(v):
    return f"{v:.2f}".rstrip("0").rstrip(".")


def hexc(c):
    return "#%02x%02x%02x" % c


def wrap_svg(box, body, xlink=False):
    ns = ' xmlns:xlink="http://www.w3.org/1999/xlink"' if xlink else ""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg"{ns} viewBox="0 0 {box} {box}">\n'
        + "\n".join("  " + line for line in body)
        + "\n</svg>\n"
    )


def build_photo_svg(photo, box, spec, jpeg_px=512, quality=82):
    """icon.svg: ảnh JPEG nhúng base64, cắt bằng clipPath bo góc, trên nền giấy."""
    pad, rad = spec
    inset, side, r = pad * box, box * (1 - 2 * pad), rad * box
    buf = io.BytesIO()
    photo.resize((jpeg_px, jpeg_px), Image.LANCZOS).save(
        buf, "JPEG", quality=quality, optimize=True, progressive=False
    )
    data = base64.b64encode(buf.getvalue()).decode("ascii")
    body = [
        f'<rect width="{box}" height="{box}" fill="{hexc(PAPER)}"/>',
        f'<clipPath id="r"><rect x="{fmt(inset)}" y="{fmt(inset)}" '
        f'width="{fmt(side)}" height="{fmt(side)}" rx="{fmt(r)}"/></clipPath>',
        f'<image x="{fmt(inset)}" y="{fmt(inset)}" width="{fmt(side)}" '
        f'height="{fmt(side)}" clip-path="url(#r)" '
        f'preserveAspectRatio="xMidYMid slice" '
        f'xlink:href="data:image/jpeg;base64,{data}"/>',
    ]
    return wrap_svg(box, body, xlink=True)


# ------------------------------------- bóng một màu cho safari-pinned-tab.svg
# Toạ độ "scene" 0..1; khung vẽ phóng quanh tâm nên phần ngoài [0,1] bị cắt.
X0, X1, Y1 = -0.40, 1.40, 1.45

# mép trên của mặt nước — đáy của các khối núi
WATER_BAND = [
    (X0, 0.745),
    (0.030, 0.708),
    (0.160, 0.680),
    (0.300, 0.659),
    (0.440, 0.647),
    (0.580, 0.653),
    (0.720, 0.669),
    (0.860, 0.693),
    (1.000, 0.719),
    (X1, 0.765),
]

# Đường đỉnh từng khối núi, hai đầu đều chúi xuống dưới mực nước.
NEAR_LEFT = [
    (X0, 0.500),
    (-0.14, 0.460),
    (-0.05, 0.315),
    (0.030, 0.252),
    (0.085, 0.245),
    (0.140, 0.330),
    (0.196, 0.238),
    (0.248, 0.212),
    (0.296, 0.300),
    (0.330, 0.430),
    (0.352, 0.600),
    (0.366, 0.790),
]
NEAR_RIGHT = [
    (0.598, 0.700),
    (0.622, 0.430),
    (0.655, 0.290),
    (0.706, 0.190),
    (0.762, 0.172),
    (0.812, 0.262),
    (0.860, 0.228),
    (0.912, 0.285),
    (0.975, 0.246),
    (1.060, 0.300),
    (1.140, 0.420),
    (X1, 0.480),
]


def catmull(rows, per_seg=14):
    """Nội suy Catmull-Rom theo chỉ số, giữ nguyên số chiều của mỗi hàng."""
    p = [rows[0]] + list(rows) + [rows[-1]]
    out = []
    for i in range(len(p) - 3):
        a, b, c, d = p[i], p[i + 1], p[i + 2], p[i + 3]
        for j in range(per_seg):
            t = j / per_seg
            t2, t3 = t * t, t * t * t
            out.append(
                tuple(
                    0.5
                    * (
                        2 * b[k]
                        + (-a[k] + c[k]) * t
                        + (2 * a[k] - 5 * b[k] + 4 * c[k] - d[k]) * t2
                        + (-a[k] + 3 * b[k] - 3 * c[k] + d[k]) * t3
                    )
                    for k in range(len(a))
                )
            )
    out.append(tuple(rows[-1]))
    return out


def band_y(x):
    """Cao độ mép dải nước tại x, nội suy từ đường đã lấy mẫu."""
    pts = catmull(WATER_BAND, per_seg=12)
    for (xa, ya), (xb, yb) in zip(pts, pts[1:]):
        if xa <= x <= xb:
            t = 0.0 if xb == xa else (x - xa) / (xb - xa)
            return ya + (yb - ya) * t
    return pts[0][1] if x < pts[0][0] else pts[-1][1]


def massif_to_band(top_controls, n=48):
    """Khối núi cắt ngang ở mực nước.

    Safari không chắc chắn tôn trọng <mask> trong tệp mask-icon, nên không khoét
    nước bằng mask mà đóng luôn đáy khối bằng chính mép dải nước.
    """
    top = [(x, min(y, band_y(x))) for x, y in catmull(top_controls)]
    xa, xb = top[0][0], top[-1][0]
    bottom = [
        (xb + (xa - xb) * i / n, band_y(xb + (xa - xb) * i / n)) for i in range(n + 1)
    ]
    return top + bottom


class Tx:
    """Ánh xạ toạ độ scene sang pixel: phóng quanh tâm, tuỳ chọn dịch lên."""

    def __init__(self, size, scale, dy=0.0):
        self.size, self.scale, self.dy = size, scale, dy

    def __call__(self, p):
        x, y = p
        return (
            self.size * (0.5 + (x - 0.5) * self.scale),
            self.size * (0.5 + (y - 0.5) * self.scale - self.dy),
        )

    def poly(self, pts):
        return [self(p) for p in pts]


def svg_poly(tx, pts, fill):
    pt = " ".join(f"{fmt(x)},{fmt(y)}" for x, y in tx.poly(pts))
    return f'<polygon points="{pt}" fill="{fill}"/>'


MONO_SCALE = 1.24
MONO_DY = -0.085  # bóng chỉ chiếm nửa trên, dịch xuống cho cân giữa khung


def build_mono_svg(box=16):
    """Bóng một màu cho mask-icon: chỉ vài đa giác đen đặc, không mask, không mờ."""
    tx = Tx(box, MONO_SCALE, MONO_DY)
    body = [svg_poly(tx, massif_to_band(m), "black") for m in (NEAR_LEFT, NEAR_RIGHT)]
    return wrap_svg(box, body)


# ------------------------------------------------------------------- xuất tệp
def main():
    os.makedirs(OUT, exist_ok=True)
    photo = load_photo()

    def save(img, name):
        p = os.path.join(OUT, name)
        img.save(p, optimize=True)
        print(f"  {name:28s} {img.size[0]:>3d}px  {os.path.getsize(p):>7,d} B")

    print("any:")
    save(compose(photo, 512, ANY, ss=2), "android-chrome-512x512.png")
    save(compose(photo, 192, ANY), "android-chrome-192x192.png")
    save(compose(photo, 180, ANY), "apple-touch-icon.png")  # iOS cần ảnh đục

    print("maskable:")
    corner, limit = check_maskable(MASKABLE)
    print(f"  {'ok ' if corner <= limit else 'VƯỢT'} góc ô ảnh {corner:.3f} / {limit:.2f}")
    if corner > limit:
        sys.exit("ô ảnh tràn khỏi vòng an toàn, tăng độ thụt của MASKABLE rồi chạy lại")
    save(compose(photo, 512, MASKABLE, ss=2), "maskable-512x512.png")
    save(compose(photo, 192, MASKABLE), "maskable-192x192.png")

    print("favicon:")
    f48 = compose(photo, 48, SMALL, sharpen=True)
    f32 = compose(photo, 32, SMALL, sharpen=True)
    f16 = compose(photo, 16, SMALL, sharpen=True)
    save(f32, "favicon-32x32.png")
    save(f16, "favicon-16x16.png")

    ico = os.path.join(OUT, "favicon.ico")
    tmp = [os.path.join(OUT, f".tmp-{s}.png") for s in (16, 32, 48)]
    for img, p in zip((f16, f32, f48), tmp):
        img.save(p)
    subprocess.run(["convert", *tmp, ico], check=True)
    for p in tmp:
        os.remove(p)
    print(f"  {'favicon.ico':28s} 16/32/48 {os.path.getsize(ico):>7,d} B")

    print("svg:")
    for name, svg in (
        ("icon.svg", build_photo_svg(photo, 512, ANY)),
        ("safari-pinned-tab.svg", build_mono_svg()),
    ):
        p = os.path.join(OUT, name)
        with open(p, "w") as f:
            f.write(svg)
        print(f"  {name:28s} vector {os.path.getsize(p):>7,d} B")

    for name in STALE:
        p = os.path.join(OUT, name)
        if os.path.exists(p):
            os.remove(p)
            print(f"đã xoá tệp thừa: {name}")


if __name__ == "__main__":
    main()
