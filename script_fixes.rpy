# =========================================================================
# TECHNISCHE FIXES FÜR script.rpy
# Diese Datei ergänzt fehlende Store-Variablen/Charaktere, ohne bestehende
# Dialog- oder Menütexte in script.rpy zu verändern.
# =========================================================================

default hat_selfie_sarah = False
default hat_selfie_krause = False
default hat_selfie_berg = False
default hat_selfie_elena = False

default verabredung_wer = "Keine"
default verabredung_ort = "Keiner"

define el_handy = Character("Elena (SMS)", color="#ffd0e5")

# script.rpy enthält aktuell einen Tippfehler in der Bedingung:
#     not berg_test_trigger_event
# obwohl berg_test_trigger_event ein Label und keine boolesche Variable ist.
# Dieser kleine Proxy sorgt dafür, dass die vorhandene Zeile funktioniert:
# - vor dem Test: False -> das Label wird angesprungen
# - nach test_verlangt: True -> kein erneuter Trigger
init python:
    class BergTestTriggerProxy(object):
        def __bool__(self):
            return store.berg_test_verlangt

        __nonzero__ = __bool__

# Nur als technische Kompatibilität für die fehlerhafte bestehende Bedingung.
default berg_test_trigger_event = BergTestTriggerProxy()
