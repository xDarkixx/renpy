# =========================================================================
# FEHLENDE LABELS / KOMPATIBILITÄT
# =========================================================================
# Diese Datei ergänzt die im vorhandenen script.rpy angesprungenen Labels,
# ohne den bestehenden script.rpy zu verändern.

label krause_miete_event:
    k "Guten Abend, Max. Die Miete für diese Woche ist noch offen."
    menu:
        "Miete bezahlen (-20$)" if geld >= 20:
            $ geld -= 20
            $ miete_bezahlt = True
            k "Danke. Damit ist die Miete für diese Woche erledigt."
            jump wohnheim_flur
        "Später bezahlen":
            k "Dann kümmern Sie sich bitte bald darum."
            jump wohnheim_flur

label sarah_test_trigger_event:
    s "Max, ich glaube, wir sollten das jetzt überprüfen."
    $ sarah_test_verlangt = True
    jump sarahs_zimmer

label krause_test_trigger_event:
    k "Max, wir sollten die Situation sicherheitshalber überprüfen."
    $ krause_test_verlangt = True
    jump krause_buero

label sarah_test_abgabe_label:
    if "Schwangerschaftstest" in inventar:
        menu:
            "Schwangerschaftstest abgeben":
                $ inventar.remove("Schwangerschaftstest")
                $ sarah_test_verlangt = False
                $ sarah_test_bestanden = True
                s "Danke, Max. Jetzt wissen wir wenigstens, woran wir sind."
                jump wohnheim_flur
            "Noch nicht":
                jump wohnheim_flur
    else:
        s "Du brauchst zuerst einen Schwangerschaftstest aus der Apotheke."
        jump wohnheim_flur

label krause_test_abgabe_label:
    if "Schwangerschaftstest" in inventar:
        menu:
            "Schwangerschaftstest abgeben":
                $ inventar.remove("Schwangerschaftstest")
                $ krause_test_verlangt = False
                $ krause_test_bestanden = True
                k "Danke. Jetzt haben wir Gewissheit."
                jump wohnheim_flur
            "Noch nicht":
                jump wohnheim_flur
    else:
        k "Besorgen Sie bitte zuerst einen Schwangerschaftstest."
        jump wohnheim_flur

label sarah_bettelt_event:
    s "Max, kannst du kurz mit mir reden? Ich brauche deine Hilfe."
    menu:
        "Ihr 10$ geben" if geld >= 10:
            $ geld -= 10
            $ sarah_beziehung += 1
            s "Danke, Max. Das hilft mir wirklich."
            jump wohnheim_flur
        "Ablehnen":
            s "Okay... schon gut."
            jump wohnheim_flur

label krause_bettelt_event:
    k "Max, ich brauche kurz Ihre Unterstützung."
    menu:
        "10$ geben" if geld >= 10:
            $ geld -= 10
            $ krause_beziehung += 1
            k "Danke. Das vergesse ich Ihnen nicht."
            jump wohnheim_flur
        "Ablehnen":
            k "In Ordnung."
            jump wohnheim_flur

label sarah_schenkt_geschenk:
    s "Max, weil du mir in letzter Zeit so oft geholfen hast, habe ich etwas für dich."
    $ inventar.append("Geschenk von Sarah")
    $ sarah_event_erledigt = True
    s "Ich hoffe, es gefällt dir."
    jump wohnheim_flur

label krause_buero:
    "Du betrittst das Büro der Vermieterin."
    k "Was kann ich für Sie tun, Max?"
    if krause_test_verlangt and not krause_test_bestanden:
        jump krause_test_abgabe_label
    menu:
        "Mit Frau Krause sprechen":
            $ krause_beziehung += 1
            $ energie = max(0, energie - 10)
            k "Danke für das Gespräch."
            jump wohnheim_flur
        "Zurück":
            jump wohnheim_flur

label gemeinschaftsdusche:
    "Du gehst zur Gemeinschaftsdusche."
    menu:
        "Duschen und Energie sparen":
            $ energie = min(100, energie + 10)
            "Eine kurze Dusche hilft dir, wieder etwas Energie zu bekommen."
            jump wohnheim_flur
        "Zurück":
            jump wohnheim_flur

label wochenend_markt:
    "Auf dem Wochenend-Markt gibt es verschiedene Angebote."
    menu:
        "Kleinen Einkauf machen (-10$)" if geld >= 10:
            $ geld -= 10
            $ inventar.append("Markteinkauf")
            "Du hast einen kleinen Einkauf gemacht."
            jump wohnheim_flur
        "Nichts kaufen":
            jump wohnheim_flur
        "Zurück":
            jump wohnheim_flur

label arbeiten:
    if energie < 40:
        "Du hast nicht genug Energie zum Arbeiten."
        jump wohnheim_flur
    $ energie -= 40
    $ geld += 50
    $ heute_gearbeitet = True
    "Du hast gearbeitet und 50$ verdient."
    jump wohnheim_flur

label sarah_schwanger_sex_menue:
    # Nicht explizite Kompatibilitätsroute für den vorhandenen Sprung.
    s "Max, lass uns heute einfach etwas Zeit miteinander verbringen."
    menu:
        "Zeit miteinander verbringen (-10 Energie)":
            $ energie = max(0, energie - 10)
            $ sarah_beziehung += 1
            "Ihr verbringt gemeinsam etwas Zeit."
            jump wohnheim_flur
        "Zurück":
            jump wohnheim_flur

label sarah_ausziehen_szene:
    # Nicht explizite Kompatibilitätsroute für den vorhandenen Sprung.
    s "Max, lass uns einen Moment allein verbringen."
    $ sarah_korruption += 2
    $ sarah_beziehung += 1
    $ energie = max(0, energie - 10)
    "Ihr verbringt einen privaten Moment miteinander."
    jump wohnheim_flur
