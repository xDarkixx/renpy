# Sarah – visueller Charakter-Layer
# Dieses Modul verändert keine Dialog- oder Menütexte.
# Es wird ausschließlich als Bild-Layer im bestehenden Say-Screen verwendet.

image sarah_visual_base = Transform(
    "images/characters/00015-3563459718.png",
    xysize=(480, 960)
)

# Vorhandene Augen-Layer.
image sarah_visual_eyes_closed = Transform(
    "images/characters/Eyes_closed.png",
    xysize=(480, 480)
)
image sarah_visual_eyes_wink = Transform(
    "images/characters/eyes_wink.png",
    xysize=(480, 480)
)
image sarah_visual_eyes_ahegao = Transform(
    "images/characters/Eyes_Ahegao.png",
    xysize=(480, 480)
)

# Vorhandene Mund-Layer.
image sarah_visual_mouth_pout = Transform(
    "images/characters/Mouth_pout.png",
    xysize=(480, 480)
)
image sarah_visual_mouth_smile = Transform(
    "images/characters/Mouth_smile.png",
    xysize=(480, 480)
)
image sarah_visual_mouth_smirk = Transform(
    "images/characters/Mouth_smirk.png",
    xysize=(480, 480)
)
image sarah_visual_mouth_talk = Transform(
    "images/characters/Mouth_talk.png",
    xysize=(480, 480)
)

default sarah_visual_eyes = "wink"
default sarah_visual_mouth = "smile"

transform sarah_visual_base_pos:
    xalign 0.08
    yalign 1.0
    xmaximum 420
    ymaximum 840
    zoom 0.82

transform sarah_visual_face_pos:
    xalign 0.08
    yalign 0.0
    zoom 0.82
