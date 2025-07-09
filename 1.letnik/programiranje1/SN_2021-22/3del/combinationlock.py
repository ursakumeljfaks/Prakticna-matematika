while True:
    a, b, c, d = map(int, input().split())
    if a == 0 and b == 0 and c == 0 and d == 0:
        break

    # 1 crtica ima 360 // 40 = 9 stopinj
    skupno = 0 
    # vzamemo primer 0 30 -> od 0 do 30 gremo lahko v smeri urinega kazalca ali v obratni smeri
    # bolj se splaca v obratni smeri, ker naredimo manj, zato rabimo preveriti vse mozne variante
    if a >= b:
        skupno += a - b
    else:
        skupno += 40 - (b - a)
    if c >= b:
        skupno += c - b
    else:
        skupno += 40 - (b - c)
    if c >= d:
        skupno += c - d
    else:
        skupno += 40 - (d - c)
    # na koncu = 360 * 2, ker pise navodilo dvakrat v celoti zavrtimo, kasneje pa se za 360, torej 1080 + skupno * 9
    print(1080 + skupno * 9)