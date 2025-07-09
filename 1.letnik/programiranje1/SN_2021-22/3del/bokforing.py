import sys

N, Q = map(int, input().split())
slovar = {}
vrednost = 0

for vrstica in sys.stdin:
    vrstica = vrstica.strip()
    vrstica1 = vrstica.split(" ")
    # SET
    if len(vrstica1) == 3:
        oseba = vrstica1[1]
        znesek_na_racunu = vrstica1[2]
        slovar[oseba] = znesek_na_racunu
    # pogledamo se RESTART in PRINT
    if len(vrstica1) == 2:
        if vrstica1[0] == "PRINT":
            oseba_za_izpis = vrstica1[1]
            print(slovar.get(oseba_za_izpis, vrednost)) 
        if vrstica1[0] == "RESTART":
            # vsem kljucem da enako vrednost
            vrednost = vrstica1[1]
            slovar.clear()



        