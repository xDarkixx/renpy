# =========================================================================
# 1. CHARAKTERE DEFINIEREN
# =========================================================================
define m = Character("Max", color="#c8ffc8")
define s = Character("Sarah", color="#ffc8c8")
define k = Character("Frau Krause", color="#e0aaff")
define b = Character("Frau Berg", color="#ffaa66") 
define el = Character("Elena", color="#ffaad4")
define ag = Character("Schwester Agnes", color="#ffffff") 
define apo = Character("Apotheker", color="#aaffff")

# Handy-Kontakte (SMS)
define s_handy = Character("Sarah (SMS)", color="#ffffc8")
define k_handy = Character("Frau Krause (SMS)", color="#f0c8ff")
define b_handy = Character("Frau Berg (SMS)", color="#ffd8aa")
define el_handy = Character("Elena (SMS)", color="#ffd4fa")
define ag_handy = Character("Schwester Agnes (SMS)", color="#e6e6e6")

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

default agnes_beziehung = 0
default agnes_korruption = 0
default agnes_schwanger = False
default agnes_tage_seit_sex = 0
default agnes_test_verlangt = False
default agnes_test_bestanden = False

# --- SAMMLER-FLAGS FÜR TEXT-SELFIES ---
default hat_selfie_sarah = False
default hat_selfie_krause = False
default hat_selfie_berg = False
default hat_selfie_elena = False
default hat_selfie_agnes = False

# Verabredungs-Flags
default verabredung_ort = "Keiner"
default verabredung_wer = "Keine"

# Story-Flags
default miete_bezahlt = False
default sarah_event_erledigt = False
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

    if berg_schwanger and berg_tage_seit_sex >= 3 and not berg_test_trigger_event:
        jump berg_test_trigger_event

    if elena_schwanger and elena_tage_seit_sex >= 3 and not elena_test_verlangt:
        jump elena_test_trigger_event

    if agnes_schwanger and agnes_tage_seit_sex >= 3 and not agnes_test_verlangt:
        jump agnes_test_trigger_event

    "Status: [tag_name] ([tageszeit]) | Geld: [geld]$ | Energie: [energie]/[max_energie]"
    "Mädels-Status:"
    "Sarah - Korruption: [sarah_korruption] | Frau Krause - Korruption: [krause_korruption]"
    "Frau Berg - Korruption: [berg_korruption] | Elena - Korruption: [elena_korruption] | Schwester Agnes - Korruption: [agnes_korruption]"
    
    if energie <= 0:
        "Du bist völlig erschöpft! Du musst dich in deinem Zimmer ausruhen."
        jump mein_zimmer_schlafen

    if neue_nachrichten_anzahl > 0:
        $ zimmer_button_text = "In mein Zimmer (Handy blinkt!)"
    else:
        $ zimmer_button_text = "In mein Zimmer"

    menu:
        "Wohin möchtest du gehen?"
        
        "[zimmer_button_text]":
            jump mein_zimmer
            
        "In Sarahs Zimmer":
            if verabredung_wer == "Sarah" and verabredung_ort == "Zimmer":
                $ verabredung_wer = "Keine"
                $ verabredung_ort = "Keiner"
                "Du betrittst das Zimmer. Sarah erwartet dich bereits sehnsüchtig, genau wie per SMS vereinbart."
                jump sarah_erwachsenen_menue
            jump sarahs_zimmer
            
        "In das Büro der Vermieterin":
            if verabredung_wer == "Krause" and verabredung_ort == "Büro":
                $ verabredung_wer = "Keine"
                $ verabredung_ort = "Keiner"
                "Frau Krause hat das Büro für eure Verabredung bereits von innen verriegelt."
                jump krause_erwachsenen_menue
            jump krause_buero
            
        "Zur Universität gehen" if tageszeit == "Morgen" or tageszeit == "Nachmittag":
            jump universitaet
            
        "Zum Stadtpark gehen (Elena)":
            if verabredung_wer == "Elena" and verabredung_ort == "Park" and tageszeit == "Nachmittag":
                $ verabredung_wer = "Keine"
                $ verabredung_ort = "Keiner"
                "Elena winkt dir bereits hinter den großen Büschen im Park zu."
                jump elena_erwachsenen_menue
            jump stadtpark
            
        "Zur Stadtkirche gehen (Schwester Agnes)" if (tag_name == "Samstag" or tag_name == "Sonntag") and (tageszeit == "Morgen" or tageszeit == "Nachmittag"):
            jump stadtkirche
            
        "Zum Sportstudio gehen" if tageszeit == "Nachmittag" or tageszeit == "Abend":
            jump sportstudio
            
        "In die Gemeinschaftsdusche":
            if verabredung_wer == "Sarah" and verabredung_ort == "Dusche":
                $ verabredung_wer = "Keine"
                $ verabredung_ort = "Keiner"
                "Sarah wartet bereits nackt hinter dem Duschvorhang auf dich."
                jump dusche_sarah_event
            jump gemeinschaftsdusche
            
        "Zur Apotheke gehen" if tageszeit != "Nacht":
            jump apotheke
            
        "Zum Samstags-Markt gehen" if tag_name == "Samstag" or tag_name == "Sonntag":
            jump wochenend_markt
            
        "Arbeiten gehen (+50$, kostet 40 Energie)" if tageszeit != "Nacht" and not heute_gearbeitet:
            jump arbeiten


# =========================================================================
# 5. ORT: MEIN ZIMMER, SCHLAFEN & MULTI-APP SMARTPHONE
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
        "Spionage-App & Galerie":
            "--- BIOMETRISCHE DATENBANK ---"
            "Sarah - Korruption: [sarah_korruption] | Oberweite: 85C"
            "Frau Krause - Korruption: [krause_korruption] | Oberweite: 95E"
            "Frau Berg (Lehrerin) - Korruption: [berg_korruption] | Oberweite: 90D"
            "Elena (Park) - Korruption: [elena_korruption] | Oberweite: 100F"
            "Schwester Agnes - Korruption: [agnes_korruption] | Oberweite: 85D"
            "--- FREIGESCHALTETE TEXT-SELFIES ---"
            if hat_selfie_sarah: "- Sarahs Reizwäsche-Selfie freigeschaltet"
            if hat_selfie_krause: "- Frau Krauses Morgenmantel-Selfie freigeschaltet"
            if hat_selfie_berg: "- Frau Bergs geöffnetes Blusen-Selfie freigeschaltet"
            if hat_selfie_elena: "- Elenas enges Kleid-Selfie freigeschaltet"
            if hat_selfie_agnes: "- Schwester Agnes' abgelegtes Tracht-Selfie freigeschaltet"
            jump handy_menue
            
        "SMS-Messenger & Sexting":
            jump handy_sms_menue
            
        "Online-Shop (Lieferdienst)":
            jump handy_shop_menue
            
        "Amor's Choice (Sex-Shop App)":
            jump handy_sexshop_app
            
        "Handy weglegen":
            jump mein_zimmer

# --- MESSENGER MIT SCHWANGERSCHAFTS-DYNAMIK FÜR SEXTING-ANFRAGEN ---
label handy_sms_menue:
    "--- MESSENGER ---"
    "Aktive Verabredung: [verabredung_wer] -> [verabredung_ort]"
    menu:
        "Sarah (Mitbewohnerin)":
            jump handy_chat_sarah
        "Frau Krause (Vermieterin)" if krause_korruption >= 5:
