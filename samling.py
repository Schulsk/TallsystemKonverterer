

class Samling:
    def __init__(self):
        self._tall = {}     # Nøkkel i ordboken er basen tallet er skrevet i

    def __str__(self):
        streng = "Samling:\n"
        for tall in self._tall.values():
            streng += "Tall:" + str(tall) + "\n"
            streng += "Base:" + str(tall.hent_base()) + "\n"
        return streng

    def legg_til_tall(self, nokkel, nyttTall):
        self._tall[nokkel] = nyttTall

    def hent_alle_nokler(self):
        nokler = []
        for nokkel in self._tall:
            nokler.append(nokkel)
        return nokler

    def hent_alle_tall(self):
        tall = []
        for nokkel in self._tall:
            tall.append(self._tall[nokkel])
        return tall

    def hent_tall(self, nokkel):
        return self._tall[nokkel]

    def tom_samling(self):
        self._tall = {}
