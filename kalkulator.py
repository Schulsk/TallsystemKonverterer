
from tall import Tall
from samling import Samling

class Kalkulator:
    def __init__(self):
        self._samlinger = [Samling()]
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

            samling = self._samlinger[0]

            if inp != "A":
                if inp == "N":
                    # Legg til nytt tall
                    self._nytt_tall(inp)
                elif inp == "K":
                    # Konverter tall
                    self._konverter_tall()
                else:
                    print("Ugyldig kommando.")
                    continue

                print()
                self.print_info()
            else:
                print("¨\_(´-- ` )_/¨")

    def _nytt_tall(self, inp):
        self._tom_kalkulator()
        samling = self._samlinger[0]
        self._tall = self.nytt_tall()

        base = self._tall.hent_base()
        if base == 10:
            samling.legg_til_tall("Base 10", self._tall)
        else:
            samling.legg_til_tall(f"Base {self._tall.hent_base()}", self._tall)

        samling.legg_til_tall("Base 10", Tall(self.konverter_til_decimaltall(), 10, self._tall.er_negativt()))
        samling.legg_til_tall("Base 2", Tall(self.konverter_fra_decimaltall(2), 2, self._tall.er_negativt()))

        if self._kan_vaere_toer_komplement(self._tall):
            self._legg_til_samling()
            samling1 = self._samlinger[1]
            nyttDecimaltall = self._reverser_toer_komplement(self._tall)
            nyttTall = Tall(nyttDecimaltall, 10, True)
            samling1.legg_til_tall("Base 10", nyttTall)

    def _reverser_toer_komplement(self, tall):
        nyttTall = Tall(self.toer_komplement(tall.hent_tall()), tall.hent_base(), True)
        nyttDecimaltall = self.konverter_til_decimaltall(nyttTall)
        return nyttDecimaltall


    def _legg_til_samling(self):
        self._samlinger.append(Samling())

    def _kan_vaere_toer_komplement(self, tall):
        # Sjekker om tallet har base 2, antall siffer delelig med 8 og begynner på tallet 1
        if tall.hent_base() == 2:
            if len(tall.hent_tall()) % 8 == 0:
                if tall.hent_tall()[0] == "1":
                    return True
        return False

    def _konverter_tall(self):
        # Ta oss av brukerinput
        base = ""
        baseGyldig = False
        while not baseGyldig:
            base = input("Base:\n")
            if base != "" and base.isdigit():
                baseGyldig = True
            else:
                print("Ugyldig input")
        base = int(base)

        # Bruke inputen til å konvertere og legge til tall i begge samlingene, om begge finnes
        # Kan faktoriseres
        if len(self._samlinger) > 1:
            samling = self._samlinger[1]
            decimaltall = samling.hent_tall("Base 10")
            samling.legg_til_tall(f"Base {base}", Tall(self.konverter_fra_decimaltall(base, decimaltall), base, decimaltall.er_negativt()))

        samling = self._samlinger[0]
        decimaltall = samling.hent_tall("Base 10")
        samling.legg_til_tall(f"Base {base}", Tall(self.konverter_fra_decimaltall(base), base, decimaltall.er_negativt()))

    def _tom_kalkulator(self):
        self._samlinger = [Samling()]
        self._decimaltall = None
        self._binaertall = None
        self._toer_komplement = None
        self._andreBaser = []

    def intro(self):
        print()
        print("Denne kalkulatoren er laget for:")
        print("- Å konvertere et tall fra en base til en annen")
        print("- Å finne binærrepresentasjonen av et tall")
        print("- Å finne 2er-komplementen (negativ binærrepresentasjon) til et tall")
        print("Gjerne alt på en gang!")
        print()

    def print_info(self):
        streng = "******************************************\n"
        streng += f"Tall: {self._tall}\n"
        streng += f"Base: {self._tall.hent_base()}\n"
        streng += "\n"

        # Print alle basene i tillegg til den som ble skrevet inn
        if len(self._samlinger) == 1:
            streng += self._hent_samling_innhold(self._samlinger[0])
        else:
            streng += "Dette tallet kan ha både positiv og negativ verdi.\n\n"
            streng += "Positive verdier:\n"
            streng += self._hent_samling_innhold(self._samlinger[0])
            streng += "\n"
            streng += "Negative verdier:\n"
            streng += self._hent_samling_innhold(self._samlinger[1])

        streng += "******************************************\n"
        print(streng)

    def _hent_samling_innhold(self, samling):
        streng = ""
        for nokkel in samling.hent_alle_nokler():
            streng += f"{nokkel}: {samling.hent_tall(nokkel)}\n"
        return streng

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

    def konverter_til_decimaltall(self, tall=None):
        if tall == None:
            tall = self._tall

        verdier = tall.hent_verdier()
        base = tall.hent_base()
        total = 0
        potens = len(verdier) - 1
        for verdi in verdier:
            total += verdi * (base ** potens)
            potens -= 1
        return str(total)

    def konverter_fra_decimaltall(self, tilBase, tall=None):
        if tall == None:
            tall = self._samlinger[0].hent_tall("Base 10")

        verdi = int(tall.hent_tall())
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
            if tilBase == 2:
                nyttTall = self.toer_komplement(nyttTall)
                print("toer-komplement:", nyttTall)

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
