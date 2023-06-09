import random
from datetime import datetime
import os

class Hirsipuu:
    def __init__(self) -> None:
        self.__arvattava_sana = ""
        self.__oikein_arvatut_kirjaimet = []
        self.__vaarin_arvatut_kirjaimet = []
        self.__arvatut_kirjaimet = []
        self.__vaaria_arvauksia = 0
        self.__aloitusaika = None
        self.__jaljella_olevat_kirjaimet = []

    @property
    def arvattava_sana(self) -> str:
        return self.__arvattava_sana
    
    @property
    def oikein_arvatut_kirjaimet(self) -> list:
        return self.__oikein_arvatut_kirjaimet
    
    @property
    def vaaria_arvauksia(self) -> int:
        return self.__vaaria_arvauksia
    
    @property
    def vaarin_arvatut_kirjaimet(self) -> list:
        return self.__vaarin_arvatut_kirjaimet
    
    @property
    def jaljella_olevia_kirjaimia(self) -> int:
        return len(self.__jaljella_olevat_kirjaimet)
    
    def kirjoita_highscore(self) -> None:
        """ Kirjoittaa highscores-tiedostoon päivämäärän, arvattavan sanan, kauan aikaa kului sanan arvaamiseen sekä väärien arvausten määrän """
        with open("highscores.csv", "a") as tiedosto:
            pvm = datetime.now()
            pvm_f = pvm.strftime("%Y.%m.%d/%H:%M:%S")
            ero = pvm - self.__aloitusaika
            minuutit = ero.total_seconds() // 60
            sekuntit = int(ero.total_seconds() % 60)
            tiedosto.write(f"{pvm_f};{self.arvattava_sana};{int(minuutit):02d}:{int(sekuntit):02d};{self.__vaaria_arvauksia}\n")

    def lue_highscore(self) -> dict:
        """ Palauttaa highscore-tiedoston sisällön sanakirjana, avain = sana, arvot = pvm, tulos, väärät arvaukset """ 
        tiedosto = "highscores.csv"
        sanakirja = {}
        if os.path.exists(tiedosto): # tarkistetaan varuilta, että tiedosto on olemassa
            with open(tiedosto, "r") as tiedosto:
                for rivi in tiedosto:
                    rivi = rivi.strip() # poistellaan whitespace yms merkit
                    osat = rivi.split(";") #pvm;sana;tulos;vaarat_arvaukset
                    sanakirja[osat[1]] = {"pvm": osat[0], "tulos": osat[2], "vaarat_arvaukset": osat[3]}
            return sanakirja
        else:
            self.nollaa_highscore() # jos ei ollut, niin kirjoitetaan tyhjä tiedosto
            return None

    def nollaa_highscore(self) -> None:
        """ Ylikirjoittaa highscores-tiedoston tyhjäksi """
        with open("highscores.csv", "w") as tiedosto:
            pass

    def alusta_peli(self) -> None:
        """ Lukee sanat tiedostosta listaan ja tarkistaa löytyykö sana jo aiemmin arvatuista sanoista, """
        """ jos ei, niin tallentaa satunnaisen sanan listasta arvattava_sana muuttujaan """

        self.__oikein_arvatut_kirjaimet = []
        self.__vaarin_arvatut_kirjaimet = []
        self.__arvatut_kirjaimet = []
        self.__vaaria_arvauksia = 0

        sanat = []
        with open("kaikkisanat.txt", "r", encoding="utf-8") as tiedosto:
            for rivi in tiedosto:
                sanat.append(rivi.strip())
        aiemmin_arvatut_sana = self.lue_highscore()
        if aiemmin_arvatut_sana == None: # jos tyhjä, niin ei tarvitse tarkistaa löytyykö sana jo sieltä
            self.__arvattava_sana = random.choice(sanat)
            self.__aloitusaika = datetime.now()
            self.__jaljella_olevat_kirjaimet = list(self.__arvattava_sana)
        else:
            yritykset = 0 # yritetään löytää sanaa 100k kertaa, joka on riittävästi kaikkien rivien läpikäyntiin,
                          # mutta ei aiheuteta päättymätöntä silmukkaa jos jostain syystä kaikki sanat ovat jo arvattu
            sana = random.choice(sanat)
            while sana in aiemmin_arvatut_sana:
                if yritykset >= 100000:
                    raise ValueError("Olet löytänyt salaisen lopun. Taidat olla melkoinen sananikkari!")
                sana = random.choice(sanat)
                yritykset += 1

            self.__arvattava_sana = random.choice(sanat)
            self.__aloitusaika = datetime.now()
            self.__jaljella_olevat_kirjaimet = list(self.__arvattava_sana)
    
    def arvaa(self, kirjain: str) -> None:
        """ Tarkistaa jos kirjain esiintyy arvattavassa sanassa, jos ei niin kasvattaa väärien arvauksien määrää, """
        """ muuten poistaa jaljella_olevat_kirjaimet listasta kaikki annetut merkit. """
        """ Jos jaljella_olevat_kirjaimet listan pituus on nolla, silloin, ehkä, toivottavasti, sana on arvattu oikein """
        if kirjain in self.__arvatut_kirjaimet:
            print("Kirjain on jo kerran arvattu")
            return
        
        if kirjain in self.__arvattava_sana:
            self.__oikein_arvatut_kirjaimet.append(kirjain)
            self.__arvatut_kirjaimet.append(kirjain)
            tmp = []
            for merkki in self.__jaljella_olevat_kirjaimet:
                if merkki != kirjain:
                    tmp.append(merkki)
            self.__jaljella_olevat_kirjaimet = tmp
            
        else:
            self.__arvatut_kirjaimet.append(kirjain)
            self.__vaarin_arvatut_kirjaimet.append(kirjain)
            self.__vaaria_arvauksia += 1
