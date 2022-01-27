

class Samling:
    def __init__(self):
        self._tall = {}

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
