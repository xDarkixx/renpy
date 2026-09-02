# =========================================================================
# 1. CHARAKTERE DEFINIEREN
# =========================================================================
define m = Character("Max", color="#c8ffc8")
define s = Character("Sarah", color="#ffc8c8")
define k = Character("Frau Krause", color="#e0aaff")
define b = Character("Frau Berg", color="#ffaa66") 
define el = Character("Elena", color="#ffaad4")
define apo = Character("Apotheker", color="#aaffff")

# Handy-Kontakte
define s_handy = Character("Sarah (SMS)", color="#ffffc8")
define k_handy = Character("Frau Krause (SMS)", color="#f0c8ff")
define b_handy = Character("Frau Berg (SMS)", color="#ffd8aa")

# =========================================================================
# 2. STATISTIKEN, INVENTAR UND SYSTEM-VARIABLEN
# =========================================================================
default geld = 20
default energie = 100
default max_energie = 100 
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
default sarah_traegt_outfit = False

default krause_beziehung = 0
default krause_korruption = 0
default krause_schwanger = False
default krause_tage_seit_sex = 0
default krause_test_verlangt = False
default krause_test_bestanden = False
default krause_traegt_outfit = False

default berg_beziehung = 0
default berg_korruption = 0
default berg_schwanger = False
default berg_tage_seit_sex = 0
default berg_test_verlangt = False
default berg_test_bestanden = False

default elena_beziehung = 0
default elena_korruption = 0
default elena_schwanger = False
default elena_tage_seit_sex = 0
default elena_test_verlangt = False
default elena_test_bestanden = False

# Story-Flags
default miete_bezahlt = False
default sarah_event_erledigt = False
default neue_nachrichten_anzahl = 1


# =========================================================================
# 3. SPIELSTART
# =========================================================================
init python:
    # Hilfsfunktion zum Prüfen von Gegenständen
    def hat_item(item_name):
        return item_name in store.inventar

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

    if berg_schwanger and berg_tage_seit_sex >= 3 and not berg_test_trigger_event:
        jump berg_test_trigger_event

    if elena_schwanger and elena_tage_seit_sex >= 3 and not elena_test_verlangt:
        jump elena_test_trigger_event

    # ZUFÄLLIGES BETTEL-EVENT (Triggert nachts auf dem Flur, wenn Korruption sehr hoch ist)
    if tageszeit == "Nacht" and sarah_korruption >= 35 and renpy.random.randint(1, 100) <= 30:
        jump sarah_bettelt_event

    if tageszeit == "Nacht" and krause_korruption >= 35 and renpy.random.randint(1, 100) <= 30:
        jump krause_bettelt_event

    "Status: [tag_name] ([tageszeit]) | Geld: [geld]$ | Energie: [energie]/[max_energie]"
    "Mädels-Status:"
    "Sarah - Korruption: [sarah_korruption] | Outfit aktiv: [sarah_traegt_outfit]"
    "Frau Krause - Korruption: [krause_korruption] | Outfit aktiv: [krause_traegt_outfit]"
    "Frau Berg (Lehrerin) - Korruption: [berg_korruption]"
    "Elena (Park) - Korruption: [elena_korruption]"
    
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
            
        "Zur Universität gehen" if tageszeit == "Morgen" or tageszeit == "Nachmittag":
            jump universitaet
            
        "Zum Stadtpark gehen (Elena)" if tageszeit == "Nachmittag" or tageszeit == "Abend":
            jump stadtpark
            
        "Zum Sportstudio gehen" if tageszeit == "Nachmittag" or tageszeit == "Abend":
            jump sportstudio
            
        "In die Gemeinschaftsdusche":
            jump gemeinschaftsdusche
            
        "Zur Apotheke gehen" if tageszeit != "Nacht":
            jump apotheke
            
        "Zum Samstags-Markt gehen" if tag_name == "Samstag" or tag_name == "Sonntag":
            jump wochenend_markt
            
        "Arbeiten gehen (+50$, kostet 40 Energie)" if tageszeit != "Nacht" and not heute_gearbeitet:
            jump arbeiten


# =========================================================================
# 5. ORT: MEIN ZIMMER, SCHLAFEN & HANDY-APPS
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
            
        "In den Rucksack schauen (Inventar & Items benutzen)":
            jump rucksack_ansehen
        
        "Im Bett schlafen (Energie aufladen & Zeit voranschreiten lassen)":
            jump mein_zimmer_schlafen
            
        "Zurück auf den Flur":
            jump wohnheim_flur

label handy_menue:
    "--- SMARTPHONE ---"
    menu:
        "Spionage-App (Werte & Maße)":
            "--- BIOMETRISCHE DATENBANK ---"
            "Sarah - Korruption: [sarah_korruption] | Oberweite: 85C"
            "Frau Krause - Korruption: [krause_korruption] | Oberweite: 95E"
            "Frau Berg (Lehrerin) - Korruption: [berg_korruption] | Oberweite: 90D"
            "Elena (Park) - Korruption: [elena_korruption] | Oberweite: 100F"
            jump handy_menue
            
        "SMS-Messenger":
            jump handy_sms_menue
            
        "Online-Shop (Lieferdienst)":
            jump handy_shop_menue
            
        "Amor's Choice (Sex-Shop App)":
            jump handy_sexshop_app
            
        "Handy weglegen":
            jump mein_zimmer

label handy_sms_menue:
    menu:
        "Sarah schreiben":
            m "Hey Sarah, was machst du gerade?"
            s_handy "Hey Max! Bin in meinem Zimmer... komm doch einfach rüber."
            jump handy_sms_menue
        "Frau Krause schreiben":
            m "Guten Abend Frau Krause, alles ruhig im Wohnheim?"
            k_handy "Herr Max, kümmern Sie sich um Ihr Studium! Aber nett, dass Sie fragen."
            jump handy_sms_menue
        "Zurück":
            jump handy_menue

label handy_shop_menue:
    "--- AMAZON & LIEFERDIENST ---"
    menu:
        "Fast-Food bestellen (-15$)" if geld >= 15:
            $ geld -= 15
            $ inventar.append("Essen (Snacks)")
            "Du hast eine Pizza bestellt. Sie wurde diskret vor deine Zimmertür gelegt."
            jump handy_shop_menue
        "Flasche Wodka bestellen (-25$)" if geld >= 25:
            $ geld -= 25
            $ inventar.append("Alkohol (Wodka)")
            "Du hast eine Flasche harten Alkohol im Express-Versand bestellt."
            jump handy_shop_menue
        "Zurück":
            jump handy_menue

# --- NEU: SEX-SHOP APP FÜR SPIELZEUG & OUTFITS ---
label handy_sexshop_app:
    "--- AMOR'S CHOICE (ADULT SHOP) ---"
    menu:
        "Vibrator / Intim-Spielzeug bestellen (-35$)" if geld >= 35:
            $ geld -= 35
            $ inventar.append("Intim-Spielzeug")
            "Erfolgreich bestellt! Ein unauffälliges, neutral verpacktes Paket wird geliefert."
            jump handy_sexshop_app
            
        "Reizwäsche / Knappes Outfit bestellen (-50$)" if geld >= 50:
            $ geld -= 50
            $ inventar.append("Knappes Outfit")
            "Erfolgreich bestellt! Ein diskretes Paket mit heißer Unterwäsche ist auf dem Weg."
            jump handy_sexshop_app
            
        "Zurück":
            jump handy_menue

label rucksack_ansehen:
    if not inventar:
        "Dein Rucksack ist komplett leer."
        jump mein_zimmer
    else:
        "Im Rucksack befindet sich aktuell:"
        $ index = 0
        while index < len(inventar):
            $ item = inventar[index]
            "- [item]"
            $ index += 1
            
        menu:
            "Essen (Snacks) verzehren (+30 Energie)" if "Essen (Snacks)" in inventar:
                $ inventar.remove("Essen (Snacks)")
                $ energie = min(energie + 30, max_energie)
