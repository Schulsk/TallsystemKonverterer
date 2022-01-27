

class Tall:

    def __init__(self, tall, base):
        self._tall = tall
        self._base = base
        self._decimal = self.konverter_til_decimaltall()

    def hent_tall_med_base(self, base):


    def konverter_til_base():


    def konverter_til_decimaltall(self):
        verdier = self._tall.hent_verdier()
        base = self._tall.hent_base()
        total = 0
        potens = len(verdier) - 1
        for verdi in verdier:
            total += verdi * (base ** potens)
            potens -= 1
        return str(total)
