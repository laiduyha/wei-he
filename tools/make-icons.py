#!/usr/bin/env python3
"""Sinh toàn bộ icon cho 维河.

Đây là nguồn hình học duy nhất của mọi tệp trong `assets/favicon/` — sửa hình
ở đây rồi chạy lại, đừng chỉnh tay PNG/SVG.

    python3 tools/make-icons.py

Hình lấy ý từ bức sông núi ở `assets/images/bio-photo.jpeg`, rút về bốn mảng
lớn: trời giấy ấm ở trên, dải núi đá vôi màu mực vắt ngang, mặt nước xanh nhạt
lạnh loe từ khe núi xuống kín cả tiền cảnh, và một con thuyền chu sa — điểm bão
hoà duy nhất của cả icon. Xen giữa là hai lớp núi nhạt dần về xa để lấy chiều
sâu.

Ba điều rút ra sau mấy lần vẽ sai, đừng làm lại:

  * Sông là hình chính, không phải rặng núi. Ở 48px chỉ còn mảng nước sáng là
    nhận ra được, chi tiết núi tan hết.
  * Núi đá vôi phải *bè*: chóp cụt, bề ngang xấp xỉ bề cao. Vẽ thành tháp thanh
    và nhọn thì ra hàng cây, vẽ thành tam giác cân thì ra logo cắm trại.
  * Mọi khối núi phải chúi xuống *dưới* mặt nước ở cả hai đầu. Cho khối dừng
    lại bằng mép dọc thì ra hàng cột, còn cắt ngang bằng một dải bờ thì được
    cái gạch chia đôi icon với một vùng đen phẳng ở dưới.

Nên ở đây mặt nước là mặt phẳng nền chung: vẽ hết các khối núi trước, rồi phủ
nước lên: cái gì dưới mực nước thì biến mất, hai bờ tự lùi dần theo tông đậm
(khối gần) - xám (khối lùi) - nước.
"""

import math
import os
import subprocess
import sys

from PIL import Image, ImageChops, ImageDraw, ImageFilter

# ---------------------------------------------------------------------- màu
# theo đúng bảng màu skin "sunrise" của minimal-mistakes
PAPER = (232, 213, 183)  # $background-color #e8d5b7
INK = (14, 36, 49)  # $dark-gray       #0e2431
VERM = (252, 58, 82)  # $primary-color   #fc3a52


def mix(a, b, t):
    """Trộn màu: t là tỉ lệ của a."""
    return tuple(round(a[i] * t + b[i] * (1 - t)) for i in range(3))


HAZE = mix(INK, PAPER, 0.38)  # quả núi xa nhất, trong sương
STEP = mix(INK, PAPER, 0.70)  # hai khối lùi một lớp
RIM = mix(PAPER, INK, 0.90)  # bãi bờ được nắng, viền theo mép nước
WATER = mix((120, 170, 168), PAPER, 0.62)  # nước lạnh, tương phản với trời ấm

# ------------------------------------------------------------------ hình học
# Toạ độ "scene" 0..1; khung vẽ phóng quanh tâm nên phần ngoài [0,1] bị cắt.
# Các khối trải rộng hẳn ra ngoài khung để mọi mức phóng vẫn kín mép.
X0, X1, Y1 = -0.40, 1.40, 1.45

# Mặt nước gồm hai phần. Dải nước tiền cảnh phải *nông và rộng* mới đọc ra mặt
# phẳng lùi xa; hồi đầu vẽ nó thành cái nêm nhọn chụm lên giữa thì hình - nền
# đảo ngược, mảng sáng hoá ra một quả núi nhạt còn con thuyền thì như đậu trên
# đồi. Chiều sâu dồn cho lạch nước hẹp vót lên khe núi.
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

# Vũng nước lấn lên khe giữa hai khối lùi: (y, tâm x, nửa rộng).
# Phải thấp và loe — vẽ thành lạch cao, hẹp, thành thẳng thì ra cái đường dốc
# chứ không ra nước, nhất là khi còn viền bãi chạy quanh.
CHANNEL = [
    (0.585, 0.472, 0.020),
    (0.606, 0.468, 0.036),
    (0.628, 0.462, 0.054),
    (0.650, 0.454, 0.074),
    (0.690, 0.444, 0.100),  # đủ sâu để nhập hẳn vào dải nước
]

# Đường đỉnh từng khối núi, hai đầu đều chúi xuống dưới mực nước.
# Hai điểm liền nhau cùng cao độ thì cho chóp cụt.
NEAR_LEFT = [
    (X0, 0.500),
    (-0.14, 0.460),
    (-0.05, 0.315),
    (0.030, 0.252),
    (0.085, 0.245),  # chóp cụt
    (0.140, 0.330),  # yên
    (0.196, 0.238),
    (0.248, 0.212),
    (0.296, 0.300),
    (0.330, 0.430),
    (0.352, 0.600),
    (0.366, 0.790),  # chúi xuống dưới nước
]
NEAR_RIGHT = [
    (0.598, 0.700),  # chúi xuống dưới nước
    (0.622, 0.430),
    (0.655, 0.290),
    (0.706, 0.190),
    (0.762, 0.172),  # chóp cao nhất cả hình
    (0.812, 0.262),
    (0.860, 0.228),
    (0.912, 0.285),
    (0.975, 0.246),
    (1.060, 0.300),
    (1.140, 0.420),
    (X1, 0.480),
]
# hai khối lùi cố ý lệch nhau: bên trái thấp và bè, bên phải cao và thót, nếu
# không thì thành hai cái cột giống nhau kẹp lấy khe như một cái cổng
STEP_LEFT = [
    (0.258, 0.830),
    (0.286, 0.500),
    (0.322, 0.396),
    (0.366, 0.352),
    (0.402, 0.372),
    (0.428, 0.470),
    (0.442, 0.660),
]
STEP_RIGHT = [
    (0.505, 0.660),
    (0.520, 0.450),
    (0.548, 0.318),
    (0.590, 0.272),
    (0.634, 0.320),
    (0.668, 0.470),
    (0.690, 0.740),
]
HAZE_MASS = [
    (0.326, 0.780),
    (0.360, 0.470),
    (0.398, 0.412),
    (0.452, 0.386),
    (0.508, 0.400),
    (0.556, 0.452),
    (0.596, 0.560),
    (0.628, 0.700),
]

RIM_WIDTH = 0.007  # bãi bờ được nắng, chạy sát trên mép dải nước
FLOW_INSET = 0.026  # nét dòng chảy phải thụt vào khỏi bờ chừng này
FLOW_ALPHA = 95

# nét dòng chảy: (y, [(x0, x1), ...], độ vồng, bề dày)
# So le chiều vồng và chừa khoảng hở cho khỏi thành mấy vạch đếm đều tăm tắp.
FLOW_FULL = [
    (0.775, [(0.285, 0.560)], 0.009, 0.0080),
    (0.850, [(0.180, 0.455), (0.535, 0.800)], -0.008, 0.0090),
    (0.925, [(0.100, 0.630)], 0.010, 0.0100),
]
FLOW_MID = [(0.865, [(0.165, 0.515), (0.595, 0.825)], -0.010, 0.0160)]

BOAT = dict(cx=0.400, cy=0.815, hw=0.078, hull=0.029, canopy=0.033)


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


def massif(top_controls):
    """Khối núi: đường đỉnh nội suy mềm, hai mép đổ xuống đáy khung.

    Hai đầu đường đỉnh đã nằm dưới mực nước nên mép dọc bị nước phủ hết.
    """
    top = catmull(top_controls)
    return [(top_controls[0][0], Y1)] + top + [(top_controls[-1][0], Y1)]


def band_polygon(dy=0.0):
    """Dải nước tiền cảnh: mép trên là WATER_BAND dịch xuống `dy`."""
    top = [(x, y + dy) for x, y in catmull(WATER_BAND, per_seg=12)]
    return top + [(X1, Y1), (X0, Y1)]


def channel_polygon(grow=0.0):
    """Lạch nước vót lên khe núi, nới ra `grow` mỗi bên."""
    samples = catmull(CHANNEL)
    left = [(cx - hw - grow, y) for y, cx, hw in samples]
    right = [(cx + hw + grow, y) for y, cx, hw in reversed(samples)]
    return left + right


def water_shapes():
    """Mặt nước là hợp của dải tiền cảnh và vũng nước — vẽ chồng hai mảng."""
    return [band_polygon(), channel_polygon()]


def band_y(x):
    """Cao độ mép dải nước tại x, nội suy từ đường đã lấy mẫu."""
    pts = catmull(WATER_BAND, per_seg=12)
    for (xa, ya), (xb, yb) in zip(pts, pts[1:]):
        if xa <= x <= xb:
            t = 0.0 if xb == xa else (x - xa) / (xb - xa)
            return ya + (yb - ya) * t
    return pts[0][1] if x < pts[0][0] else pts[-1][1]


def massif_to_band(top_controls, n=48):
    """Khối núi cắt ngang ở mực nước, dùng cho bóng một màu của Safari.

    Safari không chắc chắn tôn trọng <mask> trong tệp mask-icon, nên ở đó không
    khoét nước bằng mask mà đóng luôn đáy khối bằng chính mép dải nước.
    """
    top = [(x, min(y, band_y(x))) for x, y in catmull(top_controls)]
    xa, xb = top[0][0], top[-1][0]
    bottom = [
        (xb + (xa - xb) * i / n, band_y(xb + (xa - xb) * i / n)) for i in range(n + 1)
    ]
    return top + bottom


def flow_path(y0, x0, x1, amp, n=40):
    return [
        (
            x0 + (x1 - x0) * (i / n),
            y0 + amp * math.sin(math.pi * (i / n)),
        )
        for i in range(n + 1)
    ]


def boat_shapes():
    """Thân thuyền và mái che, hơi lệch cho khỏi cân đối cứng."""
    cx, cy, hw = BOAT["cx"], BOAT["cy"], BOAT["hw"]
    hull, canopy = BOAT["hull"], BOAT["canopy"]
    return [
        [
            (cx - hw, cy),
            (cx + hw, cy),
            (cx + hw * 0.60, cy + hull),
            (cx - hw * 0.64, cy + hull),
        ],
        [
            (cx - hw * 0.50, cy),
            (cx - hw * 0.40, cy - canopy),
            (cx + hw * 0.38, cy - canopy),
            (cx + hw * 0.48, cy),
        ],
    ]


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

    def px(self, w):
        return max(1.0, w * self.scale * self.size)


# (có khối lùi, có bãi bờ, nét dòng chảy, có thuyền)
LEVELS = {
    "full": (True, True, FLOW_FULL, True),
    "mid": (True, True, FLOW_MID, True),
    "min": (False, False, [], False),
}


def fills_for(detail):
    """Các mảng tô, theo thứ tự xa tới gần."""
    with_step = LEVELS[detail][0]
    out = [(massif(HAZE_MASS), HAZE)]
    if with_step:
        out.append((massif(STEP_LEFT), STEP))
        out.append((massif(STEP_RIGHT), STEP))
    out.append((massif(NEAR_LEFT), INK))
    out.append((massif(NEAR_RIGHT), INK))
    return out


def render(px, detail="full", scale=1.12, dy=0.0, ss=4):
    """Vẽ ở ss lần kích thước rồi thu nhỏ bằng LANCZOS để khử răng cưa."""
    _, with_rim, flows, with_boat = LEVELS[detail]
    size = px * ss
    tx = Tx(size, scale, dy)
    img = Image.new("RGB", (size, size), PAPER)
    d = ImageDraw.Draw(img)

    for pts, colour in fills_for(detail):
        d.polygon(tx.poly(pts), fill=colour)

    # Vạch bãi chỉ chạy theo mép dải nước, không viền quanh vũng — viền cả vũng
    # thì nó thành một mảng có đường bao riêng, trông như vật thể chứ không như
    # nước. Vũng vẽ sau nên cắt ngang vạch bãi, đúng như nước ăn vào bờ.
    if with_rim:
        d.polygon(tx.poly(band_polygon(-RIM_WIDTH)), fill=RIM)
    for pts in water_shapes():
        d.polygon(tx.poly(pts), fill=WATER)

    if flows:
        draw_flow(img, tx, size, flows)
    if with_boat:
        draw_boat(img, tx, size)

    return img.resize((px, px), Image.LANCZOS)


def draw_flow(img, tx, size, flows):
    """Nét dòng chảy, cắt gọn trong mặt nước và thụt vào khỏi bờ."""
    strokes = Image.new("L", (size, size), 0)
    ds = ImageDraw.Draw(strokes)
    for y0, segs, amp, width in flows:
        pw = int(round(tx.px(width)))
        for x0, x1 in segs:
            pts = tx.poly(flow_path(y0, x0, x1, amp))
            ds.line(pts, fill=255, width=pw, joint="curve")
            r = pw / 2
            for p in (pts[0], pts[-1]):
                ds.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=255)
    inner = Image.new("L", (size, size), 0)
    ImageDraw.Draw(inner).polygon(tx.poly(band_polygon(FLOW_INSET)), fill=255)
    clipped = ImageChops.multiply(strokes, inner)
    img.paste(INK, mask=clipped.point(lambda v: v * FLOW_ALPHA // 255))


def draw_boat(img, tx, size):
    """Chu sa trên nước, có viền nước mảnh để không lẫn vào nét dòng chảy."""
    mask = Image.new("L", (size, size), 0)
    dm = ImageDraw.Draw(mask)
    for shape in boat_shapes():
        dm.polygon(tx.poly(shape), fill=255)

    halo = max(1, int(round(0.006 * tx.scale * size)))
    box = mask.getbbox()
    pad = halo * 2 + 4
    crop = (
        max(0, box[0] - pad),
        max(0, box[1] - pad),
        min(size, box[2] + pad),
        min(size, box[3] + pad),
    )
    grown = Image.new("L", (size, size), 0)
    grown.paste(mask.crop(crop).filter(ImageFilter.MaxFilter(halo * 2 + 1)), crop)

    img.paste(WATER, mask=grown)
    img.paste(VERM, mask=mask)


# --------------------------------------------------------------------- xuất SVG
def fmt(v):
    return f"{v:.2f}".rstrip("0").rstrip(".")


def hexc(c):
    return "#%02x%02x%02x" % c


def svg_poly(tx, pts, fill):
    pt = " ".join(f"{fmt(x)},{fmt(y)}" for x, y in tx.poly(pts))
    return f'<polygon points="{pt}" fill="{fill}"/>'


def svg_path(tx, pts, colour, width, opacity=None):
    d = "M " + " L ".join(f"{fmt(x)} {fmt(y)}" for x, y in tx.poly(pts))
    op = f' stroke-opacity="{opacity:.3f}"' if opacity is not None else ""
    return (
        f'<path d="{d}" fill="none" stroke="{colour}" stroke-width="{fmt(width)}"'
        f' stroke-linecap="round" stroke-linejoin="round"{op}/>'
    )


def wrap_svg(box, body):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {box} {box}">\n'
        + "\n".join("  " + line for line in body)
        + "\n</svg>\n"
    )


def build_svg(box, detail, scale):
    _, with_rim, flows, with_boat = LEVELS[detail]
    tx = Tx(box, scale)

    body = [f'<rect width="{box}" height="{box}" fill="{hexc(PAPER)}"/>']
    body += [svg_poly(tx, pts, hexc(colour)) for pts, colour in fills_for(detail)]
    if with_rim:
        body.append(svg_poly(tx, band_polygon(-RIM_WIDTH), hexc(RIM)))
    body += [svg_poly(tx, pts, hexc(WATER)) for pts in water_shapes()]

    if flows:
        clip = svg_poly(tx, band_polygon(FLOW_INSET), "white")
        body.append(f'<clipPath id="w">{clip}</clipPath>')
        strokes = "".join(
            svg_path(tx, flow_path(y0, x0, x1, amp), hexc(INK), tx.px(w), FLOW_ALPHA / 255)
            for y0, segs, amp, w in flows
            for x0, x1 in segs
        )
        body.append(f'<g clip-path="url(#w)">{strokes}</g>')

    if with_boat:
        body += [svg_poly(tx, s, hexc(VERM)) for s in boat_shapes()]

    return wrap_svg(box, body)


MONO_MASSIFS = [NEAR_LEFT, NEAR_RIGHT]
MONO_DY = -0.085  # bóng chỉ chiếm nửa trên, dịch xuống cho cân giữa khung


def build_mono_svg(box, scale):
    """Bóng một màu cho mask-icon: chỉ vài đa giác đen đặc, không mask, không mờ."""
    tx = Tx(box, scale, MONO_DY)
    body = [svg_poly(tx, massif_to_band(m), "black") for m in MONO_MASSIFS]
    return wrap_svg(box, body)


# ------------------------------------------------------- kiểm tra vùng an toàn
def key_points():
    """Những điểm mất đi thì hình hỏng.

    Không kể mép ngoài các khối núi và mặt nước phía dưới: chúng cố ý chạy tràn
    ra ngoài khung, bị cắt là đúng ý.
    """
    cx, cy, hw = BOAT["cx"], BOAT["cy"], BOAT["hw"]
    return {
        "chóp khối bên trái": NEAR_LEFT[7],
        "chóp khối bên phải": NEAR_RIGHT[4],
        "chóp núi xa": HAZE_MASS[3],
        "ngọn lạch nước": (CHANNEL[0][1], CHANNEL[0][0]),
        "thuyền, mạn trái": (cx - hw, cy + BOAT["hull"]),
        "thuyền, mạn phải": (cx + hw, cy + BOAT["hull"]),
        "thuyền, mái che": (cx, cy - BOAT["canopy"]),
    }


def check_maskable(scale, dy, limit=0.40):
    rows = []
    for name, (x, y) in key_points().items():
        mx = 0.5 + (x - 0.5) * scale
        my = 0.5 + (y - 0.5) * scale - dy
        rows.append((math.hypot(mx - 0.5, my - 0.5), name))
    rows.sort(reverse=True)
    return rows, limit


# ------------------------------------------------------------------- xuất tệp
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "favicon")
STALE = ["browserconfig.xml"]

BLEED = 1.12  # phủ kín khung
MASK_SCALE, MASK_DY = 0.84, 0.0  # maskable: kéo nội dung chính vào vòng an toàn
MID_SCALE, MIN_SCALE = 1.18, 1.24


def main():
    os.makedirs(OUT, exist_ok=True)

    def save(img, name):
        p = os.path.join(OUT, name)
        img.save(p, optimize=True)
        print(f"  {name:28s} {img.size[0]:>3d}px  {os.path.getsize(p):>7,d} B")

    print("phủ kín khung (any):")
    save(render(512), "android-chrome-512x512.png")
    save(render(192), "android-chrome-192x192.png")
    save(render(180), "apple-touch-icon.png")  # iOS cần ảnh đục, không alpha

    print("maskable:")
    rows, limit = check_maskable(MASK_SCALE, MASK_DY)
    for dist, name in rows:
        print(f"  {'ok ' if dist <= limit else 'VƯỢT'} {dist:.3f} / {limit:.2f}  {name}")
    if rows[0][0] > limit:
        sys.exit("nội dung chính tràn khỏi vòng an toàn, giảm MASK_SCALE rồi chạy lại")
    save(render(512, scale=MASK_SCALE, dy=MASK_DY), "maskable-512x512.png")
    save(render(192, scale=MASK_SCALE, dy=MASK_DY), "maskable-192x192.png")

    print("favicon:")
    f48 = render(48, detail="mid", scale=MID_SCALE)
    f32 = render(32, detail="mid", scale=MID_SCALE)
    f16 = render(16, detail="min", scale=MIN_SCALE)
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
        ("icon.svg", build_svg(512, "full", BLEED)),
        ("safari-pinned-tab.svg", build_mono_svg(16, MIN_SCALE)),
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
