def zadnji_lihi(s):
    """spremeni vrstni red stevil, da so najprej soda in nato liha stevila"""
    soda = []
    liha = []
    for stevilo in s:
        if stevilo % 2 == 0:
            soda.append(stevilo)
        else:
            liha.append(stevilo)
    return soda + liha

print(zadnji_lihi([5, 8, 4, 17, 13, 10, 9]))     



 