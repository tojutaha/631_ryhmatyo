import random

class Hirsipuu:
    def __init__(self) -> None:
        self.__arvattava_sana = ""
        self.__oikein_arvatut_kirjaimet = []
        self.__vaarin_arvatut_kirjaimet = []
        self.__arvatut_kirjaimet = []
        self.__vaaria_arvauksia = 0

        self.alusta_peli()
        self.__jaljella_olevat_kirjaimet = list(self.__arvattava_sana)

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
    
    def debug_print(self):
        return self.__jaljella_olevat_kirjaimet
    
    @property
    def jaljella_olevia_kirjaimia(self) -> int:
        return len(self.__jaljella_olevat_kirjaimet)

    def alusta_peli(self) -> None:
        """ Lukee sanat tiedostosta listaan ja tallentaa satunnaisen sanan listasta arvattava_sana muuttujaan """
        sanat = []
        with open("kaikkisanat.txt", "r", encoding="utf-8") as tiedosto:
            for rivi in tiedosto:
                sanat.append(rivi.strip())
        self.__arvattava_sana = random.choice(sanat)
    
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

# debuggausta varten
if False:
    max_vaaria_arvauksia = 6
    hp = Hirsipuu()
    while True:
        print(hp.arvattava_sana)
        kirjain = input("kirjain: ")
        hp.arvaa(kirjain)
        print("Oikein arvatut kirjaimet: ", hp.oikein_arvatut_kirjaimet)
        print("Väärin arvatut kirjaimet: ", hp.vaarin_arvatut_kirjaimet)
        print("Vääriä arvauksia: ", hp.vaaria_arvauksia)
        print("Jäljellä olevia kirjaimia: ", hp.jaljella_olevia_kirjaimia)
        print("debug_print", hp.debug_print())
        if hp.vaaria_arvauksia >= max_vaaria_arvauksia:
            print("Game over")
            break
        if hp.jaljella_olevia_kirjaimia <= 0:
            print("Voitto tuli")
            break
else:
    pass
