def cikel(permutacija, zacetek):
    """vrne cikel, ki ga v permutaciji doloca zacetek"""
    tab_cikel = [zacetek]
    kljuc = zacetek
    while permutacija[kljuc] != zacetek:
        tab_cikel.append(permutacija[kljuc])
        kljuc = permutacija[kljuc]
    return tab_cikel

print(cikel({1:4, 2:2, 3:6, 4:7, 5:8, 6:5, 7:1, 8:3}, 3))
print(cikel({1:4, 2:2, 3:6, 4:7, 5:8, 6:5, 7:1, 8:3}, 2))