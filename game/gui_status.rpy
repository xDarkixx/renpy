# =========================================================================
# GUI-STATUS-OVERLAY
# Ergänzt eine kompakte Statusanzeige, ohne vorhandene Dialoge zu ändern.
# =========================================================================

screen renpy_status_hud():
    zorder 100
    frame:
        xalign 0.02
        yalign 0.02
        padding (12, 8)
        background "#111a"

        hbox:
            spacing 14
            text "Tag: [wochentage[aktueller_tag_index]]"
            text "Zeit: [tageszeit]"
            text "Geld: [geld]$"
            text "Energie: [energie]/[max_energie]"

init python:
    if "renpy_status_hud" not in config.overlay_screens:
        config.overlay_screens.append("renpy_status_hud")
