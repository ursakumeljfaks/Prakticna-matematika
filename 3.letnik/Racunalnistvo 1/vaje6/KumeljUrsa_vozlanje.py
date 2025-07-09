
class Vozel:
    '''
    Razred, ki predstavlja posamezen vozel s podatkom v verižnem seznamu.
    '''
    def __init__(self, podatek, naslednji=None):
        self.podatek = podatek
        self.naslednji = naslednji

class VerizniSeznam:
    '''
    Razred, ki predstavlja verižni seznam z začetkom in koncem.
    '''
    def __init__(self):
        self._zacetek = None
        self._konec = None

    def __str__(self):
        niz = ''
        vozel = self._zacetek
        while vozel is not None:
            niz += '{} -> '.format(repr(vozel.podatek))
            vozel = vozel.naslednji
        return niz + '•'
    
def vstavi_veriga_vozlov(veriga, stevilo):
    '''na ustrezno mesto v naraščajoci verigi ustavi število stevilo in vrne kazalec na prvega v verigi'''
    prvi = veriga
    prejsnji = None
    while prvi is not None and stevilo > prvi.podatek:
        prejsnji = prvi
        prvi = prvi.naslednji
    # pridemo do pravega mesta   
    nov = Vozel(stevilo)
    # povezemo prejsnjega z novim in novega s prvim
    if prejsnji is not None:
        prejsnji.naslednji = nov
    else:
        veriga = nov
    nov.naslednji = prvi   
    return veriga

# vstavi 3 v 1->2->4->5
v1 = Vozel(1, Vozel(2, Vozel(4, Vozel(5))))
v2 = vstavi_veriga_vozlov(v1, 3)
trenutni = v2
while trenutni is not None:
    print(trenutni.podatek, end="")
    if trenutni.naslednji is not None:
        print(" -> ", end="")
    trenutni = trenutni.naslednji
# dobiti bi morali 1->2->3->4->5

# vstavi 5 v 1->2->4->5
v1 = Vozel(1, Vozel(2, Vozel(4, Vozel(5))))
v2 = vstavi_veriga_vozlov(v1, 5)
trenutni = v2
while trenutni is not None:
    print(trenutni.podatek, end="")
    if trenutni.naslednji is not None:
        print(" -> ", end="")
    trenutni = trenutni.naslednji
# dobiti bi morali 1->2->4->5->5

# vstavi 1 v 1->2->4->5
v1 = Vozel(1, Vozel(2, Vozel(4, Vozel(5))))
v2 = vstavi_veriga_vozlov(v1, 1)
trenutni = v2
while trenutni is not None:
    print(trenutni.podatek, end="")
    if trenutni.naslednji is not None:
        print(" -> ", end="")
    trenutni = trenutni.naslednji
# dobiti bi morali 1->1->2->4->5
print("\n")

def vstavi_verizni_seznam(seznam, stevilo):
    '''na ustrezno mesto v naraščajočem verižnem seznamu ustavi število stevilo in 
    vrne kazalec na prvega, ter zadnjega v verižnem seznamu'''
    prejsnji = None
    prvi = seznam._zacetek
    while prvi is not None and stevilo > prvi.podatek:
        prejsnji = prvi
        prvi = prvi.naslednji
    
    nov = Vozel(stevilo)
    # povezemo prejsnjega z novim in novega s prvim
    if prejsnji is not None:
        prejsnji.naslednji = nov
    else:
        seznam._zacetek = nov
    nov.naslednji = prvi
    # kazalec za konec spremenimo, ce je to potrebno
    if prvi is None:
        seznam._konec = nov

    return seznam

# vstavi 10 v 1->2->4->5
s1 = VerizniSeznam()
vstavi_verizni_seznam(s1, 1)
vstavi_verizni_seznam(s1, 2)
vstavi_verizni_seznam(s1, 4)
vstavi_verizni_seznam(s1, 5)
print(vstavi_verizni_seznam(s1,10))# 1->2->4->5->10

# vstavi 2 v prazen
s2 = VerizniSeznam()
print(vstavi_verizni_seznam(s2,2)) # 2->

# vstavi 1 v 1->2->4->5
s3 = VerizniSeznam()
vstavi_verizni_seznam(s3, 1)
vstavi_verizni_seznam(s3, 2)
vstavi_verizni_seznam(s3, 4)
vstavi_verizni_seznam(s3, 5)
print(vstavi_verizni_seznam(s3,1)) # 1->1->2->4->5

# vstavi 3 v 1->2->4->5
s4 = VerizniSeznam()
vstavi_verizni_seznam(s4, 1)
vstavi_verizni_seznam(s4, 2)
vstavi_verizni_seznam(s4, 4)
vstavi_verizni_seznam(s4, 5)
print(vstavi_verizni_seznam(s4,3)) # 1->2->3->4->5







