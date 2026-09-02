# ============================================================
# STATISTIKEN
# ============================================================

default geld = 20
default energie = 100
default tageszeit = "Morgen"

default wochentage = [
    "Montag",
    "Dienstag",
    "Mittwoch",
    "Donnerstag",
    "Freitag",
    "Samstag",
    "Sonntag"
]

default aktueller_tag_index = 0
default heute_gearbeitet = False
default inventar = []

# Sarah
default sarah_beziehung = 0
default sarah_korruption = 0
default sarah_schwanger = False
default sarah_tage_seit_sex = 0
default sarah_test_verlangt = False
default sarah_test_bestanden = False

# Frau Krause
default krause_beziehung = 0
default krause_korruption = 0
default krause_schwanger = False
default krause_tage_seit_sex = 0
default krause_test_verlangt = False
default krause_test_bestanden = False

# Story
default miete_bezahlt = False
default sarah_event_erledigt = False
default neue_nachrichten_anzahl = 1

# Tatsächliche Ereignis-Flags
default sarah_ereignis_aktiv = False
default krause_ereignis_aktiv = False


# ============================================================
# CHARAKTERE
# ============================================================

define m = Character("Max", color="#c8ffc8")
define s = Character("Sarah", color="#ffc8c8")
define k = Character("Frau Krause", color="#e0aaff")
define apo = Character("Apotheker", color="#aaffff")

define s_handy = Character("Sarah (SMS)", color="#ffffc8")
define k_handy = Character("Frau Krause (SMS)", color="#f0c8ff")


# ============================================================
# START
# ============================================================

label start:

    m "Ein neues Semester im Wohnheim beginnt."
    m "Mal sehen, wohin das alles führt."

    jump wohnheim_flur


# ============================================================
# HAUPT-HUB
# ============================================================

label wohnheim_flur:

    $ tag_name = wochentage[aktueller_tag_index]

    # Sonntagabend: Miete
    if tag_name == "Sonntag" and tageszeit == "Abend" and not miete_bezahlt:
        jump krause_miete_event

    # Sarah-Test
    if sarah_schwanger and sarah_tage_seit_sex >= 3 and not sarah_test_verlangt:
        jump sarah_test_trigger_event

    # Krause-Test
    if krause_schwanger and krause_tage_seit_sex >= 3 and not krause_test_verlangt:
        jump krause_test_trigger_event

    # Erschöpfung
    if energie <= 0:
        "Du bist völlig erschöpft."
        jump mein_zimmer_schlafen

    "----------------------------------------"
    "Tag: [tag_name]"
    "Tageszeit: [tageszeit]"
    "Geld: [geld]$"
    "Energie: [energie]%"
    "----------------------------------------"

    "Sarah – Beziehung: [sarah_beziehung]"
    "Sarah – Status: [sarah_korruption]"

    "Frau Krause – Beziehung: [krause_beziehung]"
    "Frau Krause – Status: [krause_korruption]"

    if neue_nachrichten_anzahl > 0:
        $ zimmer_button_text = "Mein Zimmer (Handy: [neue_nachrichten_anzahl] neu)"
    else:
        $ zimmer_button_text = "Mein Zimmer"

    menu:

        "[zimmer_button_text]":
            jump mein_zimmer

        "Sarah besuchen":
            jump sarahs_zimmer

        "Büro der Vermieterin":
            jump krause_buero

        "Gemeinschaftsdusche":
            jump gemeinschaftsdusche

        "Apotheke" if tageszeit != "Nacht":
            jump apotheke

        "Samstags-Markt" if tag_name == "Samstag" or tag_name == "Sonntag":
            jump wochenend_markt

        "Arbeiten (+50$, -40 Energie)" if tageszeit != "Nacht" and not heute_gearbeitet:
            jump arbeiten


# ============================================================
# MEIN ZIMMER
# ============================================================

label mein_zimmer:

    "Du bist in deinem Zimmer."

    if neue_nachrichten_anzahl > 0:
        $ handy_button_text = "Handy benutzen ([neue_nachrichten_anzahl] neu)"
    else:
        $ handy_button_text = "Handy benutzen"

    menu:

        "[handy_button_text]":
            jump handy_menue

        "Rucksack":
            jump rucksack_ansehen

        "Schlafen":
            jump mein_zimmer_schlafen

        "Zurück":
            jump wohnheim_flur


# ============================================================
# HANDY
# ============================================================

label handy_menue:

    "--- SMARTPHONE ---"

    menu:

        "Posteingang lesen" if neue_nachrichten_anzahl > 0:

            $ neue_nachrichten_anzahl = 0

            s_handy "Hey Max! Komm heute mal in mein Zimmer, wenn du Zeit hast."

            jump handy_menue

        "Sarah schreiben":

            jump handy_sarah_chat

        "Frau Krause schreiben" if krause_korruption >= 5:

            jump handy_krause_chat

        "Handy weglegen":

            jump mein_zimmer


label handy_sarah_chat:

    menu:

        "Kompliment senden":

            m "Du hast heute wirklich toll ausgesehen."

            s_handy "Danke, Max. Das ist lieb von dir."

            $ sarah_korruption += 2

            jump handy_menue

        "Zurück":

            jump handy_menue


label handy_krause_chat:

    menu:

        "Nachricht schicken":

            m "Ich muss an unser interessantes Gespräch in Ihrem Büro denken."

            k_handy "Sie sollten sich auf Ihr Studium konzentrieren, Herr Max."

            $ krause_korruption += 2

            jump handy_menue

        "Zurück":

            jump handy_menue


# ============================================================
# INVENTAR
# ============================================================

label rucksack_ansehen:

    if not inventar:

        "Dein Rucksack ist leer."

    else:

        "Im Rucksack befindet sich:"

        $ index = 0

        while index < len(inventar):

            $ item = inventar[index]

            "- [item]"

            $ index += 1

    jump mein_zimmer


# ============================================================
# SCHLAFEN / ZEIT
# ============================================================

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

        # Nur echte aktive Ereignisse zählen
        if sarah_ereignis_aktiv:
            $ sarah_tage_seit_sex += 1

        if krause_ereignis_aktiv:
            $ krause_tage_seit_sex += 1

        # Nächster Tag
        $ aktueller_tag_index += 1

        if aktueller_tag_index > 6:

            $ aktueller_tag_index = 0
            $ miete_bezahlt = False

    $ tag_name = wochentage[aktueller_tag_index]

    "Du hast geschlafen."
    "Es ist jetzt [tag_name] ([tageszeit])."

    jump wohnheim_flur


# ============================================================
# APOTHEKE
# ============================================================

label apotheke:

    "Du betrittst die Apotheke."

    apo "Wie kann ich Ihnen helfen?"

    menu:

        "Schwangerschaftstest kaufen (-25$)" if geld >= 25:

            $ geld -= 25
            $ inventar.append("Schwangerschaftstest")

            "Du hast einen Schwangerschaftstest gekauft."

            jump wohnheim_flur

        "Pille danach kaufen (-40$)" if geld >= 40:

            $ geld -= 40
            $ inventar.append("Pille danach")

            "Du hast das Medikament gekauft."

            jump wohnheim_flur

        "Zurück":

            jump wohnheim_flur


# ============================================================
# SARAH
# ============================================================

label sarahs_zimmer:

    "Du betrittst Sarahs Zimmer."

    if sarah_test_verlangt and not sarah_test_bestanden:

        jump sarah_test_abgabe_label

    if tageszeit == "Nacht" and sarah_korruption < 10:

        s "Max? Es ist mitten in der Nacht. Bitte komm morgen wieder."

        jump wohnheim_flur

    s "Oh, hey Max! Was gibt's?"

    menu:

        "Mit Sarah unterhalten (-10 Energie)":

            $ energie = max(0, energie - 10)
            $ sarah_beziehung += 1

            s "Das war schön. Danke, dass du vorbeigekommen bist."

            jump wohnheim_flur

        "Zurück":

            jump wohnheim_flur


# ============================================================
# MÖGLICHE TEST-TRIGGER
# ============================================================

label sarah_test_trigger_event:

    $ sarah_test_verlangt = True

    s "Max, ich glaube, wir sollten einen Schwangerschaftstest machen."

    jump wohnheim_flur


label krause_test_trigger_event:

    $ krause_test_verlangt = True

    k "Herr Max, wir sollten die Situation überprüfen."

    jump wohnheim_flur


# ============================================================
# TEST-ABGABE
# ============================================================

label sarah_test_abgabe_label:

    if "Schwangerschaftstest" not in inventar:

        s "Bitte besorge zuerst einen Schwangerschaftstest."

        jump wohnheim_flur

    $ inventar.remove("Schwangerschaftstest")
    $ sarah_test_bestanden = True

    s "Danke, Max. Jetzt wissen wir mehr."

    jump wohnheim_flur


# ============================================================
# PLACEHOLDER FÜR WEITERE ORTE
# ============================================================

label krause_miete_event:

    k "Herr Max, die Miete ist fällig."

    menu:

        "Miete bezahlen (-20$)" if geld >= 20:

            $ geld -= 20
            $ miete_bezahlt = True

            k "Danke. Damit ist die Miete für diese Woche bezahlt."

            jump wohnheim_flur

        "Später bezahlen":

            k "Dann kümmern Sie sich bitte bald darum."

            jump wohnheim_flur


label krause_buero:

    "Du betrittst das Büro der Vermieterin."

    k "Guten Abend, Herr Max."

    menu:

        "Unterhalten":

            $ krause_beziehung += 1
            $ energie = max(0, energie - 10)

            k "Danke für das Gespräch."

            jump wohnheim_flur

        "Zurück":

            jump wohnheim_flur


label gemeinschaftsdusche:

    "Die Gemeinschaftsdusche ist momentan leer."

    menu:

        "Zurück":

            jump wohnheim_flur


label wochenend_markt:

    "Du besuchst den Wochenend-Markt."

    menu:

        "Zurück":

            jump wohnheim_flur


label arbeiten:

    $ geld += 50
    $ energie = max(0, energie - 40)
    $ heute_gearbeitet = True

    "Du hast gearbeitet."
    "Du erhältst 50$."
    "Du verlierst 40 Energie."

    jump wohnheim_flur