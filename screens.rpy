# ============================================================
# SPIEL-OBERFLÄCHE / HUD
# Bestehende Texte und Spielwerte bleiben unverändert.
# Nur Darstellung und Anordnung wurden verbessert.
# ============================================================

screen stats_hud():
    zorder 100

    frame:
        xalign 0.98
        yalign 0.02
        xminimum 250
        padding (16, 12)

        vbox:
            spacing 6
            text "[wochentage[aktueller_tag_index]] – [tageszeit]" size 22
            null height 3
            text "Geld: [geld]$" size 18
            text "Energie: [energie]%" size 18
            null height 3
            text "Sarah: [sarah_beziehung]" size 17
            text "Krause: [krause_beziehung]" size 17

screen game_stats():
    tag menu
    modal True

    frame:
        xalign 0.5
        yalign 0.5
        xminimum 520
        padding (35, 30)

        vbox:
            spacing 10
            text "SPIELSTATISTIK" size 36 xalign 0.5
            null height 5

            hbox:
                spacing 45
                text "Tag: [wochentage[aktueller_tag_index]]" size 20
                text "Tageszeit: [tageszeit]" size 20

            hbox:
                spacing 45
                text "Geld: [geld]$" size 20
                text "Energie: [energie]%" size 20

            null height 8
            text "Sarah" size 25
            text "Beziehung: [sarah_beziehung]" size 18
            text "Status: [sarah_korruption]" size 18
            text "Sarah – Test: [sarah_test_bestanden]" size 18

            null height 5
            text "Frau Krause" size 25
            text "Beziehung: [krause_beziehung]" size 18
            text "Status: [krause_korruption]" size 18
            text "Krause – Test: [krause_test_bestanden]" size 18

            null height 12
            textbutton "Schließen" xalign 0.5 action Hide("game_stats")
