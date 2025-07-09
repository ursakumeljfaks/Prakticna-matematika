# V vsaki vrstici poisci ime, ki je najbolj podobno imenu kamere.
# Zaradi varnosti je potrebno ime kamere vnesti pri zagonu programa.
# Podobnost je stevilo enakih crk (brez ponavljanja), pri tem pa
# ne locimo med velikimi in malimi crkami.
# Za vse vrstice sestej podobnosti najbolj podobnih besed v vrstici.
# Vsota pove sifro za izklop kamere.

ime_kamere = input("Vnesi ime kamere: ")
mnozica_kamera = set(ime_kamere.lower())

with open("sodelavci.txt") as f:
    vsota = 0
    for vrstica in f:
        naj_podobnost = 0
        for beseda in vrstica.strip().split():
            podobnost = len(set(beseda.lower()).intersection(mnozica_kamera))
            naj_podobnost = max(podobnost, naj_podobnost)
        vsota += naj_podobnost

print(vsota)