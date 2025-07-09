class Vozel:
    ''' Osnovni element verižnega seznama '''
    
    def __init__(self, kaj=None, kam=None):
        self._podatek = kaj
        self._naslednji  = kam
        
    def __str__(self):
        return str(self._podatek)
    
    def __repr__(self):
        return "Vozel({0}, {1})".format(self.podatek, repr(self.naslednji))
    
    @property
    def podatek(self):
        '''vrne podatek'''
        return self._podatek
    
    @podatek.setter
    def podatek(self, pod):
        '''nastavi podatek'''
        self._podatek = pod
        
    @property
    def naslednji(self):
        '''vrne kazalec na naslednjega'''
        return self._naslednji
    
    @naslednji.setter
    def naslednji(self, moj_nas):
        '''Vozlu nastavi novega naslednika'''
        self._naslednji = moj_nas

class VerizniSeznam:
    '''verižni seznam s kazalcem na začetku'''
    def __init__(self):
        self.prvi = None
    
    def prazen(self):
        '''vrne True v primeru, da je verižni seznam prazen in False sicer'''
        return self.prvi is None

    def prvi_element(self):
        '''vrne kazalec na prvi vozel, razen če je seznam prazen'''
        if self.prazen():
            raise Exception("Verižni seznam je prazen!")
        return self.prvi
    
    def dodaj(self, x):
        '''na začetek verižnega seznama doda vozel s podatkom x'''
        nov = Vozel(x, self.prvi)
        self.prvi = nov
    
    def odstrani(self):
        if self.prazen():
            raise Exception("Verižni seznam je prazen, nič za odstraniti!")
        self.prvi = self.prvi.naslednji

class Sklad:
    
    def __init__(self):
        self.podatki = VerizniSeznam()

    def prazen_sklad(self):
        return self.podatki.prazen()
    
    def vstavi_sklad(self, x):
        self.podatki.dodaj(x)

    def odstrani_sklad(self):
        if self.podatki.prazen():
            raise Exception("Sklad je prazen, nič za odstraniti!")
        self.podatki.odstrani()
    
    def vrh(self):
        '''Vrne vrhnji element sklada brez odstranitve.'''
        if self.podatki.prazen():
            raise Exception("Sklad je prazen, nič za vrniti!")
        return self.podatki.prvi_element().podatek
    
    def __str__(self):
        trenuten = self.podatki.prvi
        stevila = []
        izpis = "DNO : "
        while trenuten is not None:
            stevila.append(str(trenuten))
            trenuten = trenuten.naslednji
        for stevilo in stevila[::-1]:
            izpis += stevilo + " : "
        izpis += "VRH"
        return izpis
    
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
print("3. Vrh trenutnega sklada:", sk.vrh(), "\n") # vrh bi moral biti 33

sk.odstrani_sklad()
sk.odstrani_sklad()
print(sk)
print("4. Ali je sklad prazen?", sk.prazen_sklad(), "\n")

sk.odstrani_sklad()
print(sk) # prazen sklad
print("6. Ali je sklad prazen?", sk.prazen_sklad(), "\n")

#sk.odstrani_sklad()
#sk.vrh()
