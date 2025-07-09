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


def algoritem1(veriga):
    '''algoritem vrne kazalca na glavo sode in glavo lihe verige, pri tem ustvari novi verigi'''
    g_sodi = g_lihi = trenutni_lihi = trenutni_sodi = None

    trenutni = veriga
    while trenutni is not None:
        # pogledamo sode vrednosti v verigi in upoštevamo še primer, če je veriga prazna
        if trenutni.podatek is not None and trenutni.podatek % 2 == 0:
            # za prvega sodega ustvarimo novo verigo
            if g_sodi is None:
                g_sodi = Vozel(trenutni.podatek)
                trenutni_sodi = g_sodi
            # vsako naslednjo sodo vrednost samo dodamo v verigo narejeno na prvem koraku, ko smo našli sodo vrednost
            else:
                trenutni_sodi.naslednji = Vozel(trenutni.podatek)
                trenutni_sodi = trenutni_sodi.naslednji
        # pregledamo še lihe vrednosti in ponovno upoštevamo primer, če je veriga prazna
        elif trenutni.podatek is not None:
            # za prvega lihega ustvarimo novo verigo
            if g_lihi is None:
                g_lihi = Vozel(trenutni.podatek)
                trenutni_lihi = g_lihi
            # vsako naslednjo liho vrednost dodamo v verigo narejeno na prvem koraku, ko smo našli liho vrednsot
            else:
                trenutni_lihi.naslednji = Vozel(trenutni.podatek)
                trenutni_lihi = trenutni_lihi.naslednji
        # prestaviti se moramo na naslednjo vrednost v prvotni verigi
        trenutni = trenutni.naslednji
    return g_sodi, g_lihi

print("Prvi testni primer, ki ustvari nova dva vozla:")
# 1. testni primer: 1 -> 2 -> 7 -> 3 -> 11 -> 22 -> 9 -> 14
veriga = Vozel(1, Vozel(2, Vozel(7, Vozel(3, Vozel(11, Vozel(22, Vozel(9, Vozel(14))))))))
g_sodi, g_lihi = algoritem1(veriga)

# izpis: 2 -> 22 -> 14
trenutni = g_sodi
while trenutni is not None:
    print(trenutni.podatek, end="")
    if trenutni.naslednji is not None:
        print(" -> ", end="")
    trenutni = trenutni.naslednji
print(" ")

# izpis: 1 -> 7 -> 3 -> 11 -> 9
trenutni = g_lihi
while trenutni is not None:
    print(trenutni.podatek, end="")
    if trenutni.naslednji is not None:
        print(" -> ", end="")
    trenutni = trenutni.naslednji
print("\n")

print("Drugi testni primer, ki ustvari nova dva vozla:")
# 2. testni primer: 1 -> 3 -> 9 -> 35 -> 23
veriga = Vozel(1, Vozel(3, Vozel(9, Vozel(35, Vozel(23)))))
g_sodi, g_lihi = algoritem1(veriga)

# izpis: nič
trenutni = g_sodi
while trenutni is not None:
    print(trenutni.podatek, end="")
    if trenutni.naslednji is not None:
        print(" -> ", end="")
    trenutni = trenutni.naslednji
print(" ")

# izpis: 1 -> 3 -> 9 -> 35 -> 23
trenutni = g_lihi
while trenutni is not None:
    print(trenutni.podatek, end="")
    if trenutni.naslednji is not None:
        print(" -> ", end="")
    trenutni = trenutni.naslednji
print("\n")

print("Tretji testni primer, ki ustvari nova dva vozla:")
# 3. testni primer: prazen vozel
veriga = Vozel()
g_sodi, g_lihi = algoritem1(veriga)

# izpis: nič
trenutni = g_sodi
while trenutni is not None:
    print(trenutni.podatek, end="")
    if trenutni.naslednji is not None:
        print(" -> ", end="")
    trenutni = trenutni.naslednji
print(" ")

# izpis: nič
trenutni = g_lihi
while trenutni is not None:
    print(trenutni.podatek, end="")
    if trenutni.naslednji is not None:
        print(" -> ", end="")
    trenutni = trenutni.naslednji
print("\n")
########################################################################################################################################################

def algoritem2(veriga):
    '''algoritem vrne kazalca na glavo sode in glavo lihe verige, pri tem spremeni obstoječo verigo'''
    g_sodi = g_lihi = trenutni_lihi = trenutni_sodi = None
    trenutni = veriga
    while trenutni is not None:
        # pregledamo ali je veriga prazna in če je vrednost soda
        if trenutni.podatek is not None and trenutni.podatek % 2 == 0:
            # ko prvič naletimo na sodo vrednost je glava sodih vrednosti kar enaka tej prvi trenutni vrednosti, ki jo proglasimo za trenutni_sodi
            if g_sodi is None:
                g_sodi = trenutni
                trenutni_sodi = g_sodi
            # vsakič naslednjič, ko naletimo na sodo vrednost moramo nadaljevati trenutni_sodi
                trenutni_sodi.naslednji = trenutni
                trenutni_sodi = trenutni_sodi.naslednji
        # podobno kot zgoraj za sode velja za lihe vrednosti
        elif trenutni.podatek is not None:
            if g_lihi is None:
                g_lihi = trenutni
                trenutni_lihi = g_lihi
            else:
                trenutni_lihi.naslednji = trenutni
                trenutni_lihi = trenutni_lihi.naslednji
        
        trenutni = trenutni.naslednji

    # še za 120 oz. zadnjega sodega moramo narediti njegov kazalec None
    if trenutni_sodi is not None:
        trenutni_sodi.naslednji = None
    # tudi za 301 oz. zadnjega lihega moramo narediti njegov kazalec None
    if trenutni_lihi is not None:
        trenutni_lihi.naslednji = None
    return g_sodi, g_lihi

# 1. testni primer: 1 -> 500 -> 73 -> 44 -> 11 -> 120 -> 9 -> 301
print("Prvi testni primer, ki spremeni obstoječ vozel:")
veriga = Vozel(1, Vozel(500, Vozel(73, Vozel(44, Vozel(11, Vozel(120, Vozel(9, Vozel(301))))))))
g_sodi, g_lihi = algoritem2(veriga)

# izpis: 500 -> 44 -> 120
trenutni = g_sodi
while trenutni is not None:
    print(trenutni.podatek, end="")
    if trenutni.naslednji is not None:
        print(" -> ", end="")
    trenutni = trenutni.naslednji
print(" ")

# izpis: 1 -> 73 -> 11 -> 9 -> 301
trenutni = g_lihi
while trenutni is not None:
    print(trenutni.podatek, end="")
    if trenutni.naslednji is not None:
        print(" -> ", end="")
    trenutni = trenutni.naslednji
print("\n")

# 2. testni primer: 2 -> 80 -> 24 -> 16 -> 30
print("Drugi testni primer, ki spremeni obstoječ vozel:")
veriga = Vozel(2, Vozel(80, Vozel(24, Vozel(16, Vozel(30)))))
g_sodi, g_lihi = algoritem2(veriga)

# izpis: 2 -> 80 -> 24 -> 16 -> 30
trenutni = g_sodi
while trenutni is not None:
    print(trenutni.podatek, end="")
    if trenutni.naslednji is not None:
        print(" -> ", end="")
    trenutni = trenutni.naslednji
print(" ")

# izpis: nič
trenutni = g_lihi
while trenutni is not None:
    print(trenutni.podatek, end="")
    if trenutni.naslednji is not None:
        print(" -> ", end="")
    trenutni = trenutni.naslednji
print("\n")

# 3. testni primer: prazen vozel
print("Tretji testni primer, ki spremeni obstoječ vozel:")
veriga = Vozel()
g_sodi, g_lihi = algoritem2(veriga)

# izpis: nič
trenutni = g_sodi
while trenutni is not None:
    print(trenutni.podatek, end="")
    if trenutni.naslednji is not None:
        print(" -> ", end="")
    trenutni = trenutni.naslednji
print(" ")

# izpis: nič
trenutni = g_lihi
while trenutni is not None:
    print(trenutni.podatek, end="")
    if trenutni.naslednji is not None:
        print(" -> ", end="")
    trenutni = trenutni.naslednji



