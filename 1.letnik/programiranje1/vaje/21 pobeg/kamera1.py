# Za vsako vrstico izracuna povprecno dolzino besed,
# nato pa preveri, koliko vrstic je takih, da je 
# povprecna dolzina najvec enako dolzini imena kamere.
# Zaradi varnosti je potrebno ime kamere vnesti pri zagonu programa.

ime_kamere = input("Vnesi ime kamere: ")
meja = len(ime_kamere)

dobrih_vrstic = 0
with open("sodelavci.txt") as f:
    for vrstica in f:
        besede = vrstica.strip().split(" ")
        povp_dolzina = 0
        for beseda in besede:
            povp_dolzina += len(beseda)
        povp_dolzina /= len(besede)
        if povp_dolzina <= meja:
            dobrih_vrstic += 1  
print(dobrih_vrstic)