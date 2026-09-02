# =========================================================================
# 1. CHARAKTERE DEFINIEREN
# =========================================================================
define m = Character("Max", color="#c8ffc8")
define s = Character("Sarah", color="#ffc8c8")
define k = Character("Frau Krause", color="#e0aaff")
define apo = Character("Apotheker", color="#aaffff")

# Handy-Kontakte
define s_handy = Character("Sarah (SMS)", color="#ffffc8")
define k_handy = Character("Frau Krause (SMS)", color="#f0c8ff")

# =========================================================================
# 2. STATISTIKEN, INVENTAR UND SYSTEM-VARIABLEN
# =========================================================================
default geld = 20
default energie = 100
default tageszeit = "Morgen" # Morgen, Nachmittag, Abend, Nacht

# Wochentage-System
default wochentage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
default aktueller_tag_index = 0 

# Arbeitssperre
default heute_gearbeitet = False

# Inventar-System
default inventar = []

# --- CHARAKTER-WERTE (ZUNEIGUNG, KORRUPTION & STATUS) ---
default sarah_beziehung = 0
default sarah_korruption = 0
default sarah_schwanger = False
default sarah_tage_seit_sex = 0
default sarah_test_verlangt = False
default sarah_test_bestanden = False

default krause_beziehung = 0
default krause_korruption = 0
default krause_schwanger = False
default krause_tage_seit_sex = 0
default krause_test_verlangt = False
default krause_test_bestanden = False

# Story-Flags
default miete_bezahlt = False
default sarah_event_erledigt = False

# Handy-System
default neue_nachrichten_anzahl = 1


# =========================================================================
# 3. SPIELSTART
# =========================================================================
label start:
    m "Ein neues Semester im Wohnheim beginnt. Mal sehen, wohin das alles führt."
    jump wohnheim_flur


# =========================================================================
# 4. HAUPT-HUB (ORTSAUSWAHL)
# =========================================================================
label wohnheim_flur:
    $ tag_name = wochentage[aktueller_tag_index]
    
    # Miet-Check am Sonntagabend durch die Vermieterin
    if tag_name == "Sonntag" and tageszeit == "Abend" and not miete_bezahlt:
        jump krause_miete_event

    # AUTOMATISCHE SCHWANGERSCHAFTSTEST-TRIGGERS (Nach 3 Tagen)
    if sarah_schwanger and sarah_tage_seit_sex >= 3 and not sarah_test_verlangt:
        jump sarah_test_trigger_event

    if krause_schwanger and krause_tage_seit_sex >= 3 and not krause_test_verlangt:
        jump krause_test_trigger_event

    # ZUFÄLLIGES BETTEL-EVENT (Triggert nachts auf dem Flur, wenn Korruption sehr hoch ist)
    if tageszeit == "Nacht" and sarah_korruption >= 35 and renpy.random.randint(1, 100) <= 30:
        jump sarah_bettelt_event

    if tageszeit == "Nacht" and krause_korruption >= 35 and renpy.random.randint(1, 100) <= 30:
        jump krause_bettelt_event

    "Status: [tag_name] ([tageszeit]) | Geld: [geld]$ | Energie: [energie]%%"
    "Mädels-Status:"
    "Sarah - Korruption: [sarah_korruption] | Schwanger: [sarah_schwanger]"
    "Frau Krause - Korruption: [krause_korruption] | Schwanger: [krause_schwanger]"
    
    if energie <= 0:
        "Du bist völlig erschöpft! Du musst dich in deinem Zimmer ausruhen."
        jump mein_zimmer_schlafen

    if sarah_beziehung >= 5 and not sarah_event_erledigt:
        jump sarah_schenkt_geschenk

    if neue_nachrichten_anzahl > 0:
        $ zimmer_button_text = "In mein Zimmer (Handy blinkt!)"
    else:
        $ zimmer_button_text = "In mein Zimmer"

    menu:
        "Wohin möchtest du gehen?"
        
        "[zimmer_button_text]":
            jump mein_zimmer
            
        "In Sarahs Zimmer":
            jump sarahs_zimmer
            
        "In das Büro der Vermieterin":
            jump krause_buero
            
        "In die Gemeinschaftsdusche":
            jump gemeinschaftsdusche
            
        "Zur Apotheke gehen" if tageszeit != "Nacht":
            jump apotheke
            
        "Zum Samstags-Markt gehen" if tag_name == "Samstag" or tag_name == "Sonntag":
            jump wochenend_markt
            
        "Arbeiten gehen (+50$, kostet 40 Energie)" if tageszeit != "Nacht" and not heute_gearbeitet:
            jump arbeiten


# =========================================================================
# 5. ORT: MEIN ZIMMER, SCHLAFEN & HANDY
# =========================================================================
label mein_zimmer:
    "Du bist in deinem Zimmer."
    
    if neue_nachrichten_anzahl > 0:
        $ handy_button_text = "Handy benutzen [" + str(neue_nachrichten_anzahl) + "] NEU"
    else:
        $ handy_button_text = "Handy benutzen"

    menu:
        "[handy_button_text]":
            jump handy_menue
            
        "In den Rucksack schauen (Inventar)":
            jump rucksack_ansehen
        
        "Im Bett schlafen (Energie aufladen & Zeit voranschreiten lassen)":
            jump mein_zimmer_schlafen
            
        "Zurück auf den Flur":
            jump wohnheim_flur

label handy_menue:
    "--- SMARTPHONE ---"
    menu:
        "Posteingang lesen" if neue_nachrichten_anzahl > 0:
            $ neue_nachrichten_anzahl = 0
            s_handy "Hey Max! Komm heute mal in mein Zimmer, wenn du Zeit hast."
            jump handy_menue
            
        "Sarah eine SMS schreiben" if neue_nachrichten_anzahl == 0:
            jump handy_sarah_chat
            
        "Frau Krause eine SMS schreiben" if krause_korruption >= 5:
            jump handy_krause_chat
            
        "Handy weglegen":
            jump mein_zimmer

label handy_sarah_chat:
    menu:
        "Ein Kompliment senden" if sarah_korruption >= 5:
            m "Du hast heute wirklich toll ausgesehen."
            s_handy "Danke, Max... Das ist lieb von dir. Komm mich mal besuchen."
            $ sarah_korruption += 2
            jump handy_menue
        "Zurück":
            jump handy_menue

label handy_krause_chat:
    menu:
        "Ihr eine charmante Nachricht schicken":
            m "Ich muss an unser interessantes Gespräch in Ihrem Büro denken..."
            k_handy "Herr Max, Sie sollten sich auf Ihr Studium konzentrieren! Aber Sie sind sehr aufmerksam. Besuchen Sie mich ruhig wieder."
            $ krause_korruption += 2
            jump handy_menue
        "Zurück":
            jump handy_menue

label rucksack_ansehen:
    if not inventar:
        "Dein Rucksack ist komplett leer."
    else:
        "Im Rucksack befindet sich aktuell:"
        $ index = 0
        while index < len(inventar):
            $ item = inventar[index]
            "- [item]"
            $ index += 1
    jump mein_zimmer

label mein_zimmer_schlafen:
    $ energie = 100
    if tageszeit == "Morgen":
        $ tageszeit = "Nachmittag"
    elif tageszeit == "Nachmittag":
        $ tageszeit = "Abend"
    elif tageszeit == "Abend":
        $ tageszeit = "Nacht"
    else:
        $ tageszeit = "Morgen"
        $ heute_gearbeitet = False
        
        if sarah_korruption >= 25:
            $ sarah_tage_seit_sex += 1
        if krause_korruption >= 25:
            $ krause_tage_seit_sex += 1
            
        $ aktueller_tag_index += 1
        if aktueller_tag_index > 6:
            $ aktueller_tag_index = 0
            $ miete_bezahlt = False
            
    $ tag_name = wochentage[aktueller_tag_index]
    "Du hast geschlafen. Es ist jetzt [tag_name] ([tageszeit])."
    jump wohnheim_flur


# =========================================================================
# 6. ORT: APOTHEKE
# =========================================================================
label apotheke:
    "Du betrittst die Apotheke."
    apo "Wie kann ich Ihnen helfen?"
    menu:
        "Einen Schwangerschaftstest kaufen (-25$)" if geld >= 25:
            $ geld -= 25
            $ inventar.append("Schwangerschaftstest")
            jump wohnheim_flur
        "Die Pille danach kaufen (-40$)" if geld >= 40:
            $ geld -= 40
            $ inventar.append("Pille danach")
            jump wohnheim_flur
        "Zurück":
            jump wohnheim_flur


# =========================================================================
# 7. ORT: SARAHS ZIMMER (INTERAKTION & ERWACHSENEN-MENÜ)
# =========================================================================
label sarahs_zimmer:
    "Du betrittst Sarahs Zimmer."
    
    if sarah_test_verlangt and not sarah_test_bestanden:
        jump sarah_test_abgabe_label

    if tageszeit == "Nacht" and sarah_korruption < 10:
        s "Max? Es ist mitten in der Nacht! Geh bitte..."
        jump wohnheim_flur
    elif tageszeit == "Nacht" and sarah_korruption >= 10:
        s "Max... Schön, dass du dich nachts zu mir schleichst..."
        if sarah_test_bestanden:
            jump sarah_schwanger_sex_menue
        else:
            jump sarah_erwachsenen_menue
    else:
        if sarah_test_bestanden:
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
        "Die Kleidung komplett ablegen und schmutzig ficken" if sarah_korruption >= 25:
            jump sarah_vollsex_szene
        "Ihre enge Kehrseite nehmen (Anal)" if sarah_korruption >= 35:
            jump sarah_anal_szene
        "Ihr Zimmer verlassen":
            jump wohnheim_flur

label sarah_ausziehen_szene:
    m "Zieh das Top aus. Ich will deine Brüste sehen."
    s "Na gut, wenn du so heiß darauf bist..."
    "Sie wirft ihr Oberteil weg. Du greifst ihre nackten Brüste, knetest das pralle Fleisch fest mit den Händen und fängst an, gierig an ihren harten Nippeln zu saugen und ihre Titten komplett nass zu lecken."
    s "Ah... Max, ja! Saug fester an meinen Zitzen... das treibt mich um den Verstand..."
    $ sarah_korruption += 5
    $ energie -= 20
    jump sarah_erwachsenen_menue

label sarah_blowjob_szene:
    "Sarah kniet sich vor dich hin und holt deinen harten Schwanz aus der Hose. Sie leckt einmal von unten bis zur Eichel an ihm hoch."
    "Sie öffnet weit ihren feuchten Mund, umschließt deine Eichel und saugt deinen Riemen tief bis zum Anschlag in ihren Hals."
    s "Mmh.. mhh.."
    "Du packst ihre Haare fest und stößt rhythmisch tief in ihren Mund, während sie dich gierig mit Speichel bedeckt."
    menu:
        "In ihren Mund abspritzen und schlucken lassen":
            "Du stöhnst laut auf, stößt tief in ihren Hals und spritzt deine dicke, weiße Ladung Sperma direkt in ihren Mund. Sie schluckt alles gierig runter und streckt dir ihre weiße Zunge entgegen."
            s "Mmh, lecker... Ich liebe deinen warmen Saft, Max. Das ist so ein toller Geschmack."
            $ sarah_korruption += 8
            $ energie -= 25
            jump mein_zimmer_schlafen
        "Auf ihre Titten abspritzen (Nicht schlucken)":
            "Du ziehst deinen Schwanz im letzten Moment aus ihrem Mund und spritzt dein ganzes Sperma in dicken Fontänen über ihre prallen Brüste."
            s "Oh ja... Schau dir an, wie viel Saft du hast, Max! Ich liebe es, wenn du mich so einsaust."
            $ sarah_korruption += 5
            $ energie -= 25
            jump mein_zimmer_schlafen

label sarah_vollsex_szene:
    "Alle Kleider fliegen weg. Du saugst wild an ihren Brüsten, während deine Finger ihre nasse Fotze massieren."
    s "Ficke mich jetzt, Max! Ramm ihn ganz tief in mich rein!"
    "Du drückst ihre Beine weit auseinander, setzt an ihrer triefenden Muschi am und rammst deinen harten Schwanz mit einem heftigen Stoß ganz tief in sie hinein."
    "Das feuchte, klatschende Geräusch eurer Körper erfüllt den Raum. Du ziehst ihn fast ganz heraus und schiebst ihn direkt wieder bis zum Anschlag rein."
    s "Ohhh Gott, ja! Ficke meine geile Fotze härter! Ramm ihn bis an meine Gebärmutter!"
    "Du packst ihre Hüften und vögelst sie immer schneller durch. Ihr enges Fleisch umschließt dich heiß."
    menu:
        "Rausziehen und auf ihr Gesicht abspritzen":
            "Kurz vor dem Orgasmus ziehst du deinen Schwanz mit einem Ruck aus ihrer Fotze und spritzt deine klebrige Ladung Sperma komplett über ihr Gesicht."
            s "Mmh... das war so verdammt geil, Max. Schau dir die Sauerei an."
            $ sarah_korruption += 5
            $ energie -= 45
            jump mein_zimmer_schlafen
        "Voll in ihr abspritzen (Sperma in die Fotze pumpen!)":
            s "Nein, zieh nicht raus! Spritz in mir ab! Mach mich schwanger, Max! Füll meine Fotze ganz mit deinem Samen!"
            "Du bleibst ganz tief in ihr drin, drückst dich fest gegen ihr Becken und feuerst Stoß um Stoß deines warmen Spermas direkt in ihre Gebärmutter."
            s "Ahhh Max! Ja, pump mich voll! Ich will dein Kind in mir tragen!"
            "Du ziehst deinen schlaffen Riemen langsam heraus. Dein weißer Saft läuft ihr in dicken Tropfen aus der gedehnten Fotze."
            $ sarah_schwanger = True
            $ sarah_tage_seit_sex = 0
            $ sarah_korruption += 25
            $ energie -= 50
            jump mein_zimmer_schlafen

label sarah_anal_szene:
    "Du drehst Sarah auf den Bauch, sodass ihr knackiger Arsch vor dir aufragt."
    "Du spuckst auf deinen Schwanz, reibst ihre Rosette ein und drückst deine Eichel langsam, aber kraftvoll in ihr enges Poloch hinein."
    s "Ahhh! Max, das ist so enge! Aber ja... ramm ihn mir in den Arsch! Ficke meine enge Rosette!"
    "Du hältst sie fest an den Hüften und schiebst ihn ganz rein. Du ziehst ihn raus und rammst ihn rücksichtslos wieder tief in ihren Anus."
    s "Ohhh ja, ficke meinen Arsch härter! Zerstör mich!"
    "Nach unzähligen harten Stößen ziehst du ihn heraus und feuerst deine dicke Ladung komplett über ihre Pobacken."
    $ sarah_korruption += 20
    $ energie -= 45
    jump mein_zimmer_schlafen

label sarah_schwanger_sex_menue:
    s "Max... seit ich schwanger von dir bin, bin ich noch viel unartiger und geiler geworden. Ficke deinen ungeborenen Nachwuchs tief in mir durch!"
    menu:
        "Deine schwangere Mitbewohnerin intensiv durchvögeln":
            "Du ziehst sie nackt aus. Ihre Brüste sind durch die Schwangerschaft noch schwerer geworden. Du leckst ihre Nippel und drückst sie aufs Bett."
            "Du schiebst deinen harten Schwanz langsam und tief in ihre kochend heiße, schwangere Fotze rein."
            "Euer ganzer Körper bewegt sich im Rhythmus, während du den Schwanz rein- und rausziehst."
            s "Ahhh, Max! Ja! Ficke mich und dein Baby! Ramm ihn ganz tief rein, füll mich wieder mit deinem heißem Sperma auf!"
            "Du feuerst eine gigantische Ladung Samen direkt vor den Muttermund ihrer schwangeren Spalte."
            $ sarah_korruption += 10
            $ energie -= 45
            jump mein_zimmer_schlafen
        "Ihr Zimmer verlassen":
            jump wohnheim_flur

label krause_buero:
    "Du betrittst das Büro von Frau Krause."
    if krause_test_verlangt and not krause_test_bestanden:
        jump krause_test_abgabe_label
    if tageszeit == "Nacht" and krause_korruption < 10:
        k "Herr Max? Raus hier!"
        jump wohnheim_flur
    elif tageszeit == "Nacht" and krause_korruption >= 10:
        k "Ah, Max... Ich habe gehofft, dass du dich zu mir schleichst..."
        if krause_test_bestanden:
            jump krause_schwanger_sex_menue
        else:
            jump krause_erwachsenen_menue
    else:
        if krause_test_bestanden:
            k "Guten Tag, Vater meines ungeborenen Kindes. Setzen Sie sich, Max."
        else:
            k "Guten Tag, Max. Geht es um Ihre Wohnung oder die Miete?"
        menu:
            "Ihr die 'Pille danach' geben" if "Pille danach" in inventar and krause_tage_seit_sex == 1 and not krause_test_bestanden:
                $ inventar.remove("Pille danach")
                k "Oh, Gott sei Dank, Max."
                $ krause_schwanger = False
                $ krause_tage_seit_sex = 0
                jump wohnheim_flur
            "Ihr Komplimente machen":
                $ krause_beziehung += 2
                $ krause_korruption += 1
                jump wohnheim_flur
            "Zurück":
                jump wohnheim_flur

label krause_erwachsenen_menue:
    menu:
        "Ihre Bluse öffnen und sie liebkosen" if krause_korruption >= 12:
            "Du öffnest ihre Bluse und saugst gierig an ihren großen, schweren Brüsten, während du ihre reifen Zitzen nass leckst."
            k "Ohhh, Max... ja, saug an meinen Titten! Nimm sie!"
            $ krause_korruption += 5
            $ energie -= 25
            jump krause_erwachsenen_menue
        "Ein tiefer Blowjob am Schreibtisch" if krause_korruption >= 20:
            "Frau Krause schiebt ihren Bürostuhl zurück und kniet sich im engen Rock vor dich hin."
            "Sie nimmt deinen harten Riemen komplett in den Mund und saugt ihn rhythmisch ab, während sie dich von unten ansieht."
            k "Mmh... du schmeckst so gut, Max..."
            "Du packst sie am Hinterkopf und stößt tief in ihren reifen Mund."
            menu:
                "In ihren Mund abspritzen und schlucken lassen":
                    "Du feuerst dein Sperma tief in ihren Hals. Sie schluckt jeden Tropfen der heißen Wichse brav hinunter."
                    k "Puh, brave Jungs belohnen ihre Vermieterin... Das war köstlich."
                    $ krause_korruption += 8
                    $ energie -= 20
                    jump mein_zimmer_schlafen
                "In ihr Gesicht spritzen (Nicht schlucken)":
                    "Du ziehst ihn raus und spritzt der Vermieterin deine Ladung quer über die Wangen und Lippen."
                    k "Oh, du ungezogener Bengel! Das gibt eine Mietminderung im Geist... Schau mich an!"
                    $ krause_korruption += 5
                    $ energie -= 20
                    jump mein_zimmer_schlafen
        "Das Büro verlassen":
            jump wohnheim_flur

label krause_schwanger_sex_menue:
    k "Max... Wer hätte gedacht, dass ich von meinem eigenen Mieter schwanger werde?"
    menu:
        "Das Büro verlassen":
            jump wohnheim_flur

label gemeinschaftsdusche:
    "Du betrittst die feuchten Gemeinschaftsduschen des Wohnheims."
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

label dusche_sarah_event:
    "Du öffnest den Vorhang. Sarah steht nackt unter dem warmen Wasser."
    s "Max! Oh... komm rein zu mir..."
    menu:
        "Sie nackt an die Fliesen drücken und ficken":
            "Du ziehst deine Sachen aus und drückst Sarah mit dem Gesicht an die nassen Fliesen."
            if sarah_test_bestanden:
                s "Ahhh, Max! Ja! Deine schwangere Mitbewohnerin will dich."
            else:
                s "Ahhh, Max! Ja! Komm näher."
            $ sarah_schwanger = True
            $ sarah_tage_seit_sex = 0
            $ sarah_korruption += 15
            $ energie -= 40
            jump mein_zimmer_schlafen
        "Gehen":
            jump wohnheim_flur

label dusche_krause_event:
    "Du hörst Wasser laufen. Frau Krause steht in der Kabine und wäscht ihren Körper."
    k "Herr Max? Oh... Schauen Sie nicht so..."
    menu:
        "Die Vermieterin unter der Dusche nehmen":
            "Du steigst zu ihr in die Kabine. Die Szene endet mit einer gemeinsamen, einvernehmlichen Begegnung."
            if krause_test_bestanden:
                k "Max, Sie sind wirklich ungezogen."
            else:
                k "Max, Sie bringen mich noch um den Verstand."
            $ krause_schwanger = True
            $ krause_tage_seit_sex = 0
            $ krause_korruption += 15
            $ energie -= 40
            jump mein_zimmer_schlafen
        "Gehen":
            jump wohnheim_flur

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

label sarah_bettelt_event:
    "Du bist nachts auf dem Flur. Plötzlich öffnet sich Sarahs Tür."
    if sarah_test_bestanden:
        s "Max... Bitte komm rein zu mir."
    else:
        s "Max... Ich kann nicht schlafen. Komm bitte rein."
    menu:
        "Ihr Flehen erhören":
            if sarah_test_bestanden:
                jump sarah_schwanger_sex_menue
            else:
                jump sarah_vollsex_szene
        "Sie ignorieren":
            "Du lässt sie stehen. Sie jammert leise."
            jump wohnheim_flur

label krause_bettelt_event:
    "Frau Krause kommt nachts die Treppe herunter."
    if krause_test_bestanden:
        k "Max... Ich brauche dich bei mir."
    else:
        k "Max... Ich halte es in meinem Bett nicht mehr aus."
    menu:
        "Die Vermieterin begleiten":
            $ krause_schwanger = True
            $ krause_tage_seit_sex = 0
            $ krause_korruption += 10
            jump mein_zimmer_schlafen
        "Sie wegschicken":
            jump wohnheim_flur

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
            s "Oh mein Gott, Max... Es hat wirklich geklappt! Ich bekomme dein Kind!"
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
            k "Ich fass es nicht... Ich bin schwanger von meinem Studenten!"
            $ krause_test_bestanden = True
            jump wohnheim_flur
        "Sagen, dass du noch keinen hast":
            jump wohnheim_flur

label krause_miete_event:
    k "Max! Es ist Sonntagabend. Ich brauche die wöchentliche Miete von 40$."
    menu:
        "Miete bar bezahlen (-40$)" if geld >= 40:
            $ geld -= 40
            $ miete_bezahlt = True
            jump wohnheim_flur
        "Die Miete durch Gefälligkeiten abgelten" if krause_korruption >= 8:
            "Sie zwinkert dir zu und vertröstet dich auf ein nächtliches Treffen im Büro."
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
