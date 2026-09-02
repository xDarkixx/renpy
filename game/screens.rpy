# =========================================================================
# MATRIX DESIGN / GUI
# Bestehende Dialog- und Menütexte werden nicht verändert.
# Visuelles Redesign: moderne Neon-/Glass-Optik, Status-HUD und Icons.
# =========================================================================

init python:
    if "stats_hud" not in config.overlay_screens:
        config.overlay_screens.append("stats_hud")

style matrix_panel:
    background Solid("#101923e6")
    padding (18, 16)

style matrix_title:
    size 25
    bold True
    color "#7ff7d4"

style matrix_stat:
    size 18
    color "#eef7ff"

style matrix_small:
    size 15
    color "#b9c8d6"

style matrix_button:
    xminimum 170
    yminimum 44
    padding (16, 9)
    background Solid("#172533")
    hover_background Solid("#244052")
    insensitive_background Solid("#111820")
    xalign 0.5

style matrix_button_text:
    size 18
    color "#dffcff"
    hover_color "#7ff7d4"
    xalign 0.5

style matrix_choice_button:
    xfill True
    yminimum 58
    padding (18, 12)
    background Solid("#17222de8")
    hover_background Solid("#234051f2")
    insensitive_background Solid("#121820e8")

style matrix_choice_text:
    size 21
    color "#f1f7fb"
    hover_color "#7ff7d4"
    insensitive_color "#71808d"
    xalign 0.5
    text_align 0.5

style matrix_say_window:
    background Solid("#0b1219f2")
    padding (26, 20)

style matrix_say_name:
    size 28
    bold True
    color "#7ff7d4"

style matrix_say_text:
    size 24
    color "#f5f8fa"

screen say(who, what):
    zorder 100

    # Sarah bekommt hier ihren vorhandenen PNG-Sprite plus Gesichts-Layer.
    # Dadurch wird die bisherige Sarah-SVG nicht zusätzlich angezeigt.
    if who == "Sarah" or who == "Sarah (SMS)":
        add "sarah_visual_base" at sarah_visual_base_pos

        if sarah_visual_eyes == "closed":
            add "sarah_visual_eyes_closed" at sarah_visual_face_pos
        elif sarah_visual_eyes == "ahegao":
            add "sarah_visual_eyes_ahegao" at sarah_visual_face_pos
        else:
            add "sarah_visual_eyes_wink" at sarah_visual_face_pos

        if sarah_visual_mouth == "pout":
            add "sarah_visual_mouth_pout" at sarah_visual_face_pos
        elif sarah_visual_mouth == "smirk":
            add "sarah_visual_mouth_smirk" at sarah_visual_face_pos
        elif sarah_visual_mouth == "talk":
            add "sarah_visual_mouth_talk" at sarah_visual_face_pos
        else:
            add "sarah_visual_mouth_smile" at sarah_visual_face_pos
    elif who and matrix_character_for(who):
        add expression matrix_character_for(who) at matrix_character_sprite

    window:
        id "window"
        style "matrix_say_window"
        xalign 0.5
        yalign 0.965
        xmaximum 1220
        xfill True
        vbox:
            spacing 9
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
                text_style "matrix_button_text"
                xalign 1.0
                action Return()
    key "dismiss" action Return()

screen choice(items):
    zorder 110
    frame:
        xalign 0.5
        yalign 0.77
        xmaximum 1000
        xfill True
        padding (20, 20)
        background Solid("#0b1219ed")
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
        yalign 0.025
        xminimum 330
        xmaximum 410
        has vbox
        spacing 7

        text "MATRIX STATUS" style "matrix_title" xalign 0.5
        text "[wochentage[aktueller_tag_index]] – [tageszeit]" style "matrix_stat" xalign 0.5
        null height 5

        hbox:
            spacing 9
            add "gui/icon_money.svg" at matrix_icon
            vbox:
                spacing 0
                text "Geld" style "matrix_small"
                text "[geld]$" style "matrix_stat"

        hbox:
            spacing 9
            add "gui/icon_energy.svg" at matrix_icon
            vbox:
                spacing 0
                text "Energie" style "matrix_small"
                text "[energie]/[max_energie]" style "matrix_stat"

        null height 4
        text "BEZIEHUNGEN" style "matrix_small" xalign 0.5
        text "Sarah  | Beziehung: [sarah_beziehung]" style "matrix_small"
        text "Sarah  | Korruption: [sarah_korruption]" style "matrix_small"
        text "Krause | Beziehung: [krause_beziehung]" style "matrix_small"
        text "Krause | Korruption: [krause_korruption]" style "matrix_small"
        text "Berg   | Beziehung: [berg_beziehung]" style "matrix_small"
        text "Berg   | Korruption: [berg_korruption]" style "matrix_small"
        text "Elena  | Beziehung: [elena_beziehung]" style "matrix_small"
        text "Elena  | Korruption: [elena_korruption]" style "matrix_small"
        text "Agnes  | Beziehung: [agnes_beziehung]" style "matrix_small"
        text "Agnes  | Korruption: [agnes_korruption]" style "matrix_small"
        null height 5
        textbutton "Spielstatistik":
            style "matrix_button"
            text_style "matrix_button_text"
            xalign 0.5
            action Show("game_stats")

transform matrix_icon:
    zoom 0.45
    yalign 0.5

screen game_stats():
    zorder 200
    modal True
    add "gui/matrix_bg.svg" alpha 0.96
    frame:
        style "matrix_panel"
        xalign 0.5
        yalign 0.5
        xminimum 640
        xmaximum 930
        vbox:
            spacing 11
            text "SPIELSTATISTIK" style "matrix_title" xalign 0.5
            text "Tag: [wochentage[aktueller_tag_index]] | [tageszeit]" style "matrix_stat"
            text "Geld: [geld]$ | Energie: [energie]/[max_energie]" style "matrix_stat"
            null height 5
            text "Sarah – Beziehung [sarah_beziehung] | Korruption [sarah_korruption]" style "matrix_small"
            text "Krause – Beziehung [krause_beziehung] | Korruption [krause_korruption]" style "matrix_small"
            text "Berg – Beziehung [berg_beziehung] | Korruption [berg_korruption]" style "matrix_small"
            text "Elena – Beziehung [elena_beziehung] | Korruption [elena_korruption]" style "matrix_small"
            text "Agnes – Beziehung [agnes_beziehung] | Korruption [agnes_korruption]" style "matrix_small"
            null height 8
            text "Inventar: [len(inventar)] Gegenstände" style "matrix_stat"
            textbutton "Schließen":
                style "matrix_button"
                text_style "matrix_button_text"
                xalign 0.5
                action Hide("game_stats")
