# =========================================================================
# ERWEITERTE GUI
# Bestehende Dialog- und Menütexte werden nicht verändert.
# =========================================================================

init python:
    if "stats_hud" not in config.overlay_screens:
        config.overlay_screens.append("stats_hud")

style matrix_panel:
    background Solid("#10151d")
    padding (16, 12)

style matrix_title:
    size 24
    bold True

style matrix_stat:
    size 18

style matrix_small:
    size 15

style matrix_button:
    xminimum 150
    yminimum 42
    padding (14, 8)

style matrix_choice_button:
    xfill True
    yminimum 58
    padding (18, 12)
    background Solid("#202733")
    hover_background Solid("#354052")
    insensitive_background Solid("#151a22")

style matrix_choice_text:
    size 21
    xalign 0.5
    text_align 0.5

style matrix_say_window:
    background Solid("#0c1016")
    padding (24, 18)

style matrix_say_name:
    size 28
    bold True

style matrix_say_text:
    size 24

screen say(who, what):
    zorder 100
    window:
        id "window"
        style "matrix_say_window"
        xalign 0.5
        yalign 0.96
        xmaximum 1220
        xfill True
        vbox:
            spacing 8
            if who:
                text who:
                    id "who"
                    style "matrix_say_name"
            text what:
                id "what"
                style "matrix_say_text"
                xfill True
            textbutton "Weiter":
                style "matrix_button"
                xalign 1.0
                action Return()
    key "dismiss" action Return()

screen choice(items):
    zorder 110
    frame:
        xalign 0.5
        yalign 0.78
        xmaximum 980
        xfill True
        padding (20, 20)
        background Solid("#0c1016")
        vbox:
            spacing 11
            for item in items:
                if item.action:
                    textbutton item.caption:
                        style "matrix_choice_button"
                        text_style "matrix_choice_text"
                        action item.action
                else:
                    text item.caption:
                        style "matrix_choice_text"
                        xfill True

screen stats_hud():
    zorder 90
    frame:
        style "matrix_panel"
        xalign 0.985
        yalign 0.02
        xminimum 310
        xmaximum 390
        vbox:
            spacing 6
            text "MATRIX STATUS" style "matrix_title" xalign 0.5
            text "[wochentage[aktueller_tag_index]] – [tageszeit]" style "matrix_stat" xalign 0.5
            null height 4
            text "Geld: [geld]$" style "matrix_stat"
            text "Energie: [energie]/[max_energie]" style "matrix_stat"
            null height 4
            text "Sarah  | Beziehung: [sarah_beziehung]" style "matrix_small"
            text "Sarah  | Korruption: [sarah_korruption]" style "matrix_small"
            text "Krause | Beziehung: [krause_beziehung]" style "matrix_small"
            text "Krause | Korruption: [krause_korruption]" style "matrix_small"
            text "Berg   | Beziehung: [berg_beziehung]" style "matrix_small"
            text "Berg   | Korruption: [berg_korruption]" style "matrix_small"
            text "Elena  | Beziehung: [elena_beziehung]" style "matrix_small"
            text "Elena  | Korruption: [elena_korruption]" style "matrix_small"
            null height 5
            textbutton "Spielstatistik":
                style "matrix_button"
                xalign 0.5
                action Show("game_stats")

screen game_stats():
    zorder 200
    modal True
    frame:
        style "matrix_panel"
        xalign 0.5
        yalign 0.5
        xminimum 600
        xmaximum 920
        vbox:
            spacing 10
            text "SPIELSTATISTIK" style "matrix_title" xalign 0.5
            text "Tag: [wochentage[aktueller_tag_index]] | [tageszeit]" style "matrix_stat"
            text "Geld: [geld]$ | Energie: [energie]/[max_energie]" style "matrix_stat"
            null height 5
            text "Sarah – Beziehung [sarah_beziehung] | Korruption [sarah_korruption]" style "matrix_small"
            text "Krause – Beziehung [krause_beziehung] | Korruption [krause_korruption]" style "matrix_small"
            text "Berg – Beziehung [berg_beziehung] | Korruption [berg_korruption]" style "matrix_small"
            text "Elena – Beziehung [elena_beziehung] | Korruption [elena_korruption]" style "matrix_small"
            null height 8
            text "Inventar: [len(inventar)] Gegenstände" style "matrix_stat"
            textbutton "Schließen":
                style "matrix_button"
                xalign 0.5
                action Hide("game_stats")

