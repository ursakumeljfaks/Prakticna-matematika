import os
zacetek = '2019-06-01'
konec = '2019-06-30'

with open("/Users/spela/Desktop/pisni_izpit_2020/meritve.txt") as dat:

    slovar = {}
    for vrstica in dat:
        vrstica = vrstica.strip().split(",")
        datum = vrstica[0]
        kraj = vrstica[1]
        vrednost = float(vrstica[2])
        if zacetek <= datum <= konec:
            if kraj in slovar:
                slovar[kraj]["vrednost"] += vrednost
                slovar[kraj]["koliko"] += 1
            else:
                slovar[kraj] = {
                    "vrednost": 0,
                    "koliko": 0
                }
    izpis = {}
    for kraj in slovar:
        povprecje = slovar[kraj]['vrednost'] / slovar[kraj]['koliko']
        izpis[kraj] = povprecje
    print(izpis)