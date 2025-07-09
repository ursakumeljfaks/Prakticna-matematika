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
    def __init__(self):
        self.prvi = None
    
    def prazen(self):
        return self.prvi is None

    def prvi(self):
        '''vrne kazalec na prvi vozel, razen če je seznam prazen'''
        if self.prazen():
            raise Exception("Verižni seznam je prazen!")
        return self.prvi
    
    def dodaj(self, x):
        '''na začetek verižnega seznama doda vozel s podatkom x'''
        nov = Vozel()
        nov.podatek = x
        nov.naslednji = self.prvi
        self.prvi = nov
    
    def odstrani(self):
        if self.prazen():
            raise Exception("Verižni seznam je prazen, nič za odstraniti!")
        self.prvi = self.prvi.naslednji


class Sklad:
    '''s pomočjo verige vozlov implemetiran razred sklad'''
    def __init__(self):
        # na začetku je prazna veriga
        self.prvi = Vozel()
    
    def __str__(self):
        trenuten = self.prvi.naslednji
        stevila = []
        izpis = "DNO : "
        while trenuten is not None:
            stevila.append(str(trenuten))
            trenuten = trenuten.naslednji
        for stevilo in stevila:
            izpis += str(stevilo) + " : "
        izpis += "VRH"
        return izpis

    def odstrani(self):
        '''spremeni verigo tako, da odstrani zadnji element verige'''
        # v primeru, da na že praznem skladu pokličemo metodo odstrani
        if self.prazen() :
            raise ValueError('ODSTRANI: Sklad je prazen.')
        nov = self.prvi
        while nov.naslednji.naslednji is not None:
            nov = nov.naslednji
        nov.naslednji = None
        

    def vstavi(self, x):
        '''spremeni verigo tako, da vstavi element na konec verige'''
        nov = Vozel(x)
        trenuten = self.prvi
        while trenuten.naslednji is not None:
            trenuten = trenuten.naslednji
        trenuten.naslednji = nov

    def prazen(self):
        '''vrne True v primeru, da je sklad prazen in False sicer'''
        if self.prvi.naslednji is None:
            return True
        return False
    
    def vrh(self):
        '''vrne vrhni element v skladu oz. zadnji element v verigi'''
        if self.prazen() :
            raise ValueError('VRH: Sklad je prazen.')
        trenuten = self.prvi
        while trenuten.naslednji is not None:
            trenuten = trenuten.naslednji
        zadnji = trenuten.podatek
        return zadnji

# Testni primeri:

sk = Sklad()
print("1. Ali je sklad prazen?", sk.prazen(), "\n") # True

sk.vstavi(1)
sk.vstavi(7)
sk.vstavi(33)
sk.vstavi(0)
sk.vstavi(500)
print(sk, "\n") # DNO: 1:7:33:0:500 :VRH

sk.odstrani()
sk.odstrani()
print(sk) # DNO: 1:7:33 :VRH
print("3. Vrh trenutnega sklada:", sk.vrh(), "\n") # vrh bi moral biti 33

sk.odstrani()
sk.odstrani()
print(sk)
print("4. Ali je sklad prazen?", sk.prazen(), "\n")

sk.odstrani()
print(sk) # prazen sklad
print("6. Ali je sklad prazen?", sk.prazen(), "\n")

#sk.odstrani()
#sk.vrh()




