#!/usr/bin/env python3
"""Draw 'The World in One Picture — Saturday 21 November 2026'.

A newspaper front page, 1024x1024, drawn with Pillow only. Six stories from
21 November 2026, each with a small pictogram in its label band, plus a
footer ticker. Deterministic: no timestamps, no randomness, fixed font paths.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
NAVY = (20, 33, 61)
NAVY2 = (27, 45, 82)
GOLD = (201, 162, 39)
INK = (24, 24, 24)
RED = (178, 34, 34)
TEAL = (14, 110, 110)
WHITE = (255, 255, 255)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap returning a list of lines."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, color, max_w, leading):
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=color)
        y += leading
    return y


def star(draw, cx, cy, r, color):
    import math
    pts = []
    for i in range(10):
        ang = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.45
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    draw.polygon(pts, fill=color)


def burst(draw, cx, cy, r, color):
    import math
    pts = []
    for i in range(16):
        ang = i * math.pi / 8
        rr = r if i % 2 == 0 else r * 0.42
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    draw.polygon(pts, fill=color)


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---- masthead ----
d.rectangle([0, 0, W, 148], fill=NAVY)
d.rectangle([0, 148, W, 154], fill=GOLD)
d.text((512, 26), "THE WORLD IN ONE PICTURE", font=font(SERIF_B, 58),
       fill=WHITE, anchor="ma")
d.text((512, 96), "SATURDAY  •  21 NOVEMBER 2026", font=font(SANS_B, 30),
       fill=GOLD, anchor="ma")

# ---- lead story: Mexico captures El Chapo Isidro ----
d.rectangle([28, 176, 620, 470], outline=NAVY, width=3)
d.rectangle([28, 176, 620, 214], fill=NAVY2)
d.text((44, 182), "LEAD  •  MEXICO", font=font(SANS_B, 24), fill=GOLD)
star(d, 588, 195, 15, GOLD)
d.text((44, 226), "MEXICO CAPTURES", font=font(SERIF_B, 40), fill=INK)
d.text((44, 274), "\u2018EL CHAPO ISIDRO\u2019", font=font(SERIF_B, 40), fill=RED)
para(d, 44, 332, "FBI most-wanted cartel boss Fausto Isidro Meza Flores "
     "seized in Sinaloa with US help. Gunfire erupts after the arrest.",
     font(SANS, 23), INK, 540, 30)
d.polygon([(44, 466), (180, 436), (300, 466)], fill=(196, 164, 120))
d.polygon([(230, 466), (380, 430), (530, 466)], fill=(168, 132, 88))

# ---- story 2: Kryvyi Rih ----
d.rectangle([644, 176, 996, 470], outline=NAVY, width=3)
d.rectangle([644, 176, 996, 214], fill=RED)
d.text((660, 182), "WAR  •  UKRAINE", font=font(SANS_B, 24), fill=WHITE)
burst(d, 962, 195, 14, (255, 176, 66))
d.text((660, 226), "DOUBLE-TAP STRIKE", font=font(SERIF_B, 27), fill=INK)
d.text((660, 260), "ON ZELENSKYY\u2019S", font=font(SERIF_B, 27), fill=INK)
d.text((660, 294), "HOMETOWN", font=font(SERIF_B, 27), fill=INK)
para(d, 660, 342, "Russian ballistic missiles hit Kryvyi Rih, killing a "
     "boy of 7 and a woman of 20; 60 wounded.",
     font(SANS, 21), INK, 320, 28)

# ---- story 3: COP31 overtime ----
d.rectangle([28, 494, 496, 706], outline=NAVY, width=3)
d.rectangle([28, 494, 496, 530], fill=TEAL)
d.text((44, 500), "CLIMATE  •  COP31, ANTALYA", font=font(SANS_B, 22), fill=WHITE)
d.ellipse([448, 500, 478, 530], outline=WHITE, width=3)
d.arc([456, 508, 470, 522], 200, 340, fill=WHITE, width=3)
d.text((44, 542), "CLIMATE TALKS RUN", font=font(SERIF_B, 29), fill=INK)
d.text((44, 576), "INTO OVERTIME", font=font(SERIF_B, 29), fill=INK)
para(d, 44, 622, "No deal yet in Antalya as talks run past the deadline; "
     "fossil fuels still missing from the draft text.",
     font(SANS, 21), INK, 436, 27)

# ---- story 4: Poland ----
d.rectangle([520, 494, 996, 706], outline=NAVY, width=3)
d.rectangle([520, 494, 996, 530], fill=NAVY2)
d.text((536, 500), "EUROPE  •  POLAND", font=font(SANS_B, 22), fill=GOLD)
d.polygon([(954, 500), (966, 512), (954, 524), (942, 512)], fill=RED)
d.ellipse([949, 507, 959, 517], fill=WHITE)
d.text((536, 542), "MISSILES LAND", font=font(SERIF_B, 29), fill=INK)
d.text((536, 576), "ON NATO SOIL", font=font(SERIF_B, 29), fill=INK)
para(d, 536, 622, "Warsaw calls Russian weapons crashing into Poland an "
     "\u2018intentional provocation\u2019 after the biggest November barrage.",
     font(SANS, 21), INK, 436, 27)

# ---- story 5: Peru quake ----
d.rectangle([28, 730, 496, 910], outline=NAVY, width=3)
d.rectangle([28, 730, 496, 766], fill=(96, 60, 20))
d.text((44, 736), "EARTH  •  PERU", font=font(SANS_B, 22), fill=WHITE)
for r in (8, 13):
    d.arc([448 - r, 748 - r, 448 + r, 748 + r], 0, 360,
          fill=WHITE, width=3)
d.ellipse([444, 744, 452, 752], fill=RED)
d.text((44, 778), "MAGNITUDE 6.7 QUAKE", font=font(SERIF_B, 27), fill=INK)
d.text((44, 810), "SHAKES PERU", font=font(SERIF_B, 27), fill=INK)
para(d, 44, 852, "A strong earthquake strikes the Jun\u00edn region in the "
     "Andes.", font(SANS, 21), INK, 436, 26)

# ---- story 6: tankers hit off Hormuz ----
d.rectangle([520, 730, 996, 910], outline=NAVY, width=3)
d.rectangle([520, 730, 996, 766], fill=(52, 30, 86))
d.text((536, 736), "GULF  •  STRAIT OF HORMUZ", font=font(SANS_B, 22), fill=GOLD)
d.polygon([(930, 752), (972, 752), (964, 760), (938, 760)], fill=GOLD)
d.line([(951, 752), (951, 738)], fill=GOLD, width=3)
d.line([(951, 738), (963, 742)], fill=GOLD, width=3)
d.text((536, 778), "TWO TANKERS HIT", font=font(SERIF_B, 27), fill=INK)
d.text((536, 810), "OFF HORMUZ", font=font(SERIF_B, 27), fill=INK)
para(d, 536, 852, "Two tankers hit by projectiles off Oman\u2019s Khasab; "
     "Iran says a third struck a mine.", font(SANS, 21), INK, 436, 26)

# ---- footer ticker ----
d.rectangle([0, 930, W, H], fill=NAVY)
d.rectangle([0, 930, W, 936], fill=GOLD)
para(d, 28, 946, "ALSO TODAY  —  Trump weighs new strikes on Iran  •  "
     "Houthi drone halted en route to Riyadh  •  UK\u2013EU reset deal  •  "
     "Funeral boat capsizes in Nigeria as rescuers search on  •  Bayer\u2019s "
     "Roundup deal worth billions", font(SANS_B, 20), WHITE, 968, 26)

img.save("poster.png", optimize=True)
print("saved poster.png", img.size)
