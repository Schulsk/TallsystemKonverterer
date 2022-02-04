

class Tall:
    def __init__(self, tall, base=None, negativ=None):
        self._tall = tall
        self._base = base
        if negativ == None:
            self._negativ = self._sjekk_om_negativ()
        else:
            self._negativ = negativ
        self._verdier = self.siffere_til_verdier()

    def __str__(self):
        if self._negativ:
            if self._base != 2:
                streng = f"-{self._tall}"
            else:
                streng = f"{self._tall}"
        else:
            streng = f"{self._tall}"
        return streng

    def _sjekk_om_negativ(self):
        if self._tall[0] == "-":
            self._tall = self._tall.strip("-")
            return True
        return False

    def er_negativt(self):
        return self._negativ

    def hent_tall(self):
        return self._tall

    def hent_base(self):
        return self._base

    def hent_verdier(self):
        return self._verdier

    def siffere_til_verdier(self):
        sifferVerdi = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9,
                       "A":10, "B":11, "C":12, "D":13, "E":14, "F":15, "G":16, "H":17, "I":18, "J":19,
                       "K":20, "L":21, "M":22, "N":23, "O":24, "P":25, "Q":26, "R":27, "S":28, "T":29}

        verdier = []

        for tall in self._tall:
            verdier.append(sifferVerdi[tall])
        return verdier
