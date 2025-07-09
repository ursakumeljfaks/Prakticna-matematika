########################################################################################
### Tega dela kode ne spreminjaj! ######################################################
import random
random.seed(324)
polinomi = [[random.randint(-5, 20) for _ in range(random.randint(3, 10))] for _ in range(1000)]
########################################################################################
########################################################################################
#
#
# 'polinomi' je tabela polinomov, omenjena v navodilih.
def odvod(polinom):
    """izracuna odvod polinoma"""
    odvod = []
    for indeks, koeficient in enumerate(polinom):
        odvod.append(koeficient * indeks)
    return odvod[1:]

def odvod_v_tocki(polinom):
    """izracuna odvod v tocki 3"""
    vsota = 0
    polinom2 = odvod(polinom)[1:]
    for indeks, koeficient in enumerate(polinom2,1):
        vsota += koeficient * ((3)** indeks)
    return vsota + odvod(polinom)[0]

def povprecje_polinomov(polinomi):
    """povprecje polinomov"""
    vsota = 0
    povprecje = 0
    for polinom in polinomi:
        vsota += odvod_v_tocki(polinom)
    povprecje = vsota / len(polinomi)
    return povprecje

print(povprecje_polinomov(polinomi))



        