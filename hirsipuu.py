import random

class Hirsipuu:
    def __init__(self) -> None:
        self.arvattava_sana = ""
        self.arvatut_kirjaimet = []

        self.alusta_peli()

    def alusta_peli(self):
        """ Lukee sanat tiedostosta listaan ja tallentaa satunnaisen sanan listasta arvattava_sana muuttujaan """
        sanat = []
        with open("kaikkisanat.txt", "r", encoding="utf-8") as tiedosto:
            for rivi in tiedosto:
                sanat.append(rivi.strip())
        
        self.arvattava_sana = random.choice(sanat)

    def __str__(self):
        return f"{self.arvattava_sana}"

# debuggausta varten
"""
if True:
    hp = Hirsipuu()
    print(hp)
"""