# =========================================================================
# 7b. SARAHS ZIMMER – ERWEITERTE EVENTS
# =========================================================================

label sarah_zimmer_erweitert:
    if tageszeit == "Nacht" and sarah_korruption < 10:
        s "Max? Es ist mitten in der Nacht! Geh bitte..."
        jump wohnheim_flur
    elif tageszeit == "Nacht" and sarah_korruption >= 10:
        if sarah_korruption >= 50:
            jump sarah_submission_menue
        elif sarah_test_bestanden:
            jump sarah_schwanger_sex_menue
        else:
            jump sarah_erwachsenen_menue
    else:
        if sarah_korruption >= 50:
            s "Guten Morgen, mein Master. Was kann ich heute für dich tun?"
        elif sarah_test_bestanden:
            s "Oh Max! Unserem Baby geht es gut. Ich merke richtig, wie sich mein Körper verändert..."
        else:
            s "Oh, hey Max! Was gibt's?"
        menu:
            "Ihr die 'Pille danach' geben" if "Pille danach" in inventar and sarah_tage_seit_sex == 1 and not sarah_test_bestanden:
                $ inventar.remove("Pille danach")
                s "Oh danke, Max! Jetzt bin ich erleichtert."
                $ sarah_schwanger = False
                $ sarah_tage_seit_sex = 0
                jump wohnheim_flur
            "Mit ihr unterhalten (-10 Energie)":
                $ energie -= 10
                $ sarah_beziehung += 1
                jump wohnheim_flur
            "Zurück":
                jump wohnheim_flur

label sarah_erwachsenen_menue:
    menu:
        "Ihr Top ausziehen und an den Brüsten saugen" if sarah_korruption >= 12:
            jump sarah_ausziehen_szene
        "Einen tiefen Blowjob fordern" if sarah_korruption >= 20:
            jump sarah_blowjob_szene
        "Die Kleidung komplett ablegen und ficken" if sarah_korruption >= 25:
            jump sarah_vollsex_szene
        "Ihre enge Kehrseite nehmen (Anal)" if sarah_korruption >= 35:
            jump sarah_anal_szene
        "Ihr Zimmer verlassen":
            jump wohnheim_flur

label sarah_submission_menue:
    s "Ich stehe vollkommen unter deiner Kontrolle, Master Max. Sag mir einfach, wie du deine Sklavin heute benutzen willst."
    menu:
        "Ihr befehlen, sich nackt auf den Boden zu knien (Gehorsams-Check)":
            $ gehorsam_roll = renpy.random.randint(1, 100) + (sarah_korruption - 50)
            if gehorsam_roll >= 40:
                "Sarah zieht ohne zu zögern ihre Kleidung aus und kniet sich mit gesenktem Blick vor dich hin."
                s "Wie du wünschst, Master. Ich bin dein gehorsames Spielzeug."
                $ sarah_korruption += 5
                jump sarah_erwachsenen_menue
            else:
                s "Master... bitte nicht jetzt. Ich... ich schäme mich noch etwas..."
                jump wohnheim_flur
        "Zurück":
            jump wohnheim_flur

label sarah_ausziehen_szene:
    m "Zieh das Top aus. Ich will deine Brüste sehen."
    s "Na gut, wenn du so heiß darauf bist..."
    "Sie wirft ihr Oberteil weg. Du greifst ihre nackten Brüste, knetest das pralle Fleisch fest mit den Händen und fängst an, gierig an ihren harten Nippeln zu saugen."
    $ sarah_korruption += 5
    $ energie -= 20
    jump sarah_erwachsenen_menue

label sarah_blowjob_szene:
    "Sarah kniet sich vor dich hin und holt deinen harten Schwanz aus der Hose."
    "Sie öffnet weit ihren feuchten Mund, umschließt deine Eichel und saugt deinen Riemen tief bis zum Anschlag in ihren Hals."
    menu:
        "In ihren Mund abspritzen und schlucken lassen":
            "Du stöhnst laut auf, stößt tief in ihren Hals und spritzt deine dicke Ladung Sperma direkt in ihren Mund. Sie schluckt alles gierig runter."
            $ sarah_korruption += 8
            $ energie -= 25
            jump mein_zimmer_schlafen
        "Auf ihre Titten abspritzen":
            "Du ziehst deinen Schwanz im letzten Moment aus ihrem Mund und spritzt dein ganzes Sperma über ihre prallen Brüste."
            $ sarah_korruption += 5
            $ energie -= 25
            jump mein_zimmer_schlafen

label sarah_vollsex_szene:
    "Alle Kleider fliegen weg. Du drückst ihre Beine weit auseinander, setzt an ihrer triefenden Muschi an und rammst deinen harten Schwanz ganz tief in sie hinein."
    s "Ohhh Gott, ja! Ficke meine geile Fotze härter! Ramm ihn bis an meine Gebärmutter!"
    menu:
        "Rausziehen und auf ihr Gesicht abspritzen":
            "Kurz vor dem Orgasmus ziehst du deinen Schwanz mit einem Ruck aus ihrer Fotze und spritzt deine klebrige Ladung Sperma komplett über ihr Gesicht."
            $ sarah_korruption += 5
            $ energie -= 45
            jump mein_zimmer_schlafen
        "Voll in ihr abspritzen (Sperma in die Fotze pumpen!)":
            s "Nein, zieh nicht raus! Spritz in mir ab! Mach mich schwanger, Max!"
            "Du bleibst ganz tief in ihr drin und feuerst Stoß um Stoß deines warmen Spermas direkt in ihre Gebärmutter."
            $ sarah_schwanger = True
            $ sarah_tage_seit_sex = 0
            $ sarah_korruption += 25
            $ energie -= 50
            jump mein_zimmer_schlafen

label sarah_anal_szene:
    "Du drehst Sarah auf den Bauch. Du spuckst auf deinen Schwanz und drückst deine Eichel langsam, aber kraftvoll in ihr enges Poloch hinein."
    "Nach unzähligen harten Stößen ziehst du ihn heraus und feuerst deine dicke Ladung komplett über ihre Pobacken."
    $ sarah_korruption += 20
    $ energie -= 45
    jump mein_zimmer_schlafen

label sarah_schwanger_sex_menue:
    s "Max... seit ich schwanger von dir bin, bin ich noch viel unartiger und geiler geworden. Ficke deinen ungeborenen Nachwuchs tief in mir durch!"
    menu:
        "Deine schwangere Mitbewohnerin intensiv durchvögeln":
            "Du schiebst deinen harten Schwanz langsam und tief in ihre kochend heiße, schwangere Fotze rein."
            $ sarah_korruption += 10
            $ energie -= 45
            jump mein_zimmer_schlafen
        "Ihr Zimmer verlassen":
            jump wohnheim_flur

# =========================================================================
# 8. ORT: BÜRO DER VERMIETERIN
# =========================================================================

label krause_buero:
    "Du betrittst das Büro von Frau Krause."

    if krause_test_verlangt and not krause_test_bestanden:
        jump krause_test_abgabe_label

    if tageszeit == "Nacht" and krause_korruption < 10:
        k "Herr Max? Raus hier!"
        jump wohnheim_flur
    elif tageszeit == "Nacht" and krause_korruption >= 10:
        if krause_korruption >= 50:
            jump krause_submission_menue
        elif krause_test_bestanden:
            jump krause_schwanger_sex_menue
        else:
            jump krause_erwachsenen_menue
    else:
        menu:
            "Ihr Komplimente machen":
                $ krause_beziehung += 2
                $ krause_korruption += 1
                jump wohnheim_flur
            "Zurück":
                jump wohnheim_flur

label krause_erwachsenen_menue:
    menu:
        "Ihre Bluse öffnen und sie liebkosen" if krause_korruption >= 12:
            "Du öffnest ihre Bluse und saugst gierig an ihren großen, schweren Brüsten."
            $ krause_korruption += 5
            $ energie -= 25
            jump krause_erwachsenen_menue
        "Die reife Vermieterin schmutzig auf dem Schreibtisch flachlegen" if krause_korruption >= 25:
            "Du hebst die Vermieterin auf den großen Holzschreibtisch, breitest ihre Beine weit aus und rammst deinen Schwanz tief in ihre feuchte Fotze rein."
            menu:
                "In der Vermieterin abspritzen":
                    "Du bleibst ganz tief in ihr drin und pumpst deine heiße Ladung Sperma komplett in ihr Inneres."
                    $ krause_schwanger = True
                    $ krause_tage_seit_sex = 0
                    $ krause_korruption += 25
                    $ energie -= 45
                    jump mein_zimmer_schlafen
                "Zurück":
                    jump krause_erwachsenen_menue
        "Das Büro verlassen":
            jump wohnheim_flur

label krause_submission_menue:
    k "Mein ganzer Stolz gehört ab jetzt dir, Max. Sag mir einfach, wie sich deine ältere Sklavin heute nützlich machen kann."
    menu:
        "Ihr befehlen, den Schreibtisch komplett freizuräumen (Gehorsams-Check)":
            $ gehorsam_roll = renpy.random.randint(1, 100) + (krause_korruption - 50)
            if gehorsam_roll >= 45:
                "Frau Krause fegt alle Akten vom Tisch und beugt sich willig nach vorne."
                $ krause_korruption += 5
                jump krause_erwachsenen_menue
            else:
                k "Herr Max... ich habe hier wichtige Dokumente. Ich kann das nicht tun..."
                jump wohnheim_flur
        "Zurück":
            jump wohnheim_flur

label krause_schwanger_sex_menue:
    k "Max... Wer hätte gedacht, dass ich von meinem eigenen Mieter schwanger werde? Mein Körper verlangt jetzt erst recht nach deinem harten Schwanz."
    menu:
        "Die schwangere Vermieterin wild auf dem Schreibtisch flachlegen":
            "Du schiebst deinen Riemen tief in ihre schwangere, nasse Fotze und spritzt dein ganzes Sperma kochend heiß tief in sie rein."
            $ krause_korruption += 10
            $ energie -= 45
            jump mein_zimmer_schlafen
        "Das Büro verlassen":
            jump wohnheim_flur

# =========================================================================
# 8b. ORT: UNIVERSITÄT (CHARAKTER: FRAU BERG)
# =========================================================================

label universitaet:
    "Du betrittst das Universitätsgebäude und gehst zum Büro deiner Dozentin, Frau Berg."

    if berg_test_verlangt and not berg_test_bestanden:
        jump berg_test_abgabe_label

    if berg_korruption >= 25 and tageszeit == "Nachmittag":
        jump berg_erwachsenen_menue
    else:
        b "Guten Tag, Max. Haben Sie Fragen zu der Vorlesung oder Ihrer Hausarbeit?"
        menu:
            "Mit ihr über das Studium sprechen (-10 Energie)":
                $ energie -= 10
                $ berg_beziehung += 2
                "Ihr führt ein langes, interessantes akademisches Gespräch."
                jump wohnheim_flur
            "Ihr ein charmantes Kompliment machen":
                b "Herr Max! Solche Bemerkungen gehören sich nicht... Aber danke."
                $ berg_korruption += 2
                jump wohnheim_flur
            "Zurück zum Wohnheim":
                jump wohnheim_flur

label berg_erwachsenen_menue:
    b "Max... schließen Sie bitte die Bürotür ab. Ich kann mich nicht auf die Korrekturen konzentrieren, wenn Sie so vor mir stehen..."
    menu:
        "Ihre Bluse aufknöpfen und an den Brüsten saugen" if berg_korruption >= 25:
            "Du öffnest ihre elegante Bluse. Du greifst ihre festen Brüste und saugst gierig an ihren Nippeln."
            $ berg_korruption += 5
            $ energie -= 20
            jump universitaet
        "Die Lehrerin direkt auf dem Schreibtisch flachlegen" if berg_korruption >= 45:
            "Du hebst Frau Berg auf den Schreibtisch, schiebst ihren Rock hoch und rammst deinen harten Schwanz tief in ihre nasse Fotze."
            b "Oh Gott, Max! Ficke deine Lehrerin härter! Ramm ihn ganz tief in mich rein!"
            menu:
                "Tief in der Lehrerin abspritzen (Sperma reinpumpen!)":
                    b "Ja! Spritz in mir ab! Mach mich schwanger, Max!"
                    "Du pumpst deine heiße Ladung direkt an ihren Muttermund."
                    $ berg_schwanger = True
                    $ berg_tage_seit_sex = 0
                    $ berg_korruption += 25
                    $ energie -= 50
                    jump mein_zimmer_schlafen
                "Zurück":
                    jump berg_erwachsenen_menue
        "Das Büro verlassen":
            jump wohnheim_flur

# =========================================================================
# 8c. ORT: SPORTSTUDIO (FITNESSSTUDIO)
# =========================================================================

label sportstudio:
    "Du betrittst das moderne Sportstudio. Hier klirren die Hanteln und die Musik wummert."

    if tageszeit == "Nachmittag" and berg_korruption >= 15 and renpy.random.randint(1, 100) <= 50:
        "An den Cardiogeräten entdeckst du deine Lehrerin, Frau Berg, in einem engen Sport-Outfit."
        jump sportstudio_berg_begegnung

    menu:
        "Ein intensives Krafttraining absolvieren (-30$ Gebühr, -40 Energie)" if geld >= 30:
            $ geld -= 30
            $ energie -= 40
            $ max_energie += 10
            "Du ziehst das Training knallhart durch. Deine Muskeln brennen, aber deine maximale Energie ist permanent gestiegen! Max. Energie: [max_energie]"
            jump wohnheim_flur
        "Zurück zum Wohnheim":
            jump wohnheim_flur

label sportstudio_berg_begegnung:
    b "Oh, Hallo Max! Sie trainieren also auch hier? Schön, dass Sie sich fit halten."
    "Ihr enges Oberteil betont ihre Kurven perfekt. Sie wischt sich den Schweiß von der Stirn."
    menu:
        "Ihr beim Training assistieren und Komplimente machen":
            "Du hilfst ihr bei den Gewichten und suchst bewusst Körperkontakt."
            b "Vielen Dank, Max. Sie sind wirklich sehr aufmerksam und stark..."
            $ berg_beziehung += 3
            $ berg_korruption += 3
            jump wohnheim_flur
        "Ihr ein Handtuch reichen und dich normal unterhalten":
            "Ihr plaudert entspannt über Fitness und Sportgeräte."
            $ berg_beziehung += 2
            jump wohnheim_flur
        "Gehen":
            jump wohnheim_flur

# =========================================================================
# 9. ORT: GEMEINSCHAFTSDUSCHE
# =========================================================================

label gemeinschaftsdusche:
    "Du betrittst die feuchten Gemeinschaftsduschen des Wohnheims."

    if (tag_name == "Samstag" or tag_name == "Sonntag") and tageszeit == "Nachmittag" and sarah_korruption >= 30 and krause_korruption >= 30:
        jump dusche_threesome_event

    if tageszeit == "Nachmittag" or tageszeit == "Abend":
        menu:
            "Nachsehen, wer unter der Dusche steht":
                $ wurf = renpy.random.randint(1, 2)
                if wurf == 1 and sarah_korruption >= 20:
                    jump dusche_sarah_event
                elif wurf == 2 and krause_korruption >= 20:
                    jump dusche_krause_event
                else:
                    "Die Duschen sind im Moment leer."
                    jump wohnheim_flur
            "Zurück":
                jump wohnheim_flur
    else:
        "Es ist niemand in den Duschen."
        jump wohnheim_flur

label dusche_threesome_event:
    "Du öffnest den großen Duschvorhang und traust deinen Augen nicht."
    "Sarah und die Vermieterin Frau Krause stehen gemeinsam komplett nackt unter dem herabprallenden warmen Wasser."
    s "Oh, Max! Schau mal, wer mich hier beim Waschen besucht hat... Komm doch direkt rein zu uns!"
    k "Herr Max... wir haben gerade über die Hausordnung gesprochen. Aber unter diesem warmen Wasser gelten andere Regeln. Schnappen Sie sich uns beide!"
    "Du ziehst deine Sachen blitzschnell aus und steigst zu den beiden Frauen in die große Duschkabine."
    "Das Wasser prallt auf eure Körper nieder. Du packst dir Sarah von hinten, während Frau Krause sich vor dich kniet und deinen Riemen mit den Händen massiert."
    s "Ahhh, Max! Ja, nimm mich fest von hinten unter der Dusche!"
    k "Sehr gut, Max! Verwöhne die junge Sarah, während ich mich um deinen Unterkörper kümmere!"
    "Nach einem intensiven, gemeinsamen Erlebnis drückst du beide Frauen eng an die nassen Fliesen."
    menu:
        "Das Sperma gleichmäßig auf beide Frauen verteilen":
            "Du ziehst dich zurück und verteilst deine dicke Ladung Sperma komplett über die nackten Körper der beiden Frauen. Das Wasser wäscht den weißen Saft langsam von ihren Brüsten."
            s "Das war unglaublich, Max..."
            k "Ein fantastisches Erlebnis, Herr Max. Die Miete ist für diese Woche vergessen."
            $ sarah_korruption += 15
            $ krause_korruption += 15
            $ miete_bezahlt = True
            $ energie -= 50
            jump mein_zimmer_schlafen
        "Zurück auf den Flur":
            jump wohnheim_flur

label dusche_sarah_event:
    "Du öffnest den Vorhang. Sarah steht nackt unter dem warmen Wasser."
    "Du drückst Sarah an die nassen Fliesen und schiebst deinen harten Schwanz von hinten tief in ihre nasse Fotze hinein."
    $ sarah_schwanger = True
    $ sarah_tage_seit_sex = 0
    $ sarah_korruption += 15
    $ energie -= 40
    jump mein_zimmer_schlafen

label dusche_krause_event:
    "Frau Krause steht komplett nackt in der Kabine und wäscht ihren reifen Körper."
    "Du steigst nackt zu ihr in die Kabine und rammst deinen harten Schwanz tief in sie hinein."
    $ krause_schwanger = True
    $ krause_tage_seit_sex = 0
    $ krause_korruption += 15
    $ energie -= 40
    jump mein_zimmer_schlafen

# =========================================================================
# 10. SYSTEM: ARBEITEN
# =========================================================================

label arbeiten:
    $ geld += 50
    $ energie -= 40
    $ heute_gearbeitet = True
    "Du hast im Cafe gejobbt. +50$, -40 Energie."
    if tageszeit == "Morgen":
        $ tageszeit = "Nachmittag"
    elif tageszeit == "Nachmittag":
        $ tageszeit = "Abend"
    else:
        $ tageszeit = "Nacht"
    jump wohnheim_flur

# =========================================================================
# 11. ZUFÄLLIGE BETTEL-EVENTS
# =========================================================================

label sarah_bettelt_event:
    "Du bist nachts auf dem Flur. Plötzlich öffnet sich Sarahs Tür."
    s "Max... meine Muschi ist so heiß und nass... Bitte komm rein und ficke mich! Ich bettle dich an, mach mich schwanger!"
    menu:
        "Ihr Flehen erhören und sie im Bett durchvögeln":
            jump sarah_vollsex_szene
        "Sie ignorieren":
            jump wohnheim_flur

label krause_bettelt_event:
    "Frau Krause kommt nachts im transparenten Morgenmantel die Treppe herunter."
    k "Max... Ich brauche deinen harten Schwanz! Ficke die alte Vermieterin, ramm ihn tief rein und mach mich schwanger!"
    menu:
        "Die Vermieterin auf dem Flurboden flachlegen":
            "Du reißt ihren Mantel auf und pumpst dein ganzes Sperma kochend heiß tief in sie rein."
            $ krause_schwanger = True
            $ krause_tage_seit_sex = 0
            $ krause_korruption += 10
            jump mein_zimmer_schlafen
        "Sie wegschicken":
            jump wohnheim_flur

# =========================================================================
# 12. SCHWANGERSCHAFTSTEST-STORY EVENTS
# =========================================================================

label sarah_test_trigger_event:
    $ sarah_test_verlangt = True
    s "Max... meine Tage sind überfällig und mir ist so schlecht. Bitte besorge mir sofort einen Schwangerschaftstest!"
    jump wohnheim_flur

label sarah_test_abgabe_label:
    s "Hast du den Schwangerschaftstest, Max?"
    menu:
        "Ihr den Test geben" if "Schwangerschaftstest" in inventar:
            $ inventar.remove("Schwangerschaftstest")
            "Der Test zeigt zwei deutliche Streifen: POSITIV."
            s "Oh mein Gott, Max... Es hat wirklich geklappt! Du hast mich schwanger gefickt!"
            $ sarah_test_bestanden = True
            jump wohnheim_flur
        "Sagen, dass du noch keinen hast":
            jump wohnheim_flur

label krause_test_trigger_event:
    $ krause_test_verlangt = True
    k "Max... wir haben ein Problem. Mir ist speiübel. Besorge mir unauffällig einen Schwangerschaftstest!"
    jump wohnheim_flur

label krause_test_abgabe_label:
    k "Haben Sie den Test besorgt, Max?"
    menu:
        "Ihr den Test geben" if "Schwangerschaftstest" in inventar:
            $ inventar.remove("Schwangerschaftstest")
            "Der Test ist glasklar POSITIV."
            $ krause_test_bestanden = True
            jump wohnheim_flur
        "Sagen, dass du noch keinen hast":
            jump wohnheim_flur

label berg_test_trigger_event:
    $ berg_test_verlangt = True
    b "Max... ich bin im Unterricht fast in Ohnmacht gefallen und meine Periode bleibt aus. Besorgen Sie mir sofort einen Test!"
    jump wohnheim_flur

label berg_test_abgabe_label:
    b "Haben Sie den Schwangerschaftstest für mich, Max?"
    menu:
        "Ihr den Test geben" if "Schwangerschaftstest" in inventar:
            $ inventar.remove("Schwangerschaftstest")
            "Der Test ist POSITIV."
            b "Oh mein Gott... Ich bin schwanger von meinem eigenen Studenten! Max, ich trage dein Kind unter meinem Herzen!"
            $ berg_test_bestanden = True
            jump wohnheim_flur
        "Sagen, dass du noch keinen hast":
            jump wohnheim_flur

# =========================================================================
# 13. WEITERE EVENTS
# =========================================================================

label krause_miete_event:
    k "Max! Es ist Sonntagabend. Ich brauche die wöchentliche Miete von 40$."
    menu:
        "Miete bar bezahlen (-40$)" if geld >= 40:
            $ geld -= 40
            $ miete_bezahlt = True
            jump wohnheim_flur
        "Sagen, dass du kein Geld hast":
            $ krause_beziehung -= 3
            $ miete_bezahlt = True
            jump wohnheim_flur

label sarah_schenkt_geschenk:
    s "Hey Max! Hier ist ein bisschen Taschengeld für dich!"
    $ geld += 20
    $ sarah_event_erledigt = True
    jump wohnheim_flur

label wochenend_markt:
    "Du schlenderst über den Markt."
    menu:
        "Ein Parfüm für Sarah kaufen (-15$)" if geld >= 15 and "Parfüm" not in inventar:
            $ geld -= 15
            $ inventar.append("Parfüm")
            jump wohnheim_flur
        "Zurück":
            jump wohnheim_flur
