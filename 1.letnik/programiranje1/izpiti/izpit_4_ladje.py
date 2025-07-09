# 1. naloga 

def paketov(teze, nosilnost):
    skupaj = 0
    i = 0
    for paket in teze:
        skupaj += paket
        if skupaj <= nosilnost:
            i += 1
    return i
    
teze = [5, 3, 8, 1, 2, 3, 5, 4, 2, 4]
nosilnost = 9
print(paketov(teze, nosilnost))

# 2. naloga
def razporedi(teze, nosilnost):
    seznam_seznamov = []
    ze_pregledani = set()

    while True:
        seznam = []
        skupaj = 0
        for indeks in range(len(teze)):
            if indeks not in ze_pregledani:
                skupaj += teze[indeks]
                if skupaj <= nosilnost:
                    seznam.append(teze[indeks])
                    ze_pregledani.add(indeks)
                else:
                    skupaj -= teze[indeks]
        seznam_seznamov.append(seznam)
        if len(ze_pregledani) == len(teze):
            break
    return seznam_seznamov
teze = [5, 3, 8, 1, 2, 3, 5, 4, 2, 4]
nosilnost = 9
print(razporedi(teze, nosilnost))  


    # while teze != []:
    #     koliko = paketov(teze, nosilnost)
    #     seznam.append(teze[:koliko])
    #     seznam_seznamov.append(seznam)
    #     del teze[:koliko]
    # return seznam_seznamov

# 3. naloga
def pois(ime):
    with open(ime, encoding="utf-8") as dat:
        slovar = {}
        for vrstica in dat:
            kraj, drugo = vrstica.split(":")
            zelenjava, koliko = drugo.split(" ")
            if zelenjava == "paradižnik":
                slovar[kraj] += koliko
        return slovar

# 4. naloga
def skladiscniki(marsovec, hierarhija):
    koliko = 0
    for glavni in hierarhija:
        if glavni == marsovec:
            for morebitna_oseba in hierarhija[marsovec]:
                if hierarhija[morebitna_oseba] == []:
                    koliko += 1
                else:
                    koliko += skladiscniki(morebitna_oseba, hierarhija)   
    return koliko

hierarhija = {
            "Adam": ["Matjaž", "Cilka", "Daniel"],
            "Aleksander": [],
            "Alenka": [],
            "Barbara": [],
            "Cilka": [],
            "Daniel": ["Elizabeta", "Hans"],
            "Erik": [],
            "Elizabeta": ["Ludvik", "Jurij", "Barbara"],
            "Franc": [],
            "Herman": ["Margareta"],
            "Hans": ["Herman", "Erik"],
            "Jožef": ["Alenka", "Aleksander", "Petra"],
            "Jurij": ["Franc", "Jožef"],
            "Ludvik": [],
            "Margareta": [],
            "Matjaž": ["Viljem"],
            "Petra": [],
            "Tadeja": [],
            "Viljem": ["Tadeja"],
        }
print(skladiscniki("Jurij", hierarhija))

