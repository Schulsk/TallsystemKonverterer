
from tall import Tall
from samling import Samling

class Kalkulator:
    def __init__(self):
        self._samling = Samling()
        
        self._tall = None
        self._decimaltall = None
        self._binaertall = None
        self._toer_komplement = None
        self._andreBaser = []

    def kjor(self):
        self.intro()
        inp = ""
        while inp != "A":
            print("Hva ønsker du å gjøre?")
            print("A    -   Avslutt")
            print("N    -   Nytt tall")
            if self._tall != None:
                print("K    -   Konverter til annen base")

            inp = input().strip().upper()

            if inp != "A":
                if inp == "N":
                    self._tall = self.nytt_tall()
                    self._tom_kalkulator()
                    if self._tall.hent_base() == 10:
                        self._decimaltall = self._tall
                    elif self._tall.hent_base() == 2:
                        self._binaertall = self._tall
                    else:
                        self._andreBaser.append(self._tall)
                    self._decimaltall = Tall(self.konverter_til_decimaltall(), 10)
                    self._binaertall = Tall(self.konverter_fra_decimaltall(2), 2)
                elif inp == "K":
                    base = ""
                    baseGyldig = False
                    while not baseGyldig:
                        base = input("Base:\n")
                        if base != "" and base.isdigit():
                            baseGyldig = True
                        else:
                            print("Ugyldig input")
                    base = int(base)
                    self._andreBaser.append(Tall(self.konverter_fra_decimaltall(base), base))
                else:
                    print("Ugyldig kommando.")
                    continue

                print()
                self.print_info()
            else:
                print("¨\_(´-- ` )_/¨")

    def _tom_kalkulator(self):
        self._decimaltall = None
        self._binaertall = None
        self._toer_komplement = None
        self._andreBaser = []

    def intro(self):
        print("Denne kalkulatoren er laget for:")
        print("- Å konvertere et tall fra en base til en annen")
        print("- Å finne binærrepresentasjonen av et tall")
        print("- Å finne 2er-komplementen (negativ binærrepresentasjon) til et tall")
        print("Gjerne alt på en gang!")
        print()

    def print_info(self):
        streng = f"Tall: {self._tall}\n"
        streng += f"Base: {self._tall.hent_base()}\n"
        if self._tall.hent_base() == 2:
            streng += f"Decimaltall: {self._decimaltall}\n"
            if self._binaertall.hent_tall()[0] == "1":
                pass
            if self._tall.er_negativt():
                streng += f"2er-komplement: {self.toer_komplement()}\n"
            streng += f"Binærtall: {self._binaertall}\n"
            for tall in self._andreBaser:
                streng += f"Base {tall.hent_base()}: {tall}\n"

        streng += f"Decimaltall: {self._decimaltall}\n"
        if self._tall.er_negativt():
            streng += f"2er-komplement: {self.toer_komplement()}\n"
        streng += f"Binærtall: {self._binaertall}\n"
        for tall in self._andreBaser:
            streng += f"Base {tall.hent_base()}: {tall}\n"

        print(streng)

    def nytt_tall(self):
        print("Skriv inn nytt tall")
        tall = None
        base = None
        tallGyldig = False
        baseGyldig = False
        forste = True
        while not tallGyldig or not baseGyldig:
            if not forste:
                print("Ugyldig input.")

            if not tallGyldig:
                tall = input("Tall:\n").strip().upper()
                if tall != "":
                    tallGyldig = True
            if not baseGyldig:
                base = input("Base:\n").strip()
                if base.isdigit() and base != "":
                    baseGyldig = True
                    base = int(base)

            forste = False

        tall = Tall(tall, base)
        return tall

    def hent_tall(self):
        return self._tall

    def konverter_til_decimaltall(self):
        verdier = self._tall.hent_verdier()
        base = self._tall.hent_base()
        total = 0
        potens = len(verdier) - 1
        for verdi in verdier:
            total += verdi * (base ** potens)
            potens -= 1
        return str(total)

    def konverter_fra_decimaltall(self, tilBase):
        tall = self._decimaltall.hent_tall()
        verdi = int(tall)
        konvertert = []
        i = 1
        while verdi > 0:
            rest = verdi % tilBase
            konvertert.append(rest)
            verdi = verdi // tilBase
            i += 1

        nyttTall = self.verdier_til_siffere(konvertert)

        # Sett nok 0-er foran så binærtallet vises i bytes
        if tilBase == 2:
            antallSiffer = len(nyttTall)
            while antallSiffer % 8 != 0:
                nyttTall = "0" + nyttTall
                antallSiffer += 1
        # Sørg for at vi leverer 2er-komplementen av binærtallet
        # om originaltallet er negativt
        if self._tall.er_negativt():
            print("nyttTall:", nyttTall)
            if tilBase == 2:
                nyttTall = self.toer_komplement(nyttTall)
                print("toer-komplement:", nyttTall)

        print("nyttTall:", nyttTall)
        return str(nyttTall)

    def verdier_til_siffere(self, verdier):
        verdiSiffer = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9",
                   10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F", 16:"G", 17:"H", 18:"I", 19:"J",
                   20:"K", 21:"L", 22:"M", 23:"N", 24:"O", 25:"P", 26:"Q", 27:"R", 28:"S", 29:"T"}

        nyttTall = ""
        for verdi in verdier:
            nyttTall = verdiSiffer[verdi] + nyttTall

        return nyttTall

    def toer_komplement(self, tall=None):
        streng = ""
        negativBinaer = ""

        if tall == None and self._tall.hent_base() == 2:
            tall = self._tall.hent_tall()

        if tall != None:
            if len(tall) % 8 == 0:
                # Inverter
                invertert = ""
                for siffer in tall:
                    if siffer == "1":
                        invertert += "0"
                    elif siffer == "0":
                        invertert += "1"
                # Legg til 1
                negativBinaer = ""
                mente = True
                i = 0
                for siffer in invertert:
                    i -= 1
                    if mente:
                        if invertert[i] == "1":
                            negativBinaer = "0" + negativBinaer
                        elif invertert[i] == "0":
                            negativBinaer = "1" + negativBinaer
                            mente = False
                    else:
                        negativBinaer = invertert[i] + negativBinaer
                streng = f"Negativt binærtall: {negativBinaer}\n"
        return negativBinaer
