# =========================================================================
# CHARACTER ART LAYER
# Die vorhandenen Dialog- und Menütexte werden nicht verändert.
# Die Sprites werden automatisch anhand des Sprechernamens angezeigt.
# =========================================================================

image char_max = "images/characters/max.svg"
image char_sarah = "images/characters/sarah.svg"
image char_krause = "images/characters/krause.svg"
image char_berg = "images/characters/berg.svg"
image char_elena = "images/characters/elena.svg"
image char_agnes = "images/characters/agnes.svg"
image char_apotheker = "images/characters/apotheker.svg"

init python:
    def matrix_character_for(who):
        if not who:
            return None
        name = who.strip()
        mapping = {
            "Max": "char_max",
            "Sarah": "char_sarah",
            "Sarah (SMS)": "char_sarah",
            "Frau Krause": "char_krause",
            "Frau Krause (SMS)": "char_krause",
            "Frau Berg": "char_berg",
            "Frau Berg (SMS)": "char_berg",
            "Elena": "char_elena",
            "Elena (SMS)": "char_elena",
            "Schwester Agnes": "char_agnes",
            "Schwester Agnes (SMS)": "char_agnes",
            "Apotheker": "char_apotheker",
        }
        return mapping.get(name)

transform matrix_character_sprite:
    xalign 0.08
    yalign 1.0
    xmaximum 420
    ymaximum 700
    zoom 0.82
    alpha 0.96
