# Sarah – erster visueller Charakter
# Dieses Modul verändert keine Dialog- oder Menütexte.
# Es verwendet ausschließlich bereits vorhandene PNGs aus game/images/characters/.

# Grundsprite: vorhandener 512x1024-Charakter.
image sarah_visual_base = Transform(
    "images/characters/00015-3563459718.png",
    xysize=(480, 960)
)

# Vorhandene Gesichts-Layer.
image sarah_visual_eyes_closed = Transform(
    "images/characters/eyes_closed.png",
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

image sarah_visual_mouth_smile = Transform(
    "images/characters/mouth_smile.png",
    xysize=(480, 480)
)
image sarah_visual_mouth_smirk = Transform(
    "images/characters/mouth_smirk.png",
    xysize=(480, 480)
)
image sarah_visual_mouth_talk = Transform(
    "images/characters/mouth_talk.png",
    xysize=(480, 480)
)

default sarah_visual_eyes = "wink"
default sarah_visual_mouth = "smile"

transform sarah_visual_base_pos:
    xalign 0.76
    yalign 1.0

transform sarah_visual_face_pos:
    xalign 0.76
    yalign 0.0

screen sarah_visual():
    zorder 0

    add "sarah_visual_base" at sarah_visual_base_pos

    if sarah_visual_eyes == "closed":
        add "sarah_visual_eyes_closed" at sarah_visual_face_pos
    elif sarah_visual_eyes == "ahegao":
        add "sarah_visual_eyes_ahegao" at sarah_visual_face_pos
    else:
        add "sarah_visual_eyes_wink" at sarah_visual_face_pos

    if sarah_visual_mouth == "smirk":
        add "sarah_visual_mouth_smirk" at sarah_visual_face_pos
    elif sarah_visual_mouth == "talk":
        add "sarah_visual_mouth_talk" at sarah_visual_face_pos
    else:
        add "sarah_visual_mouth_smile" at sarah_visual_face_pos

init python:
    def _sarah_visual_label_callback(label_name, abnormal):
        if label_name.startswith("sarah"):
            renpy.show_screen("sarah_visual", _layer="master")
        else:
            renpy.hide_screen("sarah_visual", _layer="master")

    config.label_callbacks.append(_sarah_visual_label_callback)
