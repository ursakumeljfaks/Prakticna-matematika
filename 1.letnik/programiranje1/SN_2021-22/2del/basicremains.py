def pretvorba_v_bazo(n, b):
    """pretvori stevilo n v katero koli bazo b, ustvari tabelo"""
    if n == 0:
        return [0]
    stevke = []
    while n != 0:
        stevke.append(int(n % b))
        n //= b
    return stevke[::-1]

testni_primer = 0
while True:
    testni_primer += 1
    try:
        b, p, m = map(str, input().split())
    except:
        break
    b = int(b)
    # int ima privzeto vrednost v b = 10, za vse ostale jo moramo podati
    ostanek = int(p, b) % int(m, b) # ostanek pri deljenju števila p v bazi b in števila m v bazi b, 
                                  # vemo da int() pretvarja niz v celo število, zato damo pri branju podatkov
                                  # mapping v string, b pa pretvorimo v int() (celo število) iz stringa
    # kot rezultat v modul dobimo število v osnovi (bazi) 10, to pa moramo potem z našo funkcijo spremeniti v zahtevano osnovo b
    rezultat = ""
    for stevilo in pretvorba_v_bazo(ostanek, b):
        rezultat += str(stevilo) 
    print(rezultat)