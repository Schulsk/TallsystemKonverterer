

class Kalkulator:

    def __init__(self):
        self._tall = []


    def kjor(self):
        inp = ""
        while inp != "a":
            print("Skriv inn et tall og så tallets base")
            inp = input("> ").lower()

            if inp.isdigit():
