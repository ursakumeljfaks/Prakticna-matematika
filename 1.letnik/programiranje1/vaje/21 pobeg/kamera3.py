# Pridobi mnozico vseh besed (priimkov), ki se nahajajo v datoteki sodelavci.txt.
# Nato izracunaj vrednost vsake besede tako, da vsako črko pretvoriš v njeno 
# številsko kodo po unicode standardu (funkcija ord).
# Izračunaj tudi vrednost imena kamere, ki je potrebno zaradi varnosti vnesti
# ob zagonu datoteke.
# Poišči besedo, katere vrednost je najbolj podobna vrednosti imena kamere.

ime_kamere = input("Vnesi ime kamere: ")
vrednost_imena = sum(ord(znak) for znak in ime_kamere)
besede = set()
besede_z_vrednostjo = set()

with open("sodelavci.txt") as f:
    for vrstica in f:
        besede_v_vrstici = vrstica.strip().split(" ")
        besede.update(besede_v_vrstici)
    
for beseda in besede:
    vrednost_besede = sum(ord(znak) for znak in beseda)
    besede_z_vrednostjo.add((beseda, vrednost_besede))
naj = min(besede_z_vrednostjo, key=lambda x: abs(x[1] - vrednost_imena))

print(naj[1])



        


    


        
    


    


