
class Elt:
    def __init__(self, vsebina, dummy=False):
        self.dummy = dummy
        if not dummy:
            self.vsebina = vsebina


class Vrsta:
    def __init__(self, zacetni_elti=None):
        self.zacetni = Elt(None, dummy=True)
        self.koncni = self.zacetni
        if zacetni_elti:
            for x in zacetni_elti:
                self.vstavi(x)

    def prazna(self):
        return self.zacetni.dummy

    def vstavi(self, vsebina):
        self.koncni.naslednji = Elt(None, dummy=True)
        self.koncni.vsebina = vsebina
        self.koncni.dummy = False
        self.koncni = self.koncni.naslednji

    def zacetek(self):
        if self.prazna():
            raise IndexError('vrsta je prazna')
        return self.zacetni.vsebina

    def odstrani(self):
        if self.prazna():
            raise IndexError('vrsta je prazna')
        self.zacetni = self.zacetni.naslednji

    def __repr__(self):
        seznam = []
        p = self.zacetni
        while not p.dummy:
            seznam.append(repr(p.vsebina))
            p = p.naslednji
        return 'Vrsta([{0}])'.format(', '.join(seznam))

    def __str__(self):
        if self.prazna():
            return 'ZACETEK : KONEC'
        seznam = []
        p = self.zacetni
        while not p.dummy:
            seznam.append(str(p.vsebina))
            p = p.naslednji
        return 'ZACETEK : ' + ' : '.join(seznam) + ' : KONEC'

class Sklad:
    '''predstavitev podatkovne strukture sklad z uporabo vrste
        odlocila sem se, da bom sklad predstavila iz vrste tako:
        vrsta: ZACETEK: 1 5 8 :KONEC ---> SKLAD: DNO: 8:5:1 :VRH
        torej zadnji v vrsti bo na dnu sklada in prvi v vrsti bo na vrhu sklada 
    '''
    def __init__(self):
        self.podatki = Vrsta()

    def __str__(self):
        if self.podatki.prazna():
            return 'DNO : VRH'
        seznam = []
        v1 = Vrsta()
        while not self.podatki.prazna():
            element = self.podatki.zacetek()
            seznam.append(str(element))
            v1.vstavi(element)
            self.podatki.odstrani()
        while not v1.prazna():
            elt = v1.zacetek()
            self.podatki.vstavi(elt)
            v1.odstrani()
        return 'DNO : ' + ' : '.join(seznam[::-1]) + ' : VRH'

    def odstrani_sklad(self):
        '''odstrani zadnji element v skladu, torej to je prvi element v vrsti'''
        if self.podatki.prazna():
            raise Exception("Sklad je prazen, nič za odstraniti!")
        self.podatki.odstrani()

    def vstavi_sklad(self, x):
        '''na konec sklada vstavi podatek x, torej na zacetek vrste vstavi element x'''
        # ideja: ker v vrsti vstavljamo na konec, dodamo na konec strazarja, potem vstavimo podatek x,
        # nato pa po vrsti vstavljamo podatke iz vrste na konec 
        # vrsta: 1 5 8 -> 1 5 8 None x -> 5 8 None x 1 -> ... -> None x 1 5 8, na koncu se odstranimo None
        self.podatki.vstavi(None)
        self.podatki.vstavi(x)
        while self.podatki.zacetek() is not None:
            zacetek = self.podatki.zacetek()
            self.podatki.vstavi(zacetek)
            self.podatki.odstrani()
        self.podatki.odstrani()

    def prazen_sklad(self):
        '''vrne True v primeru, da je sklad prazen in False sicer'''
        return self.podatki.prazna()

    def vrh_sklad(self):
        '''vrne vrhnji element sklada, ki jeravno prvi element v vrsti'''
        if self.podatki.prazna():
            raise Exception("Sklad je prazen, nič za vrniti!")
        return self.podatki.zacetek()
        


sk = Sklad()
print("1. Ali je sklad prazen?", sk.prazen_sklad(), "\n") # True

sk.vstavi_sklad(1)
sk.vstavi_sklad(7)
sk.vstavi_sklad(33)
sk.vstavi_sklad(0)
sk.vstavi_sklad(500)
print(sk, "\n") # DNO: 1:7:33:0:500 :VRH
sk.odstrani_sklad()
sk.odstrani_sklad()
print(sk) # DNO: 1:7:33 :VRH
print("3. Vrh trenutnega sklada:", sk.vrh_sklad(), "\n") # vrh bi moral biti 33

sk.odstrani_sklad()
sk.odstrani_sklad()
print(sk)
print("4. Ali je sklad prazen?", sk.prazen_sklad(), "\n")

sk.odstrani_sklad()
print(sk) # prazen sklad
print("6. Ali je sklad prazen?", sk.prazen_sklad(), "\n")

#sk.vrh_sklad() napaka
#sk.odstrani_sklad()napaka

            