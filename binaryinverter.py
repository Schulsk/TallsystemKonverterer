

def main2():
    inp = None
    while inp != "":
        inp = input("Binærtall: ")
        if inp != "":
            #binary = int(inp)
            binary = inp
            inverted = invert(binary)
            newBinary = add_to_binary(inverted)
            if binary[0] == "1":
                print(f"Tallet {binary} kan bety:")
                positiv = til_decimal(binary, 2)
                negativ = til_decimal(newBinary, 2)
                print("Positiv:", positiv)
                print(f"Negativ: -{negativ}")
            elif binary[0] == "0":
                print(f"Tallet {binary} kan bety:")
                positiv = til_decimal(binary, 2)
                print("Positiv:", positiv)
                print(f"2-er-komplementen til {binary} er:\n", newBinary)


            print("Ditt tall invertert til 2er-komplement:", newBinary)
            print()


def add_to_binary(binary):
    values = []
    for number in binary:
        values.append(int(number))

    add = 1
    i = -1
    for value in values:
        values[i] += add
        add = 0
        if values[i] == 2:
            values[i] = 0
            add = 1
        values[i] = str(values[i])
        i -= 1

    newBinary = "".join(values)
    return newBinary

def invert(binary):
    inverted = ""
    for number in str(binary):
        if number == "1":
            inverted += "0"
        elif number == "0":
            inverted += "1"
    return inverted

def til_decimal(binary, fra):

    total = 0
    potens = len(binary) - 1
    for number in binary:
        total += int(number) * (fra ** potens)
        potens -= 1
    return total

main2()
