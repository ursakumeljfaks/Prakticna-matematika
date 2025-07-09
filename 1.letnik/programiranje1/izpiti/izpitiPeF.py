# papajščina
def razkrij(stavek):
    odkodirani = ""
    spustimo = 0
    for indeks, crka in enumerate(stavek):
        if spustimo == 0:
            if crka in "aeiou":
                odkodirani += crka
                spustimo += 2
            else:
                odkodirani += crka
        else:
            spustimo -= 1
    return odkodirani

print(razkrij('upuvopod v propograpamipirapanjepe'))           

# plezanje
def rezultati(s):
    zmnozki = []
    for oseba in s:
        zmnozek = oseba[1] * oseba[2] * oseba[3]
        zmnozki.append(zmnozek)

    prvi = zmnozki[0]
    for indeks, posamezen in enumerate(zmnozki):
        if posamezen >= prvi:
            prvi = posamezen
            zalomljen = True
        else:
            zalomljen = indeks
    return zalomljen

print(rezultati([('Garnbret Janja', 5, 1, 1), ('Nonaka Miho', 3, 3, 5), ('Noguchi Akiyo', 4, 4, 4)]))
print(rezultati([('Raboutou Brooke', 7, 2, 6), ('Pilz Jessica', 6, 5, 3), ('Jaubert Anouck', 2, 6, 7)]))

# strava

def zaporedje_dni(s):
    stevilo = 0
    seznam_dni = []
    for tupl in s:
        if tupl[0] == 0 and tupl[1] == 0:
            stevilo += 1
        else:
            seznam_dni.append(stevilo)
            stevilo = 0
    return max(seznam_dni)

# print(zaporedje_dni(([(3,15), (5,25), (0,0), (0,0), (0,0), (8, 40), (0, 0)])))

def st_dni(s):
    st_dni = 0
    for (km, min) in s:
        if km >= 5:
            st_dni += 1
    return st_dni

def minute_na_km(s):
    stevilo = 0
    for tupl in s:
        if tupl[0] == 0:
            continue
        hitrost = tupl[1] / tupl[0]
        if hitrost <= 6:
            stevilo += 1
    return stevilo

print(minute_na_km(([(3,15), (5,25), (0,0), (0,0), (0,0), (8, 40), (0, 0)])))


# karte
def preveri(karte):
    vse_karte = 'A23456789TJQK'
    vrsta = 'HDCS'
    posamezen = karte.split(" ") # ["AC", "AD"]
    for par in posamezen:
        prva = par[0]
        druga = par[1]
        if prva not in vse_karte:
            return False
        if druga not in vrsta:
            return False
    return True

print(preveri('AC AD AH AS KD'))
print(preveri('2C 4D D3 4H 2D 2H'))

# simon
def simon(niz):
    vsaka_beseda = niz.split(" ")
    for beseda in vsaka_beseda:
        if vsaka_beseda[:2] == ["Simon", "reče"]:
            return " ".join(vsaka_beseda[2:])
    return False

print(simon('Simon reče primite se za nos'))
print(simon('Dvignite levo roko'))

# dobro geslo
def geslo(stavek):
    dobro_geslo = ""
    vsaka_beseda = stavek.split(" ")
    for beseda in vsaka_beseda:
        dobro_geslo += beseda[0]
        dobro_geslo += str(len(beseda))
    return dobro_geslo

print(geslo('Dni mojih lepši polovica kmalo mladosti leta kmalo ste minule'))

# planinec miha
def st_dvatisocakov(seznam):
    stevilo = 0
    for tupl in seznam:
        if tupl[1] >= 2000:
            stevilo += 1
    return stevilo

# print(st_dvatisocakov(([("Črni vrh", 1486), ("Matajur", 1642), ("Krn", 2244), ("Špik", 2472), ("Škrlatica", 2740)])))

def najvecja_razlika(seznam):
    razlike = []
    for i in range(len(seznam)-1):
        razlika = abs(seznam[i+1][1] - seznam[i][1])
        razlike.append(razlika)
    return max(razlike)

# print(najvecja_razlika(([("Črni vrh", 1486), ("Matajur", 1642), ("Krn", 2244), ("Špik", 2472), ("Škrlatica", 2740)])))

def stopnjevanje(seznam):
    for i in range(len(seznam)-1):
        if seznam[i+1][1] < seznam[i][1]:
            return False
    return True

# print(stopnjevanje(([("Črni vrh", 1486), ("Matajur", 1642), ("Krn", 2244), ("Špik", 2472), ("Škrlatica", 2740)])))

def statistika(vzponi):
    return (st_dvatisocakov(vzponi), najvecja_razlika(vzponi), stopnjevanje(vzponi))

print(statistika(([("Črni vrh", 1486), ("Matajur", 1642), ("Krn", 2244), ("Špik", 2472), ("Škrlatica", 2740)])))
print(statistika([("Prisank", 2547), ("Jalovec", 2645), ("Triglav", 2864), ("Stenar", 2501)]))

# macja hrana
def hrana(posodice):
    navodilo = []
    for i in range(1, posodice+1):
        if i % 2 == 0 and i % 3 == 0:
            navodilo.append("mokra in suha")
        elif i % 2 == 0:
            navodilo.append("suha")
        elif i % 3 == 0:
            navodilo.append("mokra")
        else:
            navodilo.append("voda")
    return navodilo

print(hrana(6))
print(hrana(15))






    


