# ============================================================
# EINFACHE SPIEL-OBERFLÄCHE
# ============================================================

screen stats_hud():
    zorder 100

    frame:
        xalign 0.98
        yalign 0.02
        padding (12, 8)

        vbox:
            spacing 3
            text "[wochentage[aktueller_tag_index]] – [tageszeit]"
            text "Geld: [geld]$"
            text "Energie: [energie]%"
            text "Sarah: [sarah_beziehung]"
            text "Krause: [krause_beziehung]"

screen game_stats():
    tag menu

    frame:
        xalign 0.5
        yalign 0.5
        padding (30, 25)

        vbox:
            spacing 8
            text "SPIELSTATISTIK" size 34
            text "Tag: [wochentage[aktueller_tag_index]]"
            text "Tageszeit: [tageszeit]"
            text "Geld: [geld]$"
            text "Energie: [energie]%"
            null height 8
            text "Sarah – Beziehung: [sarah_beziehung]"
            text "Sarah – Status: [sarah_korruption]"
            text "Sarah – Test: [sarah_test_bestanden]"
            text "Frau Krause – Beziehung: [krause_beziehung]"
            text "Frau Krause – Status: [krause_korruption]"
            text "Krause – Test: [krause_test_bestanden]"
            null height 8
            textbutton "Schließen" action Hide("game_stats")
