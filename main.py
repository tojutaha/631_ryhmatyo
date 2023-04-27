from hirsipuu import Hirsipuu

class HirsipuuSovellus:
    def __init__(self) -> None:
        self.puu = Hirsipuu()
    
    def tulosta_sana(self, sana: str):
        """ Tulostaa san"""
        for kirjain in sana:
            if kirjain in self.puu.oikein_arvatut_kirjaimet:
                print(kirjain, " ", end="")
            else:
                print("_ ", end="")

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
            self.tulosta_sana(self.puu.arvattava_sana)
            print("\n" * 2)
            print("debug_print", self.puu.debug_print())
            print(f"({self.puu.arvattava_sana})")
            print()

            kirjain = self.arvaus()
            self.puu.arvaa(kirjain)

            print("---------------")
            print("Väärin arvatut:", self.puu.vaarin_arvatut_kirjaimet)
            print("Vääriä:", self.puu.vaaria_arvauksia, "/", max_vaaria_arvauksia)
            # print("---------------")
            # print("JÄLJELLÄ:", self.puu.jaljella_olevia_kirjaimia)
            print("\n" * 5)

            if self.puu.vaaria_arvauksia >= max_vaaria_arvauksia:
                print("Game over\n")
                break
            if self.puu.jaljella_olevia_kirjaimia <= 0:
                print("Voitto tuli\n")
                self.puu.kirjoita_highscore()
                break
    
    def ohjeet(self):
        print("+-+-+-+-+-+-+")
        print("  HIRSIPUU")
        print("+-+-+-+-+-+-+")
        print("1: Pelaa")
        print("2: Highscoret")
        print("3: Poistu")

    def suorita(self):
        while True:
            self.ohjeet()
            print("+-+-+-+-+-+-+")
            komento = input("komento: ")

            if komento == "1":
                print("\n" * 5) # tälle parempi ratkaisu?
                self.pelaa()
            if komento == "2":
                self.tulosta_highscore
            if komento == "3":
                break


if __name__ == "__main__":
    sovellus = HirsipuuSovellus
    sovellus().suorita()