from hirsipuu import Hirsipuu
import os
import platform

class HirsipuuSovellus:
    def __init__(self) -> None:
        self.puu = Hirsipuu()
        self.__voittosana = ""
    
    def tyhjenna_naytto(self):
        """ Tyhjentää konsolin järjestelmästä riippumatta """
        os_nimi = platform.system()
        if os_nimi == "Windows":
            os.system("cls")
        else:
            os.system("clear")

    def tulosta_sana(self, sana: str):
        """ Tulostaa arvatut kirjaimet sekä tyhjän paikan arvaamattomille """
        for kirjain in sana:
            if kirjain in self.puu.oikein_arvatut_kirjaimet:
                print(kirjain, " ", end="")
            else:
                print("_ ", end="")

    # TODO: tämä toimimaan
    def tulosta_highscore(self):
        highscores = self.puu.lue_highscore()
        print(highscores)

    def arvaus(self) -> str:
        while True:
            kirjain = input("kirjain: ")
            if len(kirjain) != 1 or not kirjain.isalpha(): 
                print("debug: virheellinen syöte")
                continue
            return kirjain

    def pelaa(self):
        self.puu.alusta_peli()
        max_vaaria_arvauksia = 6

        while True:
            self.tyhjenna_naytto()

            print("---------------")
            print("Väärin arvatut:", self.puu.vaarin_arvatut_kirjaimet)
            print("Vääriä:", self.puu.vaaria_arvauksia, "/", max_vaaria_arvauksia)
            print("---------------")
            print("\n" * 5)
            self.tulosta_sana(self.puu.arvattava_sana)
            print("\n" * 2)
            print("debug_print", self.puu.debug_print())
            print(f"({self.puu.arvattava_sana})")
            print()

            kirjain = self.arvaus()
            self.puu.arvaa(kirjain)


            # TODO: voitto ja häviö erilliseen funktioon, ehkä sekuntikello joka heittää loputtua takaisin aloitusnäytölle
            # Häviö
            if self.puu.vaaria_arvauksia >= max_vaaria_arvauksia:
                self.tyhjenna_naytto()
                print("Game over!")
                print("Oikea sana oli:", self.puu.arvattava_sana, "\n")
                break

            # Voitto
            if self.puu.jaljella_olevia_kirjaimia <= 0:
                self.tyhjenna_naytto()
                print("Voitto tuli!\n")
                self.__voittosana = self.puu.arvattava_sana
                self.puu.kirjoita_highscore()
                break
    
    def ohjeet(self):
        """ Tulostaa otsikon ja ohjeet """
        if self.__voittosana == "":
            self.__voittosana = "HIRSIPUU"

        jakaja = f"+-+-{'+-' * (len(self.__voittosana) // 2)}+"

        print(jakaja)
        print(f"  {self.__voittosana.upper()}")
        print(jakaja)
        print("1: Pelaa")
        print("2: Highscoret")
        print("3: Poistu")
        print(jakaja)

    def suorita(self):
        self.tyhjenna_naytto()

        while True:
            self.ohjeet()
            komento = input("komento: ")

            if komento == "1":
                self.pelaa()
            if komento == "2":
                self.tulosta_highscore
            if komento == "3":
                break


if __name__ == "__main__":
    sovellus = HirsipuuSovellus
    sovellus().suorita()