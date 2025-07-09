with open("namig_za_geslo.txt") as dat:
    prvo_stevilo = dat.readline()
    rezultat = int(prvo_stevilo)
    for vrstica in dat:
        vrstica1 = vrstica.strip()
        operacija, stevilo = vrstica1.split(" ")
        if operacija == "-":
            rezultat -= int(stevilo)
        if operacija == "+":
            rezultat += int(stevilo)
        if operacija == "/":
            rezultat //= int(stevilo)
        if operacija == "x":
            rezultat *= int(stevilo)
print(str(rezultat)[-4:])
