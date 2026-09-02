# =========================================================================
# VISUAL DESIGN LAYER
# Preserves all existing dialogue and menu strings.
# =========================================================================

image bg_room = "images/backgrounds/room.svg"
image bg_park = "images/backgrounds/park.svg"
image bg_university = "images/backgrounds/university.svg"

init python:
    # Use the new vector artwork without changing any script text.
    gui.main_menu_background = "gui/main_menu.svg"
    gui.game_menu_background = "images/backgrounds/room.svg"

    def _design_label_callback(label_name, jumped):
        """Select a visual backdrop when entering major locations."""
        backgrounds = {
            "wohnheim_flur": "bg_room",
            "mein_zimmer": "bg_room",
            "mein_zimmer_schlafen": "bg_room",
            "sarahs_zimmer": "bg_room",
            "krause_buero": "bg_room",
            "apotheke": "bg_room",
            "sportstudio": "bg_room",
            "gemeinschaftsdusche": "bg_room",
            "stadtkirche": "bg_room",
            "wochenend_markt": "bg_room",
            "arbeiten": "bg_room",
            "universitaet": "bg_university",
            "stadtpark": "bg_park",
        }
        image_name = backgrounds.get(label_name)
        if image_name:
            renpy.scene()
            renpy.show(image_name, layer="master")

    config.label_callbacks.append(_design_label_callback)

# Polished visual defaults. These are style-only and do not alter script text.
style matrix_panel:
    background Frame(Solid("#09111cdd"), 18, 18)
    outlines [(1, "#ffffff18", 0, 0)]
    padding (18, 14)

style matrix_title:
    color "#ffffff"
    size 25
    bold True

style matrix_stat:
    color "#e7eef8"
    size 18

style matrix_small:
    color "#b9c7d8"
    size 15

style matrix_button:
    background Frame(Solid("#1c2a3bdd"), 12, 12)
    hover_background Frame(Solid("#31516ddd"), 12, 12)
    insensitive_background Frame(Solid("#111924cc"), 12, 12)
    xminimum 170
    yminimum 42
    padding (14, 8)
    text_color "#dce8f7"
    text_hover_color "#ffffff"

style matrix_choice_button:
    background Frame(Solid("#0a1320e8"), 16, 16)
    hover_background Frame(Solid("#29465ee8"), 16, 16)
    insensitive_background Frame(Solid("#0a1018cc"), 16, 16)
    xfill True
    yminimum 58
    padding (18, 12)

style matrix_choice_text:
    color "#edf4ff"
    hover_color "#ffffff"
    size 21
    xalign 0.5
    text_align 0.5

style matrix_say_window:
    background Frame(Solid("#070d16ee"), 22, 22)
    padding (28, 20)
    outlines [(1, "#ffffff18", 0, 0)]

style matrix_say_name:
    color "#ffffff"
    size 29
    bold True

style matrix_say_text:
    color "#f2f6fb"
    size 24
    line_spacing 3
