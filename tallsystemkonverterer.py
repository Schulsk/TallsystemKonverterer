
def main():
    inp = None
    while inp != "" and inp != "n":
        inp = input("Hvilken base skal du regne fra?\n")
        fraBase = int(inp)
        inp = input("Hvilken base skal du regne til?\n")
        tilBase = int(inp)
        inp = input("Hva er tallet du vil konvertere fra?\n")
        tall = inp.upper()
        verdier = siffere_til_verdier(tall)
        decimaltall = til_decimal(verdier, fraBase)
        print("Decimaltall:", decimaltall)
        nyttTall = fra_decimal(decimaltall, tilBase)
        print(f"Ditt nye tall med base {tilBase} er:", nyttTall)
        inp = input("Nytt tall?\n")
        print()


def fra_decimal(tall, til):
    konvertert = tall
    verdi = int(tall)
    konvertert = []
    i = 1
    while verdi > 0:
        print("Runde", i)
        print(verdi)
        rest = verdi % til
        print(rest)
        konvertert.append(rest)
        verdi = verdi // til

        i += 1

    nyttTall = verdier_til_siffere(konvertert)

    return nyttTall

def verdier_til_siffere(verdier):
    siffere = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9",
               10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F", 16:"G", 17:"H", 18:"I", 19:"J",
               20:"K", 21:"L", 22:"M", 23:"N", 24:"O", 25:"P", 26:"Q", 27:"R", 28:"S", 29:"T"}

    tall = ""
    for verdi in verdier:
        tall = siffere[verdi] + tall

    return tall

def siffere_til_verdier(siffere):
    muligVerdier = [0, 1, 2, 3, 4, 5, 6, 7, 8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
               20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
    muligeSiffere = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
               "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
               "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"]

    tall = []

    for siffer in siffere:
        i = 0
        for muligSiffer in muligeSiffere:
            if muligSiffer == siffer:
                index = i
            i += 1
        tall.append(muligVerdier[index])
    print(tall)
    return tall

def til_decimal(verdier, fra):
    total = 0
    potens = len(verdier) - 1
    for verdi in verdier:
        total += verdi * (fra ** potens)
        potens -= 1
    return total

main()
