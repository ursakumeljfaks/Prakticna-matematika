def mediana(tabela):
    """vrne manjšega v tabeli dveh vrednosti"""
    return min(tabela)

data = int(input())    
while True:
    try: 
        n = int(input()) # število ekip
    except: 
        break

    tabela = sorted(list(map(int, input().split()))) # urejena tabela rezultatov študentov
    s = 0
    # da bomo sestavili najboljšo ekipo moramo oblikovati najprej nove ekipe to naredimo tako, da
    # 1/3 najslabših dodajamo 2 najboljša. Ko imamo te ekipe pa zberemo druge najboljše izmed teh.
    # primer: [1, 1, 2, 3, 3, 5, 6, 7, 9]
    # sestavimo ekipe [1, 9, 7], [1, 6, 5], [2, 3, 3] in vedno je ta 2. najboljši vsak drugi element od zadaj v urejeni tabeli
    # s = 7 + 5 + 3 = 15 (s pa bo vsota enega iz vsake ekipe, torej vsota toliko kot je n-jev)
    while n != 0: # s bo bila vsota n - krat drugo največjih rezultatov
        s += mediana(tabela[-2:])
        del tabela[-2:] # izbriše že pregledan del tabele
        n -= 1 
    print(s)