import random
from hirsipuucopy import Hirsipuu

class HirsipuuSovellus:
    def __init__(self) -> None:
        self.puu = Hirsipuu()

    def arvaus(self) -> str:
        while True:
            kirjain = input("kirjain: ")
            if len(kirjain) != 1 or not kirjain.isalpha(): 
                print("debug: virheellinen syöte")
                continue
            return kirjain

    def suorita(self):
        self.puu.alusta_peli()
        max_vaaria_arvauksia = 6
        sanan_pituus = len(self.puu.arvattava_sana)

        while True:
            print("-" * sanan_pituus + "-----") # divideri
            print("SANA:", self.puu.arvattava_sana)
            print("-" * sanan_pituus + "-----") # divideri
            print("debug_print", self.puu.debug_print())

            kirjain = self.arvaus()
            self.puu.arvaa(kirjain)

            print("Oikein arvatut kirjaimet: ", self.puu.oikein_arvatut_kirjaimet)
            print("Väärin arvatut kirjaimet: ", self.puu.vaarin_arvatut_kirjaimet)
            print()
            print("JÄLJELLÄ:", self.puu.jaljella_olevia_kirjaimia)
            print("VÄÄRIÄ:", self.puu.vaaria_arvauksia, "/", max_vaaria_arvauksia)

            if self.puu.vaaria_arvauksia >= max_vaaria_arvauksia:
                print("Game over")
                break
            if self.puu.jaljella_olevia_kirjaimia <= 0:
                print("Voitto tuli")
                break


if __name__ == "__main__":
    sovellus = HirsipuuSovellus
    sovellus().suorita()