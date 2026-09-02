# ============================================================
# SPIEL-OBERFLÄCHE / HUD
# Bestehende Texte und Spielwerte bleiben unverändert.
# Nur Darstellung, Abstände und Anordnung wurden verbessert.
# ============================================================

# ------------------------------------------------------------
# Einheitliche GUI-Stile
# ------------------------------------------------------------
style default:
    font "DejaVuSans.ttf"
    size 20

style hud_frame:
    background Frame("gui/frame.png", 18, 18)
    padding (18, 14)

style stats_frame:
    background Frame("gui/frame.png", 22, 22)
    padding (38, 32)

style choice_vbox:
    spacing 14
    xfill True

style choice_button:
    xfill True
    yminimum 58
    padding (22, 14)

style choice_button_text:
    size 22
    xalign 0.5
    text_align 0.5

# ------------------------------------------------------------
# Eigene Darstellung der normalen Auswahlmenüs.
# Die vorhandenen Choice-Texte werden 1:1 aus dem Script übernommen.
# ------------------------------------------------------------
screen choice(items):
    zorder 100

    frame:
        xalign 0.5
        yalign 0.78
        xmaximum 900
        xfill True
        padding (24, 24)

        vbox:
            style "choice_vbox"

            for item in items:
                textbutton item.caption:
                    style "choice_button"
                    action item.action

# ------------------------------------------------------------
# Statistik-HUD
# ------------------------------------------------------------
screen stats_hud():
    zorder 100

    frame:
        style "hud_frame"
        xalign 0.98
        yalign 0.02
        xminimum 285
        xmaximum 360

        vbox:
            spacing 7
            text "[wochentage[aktueller_tag_index]] – [tageszeit]" size 22 xalign 0.5
            null height 5
            text "Geld: [geld]$" size 18
            text "Energie: [energie]%" size 18
            null height 5
            text "Sarah: [sarah_beziehung]" size 17
            text "Krause: [krause_beziehung]" size 17

# ------------------------------------------------------------
# Spielstatistik
# ------------------------------------------------------------
screen game_stats():
    tag menu
    modal True

    frame:
        style "stats_frame"
        xalign 0.5
        yalign 0.5
        xminimum 560
        xmaximum 900

        vbox:
            spacing 12
            text "SPIELSTATISTIK" size 36 xalign 0.5
            null height 5

            hbox:
                spacing 55
                xfill True
                text "Tag: [wochentage[aktueller_tag_index]]" size 20
                text "Tageszeit: [tageszeit]" size 20

            hbox:
                spacing 55
                xfill True
                text "Geld: [geld]$" size 20
                text "Energie: [energie]%" size 20

            null height 10
            text "Sarah" size 25
            text "Beziehung: [sarah_beziehung]" size 18
            text "Status: [sarah_korruption]" size 18
            text "Sarah – Test: [sarah_test_bestanden]" size 18

            null height 7
            text "Frau Krause" size 25
            text "Beziehung: [krause_beziehung]" size 18
            text "Status: [krause_korruption]" size 18
            text "Krause – Test: [krause_test_bestanden]" size 18

            null height 14
            textbutton "Schließen":
                xalign 0.5
                action Hide("game_stats")
