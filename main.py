from hirsipuu import Hirsipuu
from grafiikka import hirttopiirretty
from datetime import datetime
from random import choice
import os
import platform
import msvcrt

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
        # Tulostaa hirttopuun (indeksinä väärien arvausten määrä)
        print(hirttopiirretty[self.puu.vaaria_arvauksia])
        print()

        for kirjain in sana:
            if kirjain in self.puu.oikein_arvatut_kirjaimet:
                print(kirjain, " ", end="")
            else:
                print("_ ", end="") 
        
    def tulosta_highscore(self):
        self.tyhjenna_naytto
        highscores = self.puu.lue_highscore()

        print("\n================================")
        if highscores == {}:
            print("   Täällä ei ole vielä mitään.", end="")
        else:
            for sana, tulokset in highscores.items():
                pvm = datetime.strptime(tulokset["pvm"], "%Y.%m.%d/%H:%M:%S")

                tulos = tulokset["tulos"]
                vaarat = tulokset["vaarat_arvaukset"]

                print()
                print(f"{pvm}")
                print('\033[1m' + sana + '\033[0m') # escape sequence lihavointiin
                print(f"  \x1B[3m ratkaisuaika:\x1B[0m {tulos} min")
                print(f"  \x1B[3m vääriä arvauksia:\x1B[0m {vaarat}")
        print("\n================================")
        print("paina 2 tai 'ESC' palataksesi")
        print("paina x nollataksesi highscoret")

        # Odotetaan komentoa ennen kuin palataan alkuvalikkoon
        while True:
            if msvcrt.kbhit():
                nappain = msvcrt.getch()
                if nappain == b'2' or nappain == b'\x1b':
                    self.tyhjenna_naytto()
                    break

                # Tuloksien nollaus
                if nappain == b'x':
                    self.tyhjenna_naytto()
                    print("\n" * 3)
                    print(f"OLETKO AIVAN VARMA ETTÄ HALUAT NOLLATA TULOKSET?")
                    print(f"\033[1m tätä ei voi peruuttaa \033[0m")
                    print(f"Y: kyllä  N: ei")
                    print()
                    komento = input("komento: ")

                    if komento in ["Y", "y"]:
                        self.puu.nollaa_highscore()
                        self.tyhjenna_naytto()
                        break
                    elif komento in ["N", "n"]:
                        self.tyhjenna_naytto()
                        break

    def arvaus(self) -> str:
        while True:
            kirjain = input("kirjain: ")
            if len(kirjain) != 1 or not kirjain.isalpha(): 
                self.tyhjenna_naytto
                continue
            return kirjain

    def pelaa(self):
        self.puu.alusta_peli()
        max_vaaria_arvauksia = 6
        voittoviestit = ["Voitto tuli!", "Nonnii!", "Hienosti!", "Poika on tullut kotiin!"]
        havioviestit = ["Game over!", "Sellasta.", "Turpiin tuli!", "Miten meni noin niinkun omasta mielestä?"]

        while True:
            self.tyhjenna_naytto()
            self.tulosta_sana(self.puu.arvattava_sana)

            # Tulosta väärät kirjaimet
            print("\n" * 2)
            print('\033[1m' + 'x:' + '\033[0m', sorted(self.puu.vaarin_arvatut_kirjaimet))
            print("\n" * 2)

            # DEBUGGAUS
            # print("debug_print", self.puu.debug_print())
            # print(f"({self.puu.arvattava_sana})")
            
            # Kysellään kirjaimia arvattavaksi
            kirjain = self.arvaus()
            self.puu.arvaa(kirjain)

            # Hävitessä tulostaa suruviestin
            if self.puu.vaaria_arvauksia >= max_vaaria_arvauksia:
                self.tyhjenna_naytto()
                print(hirttopiirretty[6])
                print(choice(havioviestit))
                print(f"\x1B[3moikea sana oli \033[1m{self.puu.arvattava_sana}\033[0m \x1B[0m\n")
                break

            # Voitettaessa tulostaa ilosanoman sekä tallentaa tulokset highscoretiedostoon
            if self.puu.jaljella_olevia_kirjaimia <= 0:
                self.tyhjenna_naytto()
                print(hirttopiirretty[self.puu.vaaria_arvauksia])
                print(choice(voittoviestit))
                self.__voittosana = self.puu.arvattava_sana
                self.puu.kirjoita_highscore()
                break

    def ohjeet(self):
        """ Tulostaa otsikon ja ohjeet """
        if self.__voittosana == "":
            self.__voittosana = "HIRSIPUU"

        jakaja = f"+-+-{'+-' * (len(self.__voittosana) // 2)}+"
        print(f"{jakaja}")
        print(f"  {self.__voittosana.upper()}")
        print(f"{jakaja}")
        print(f"1: Pelaa")
        print(f"2: Highscoret")
        print(f"3: Poistu")
        print(f"{jakaja}")

    def suorita(self):
        while True:
            self.ohjeet()
            komento = input("komento: ")

            if komento == "1":
                self.tyhjenna_naytto()
                self.pelaa()
            if komento == "2":
                self.tyhjenna_naytto()
                self.tulosta_highscore()
            if komento == "3":
                break


if __name__ == "__main__":
    sovellus = HirsipuuSovellus
    sovellus().suorita()