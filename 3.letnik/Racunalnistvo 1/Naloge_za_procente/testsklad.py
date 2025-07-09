class Sklad:
    def __init__(self):
        self.podatki = []

    def vstavi(self, x):
        self.podatki.append(x)

    def prazen(self):
        return len(self.podatki) == 0

    def odstrani(self):
        if self.prazen(): raise ValueError('ODSTRANI: Sklad je prazen.')
        self.podatki.pop()

    def vrh(self):
        if self.prazen(): raise ValueError('VRH: Sklad je prazen.')
        return self.podatki[-1]
      
    def poberi(self):
      rez = self.vrh()
      self.odstrani()
      return rez

    def __str__(self):
        izp = 'DNO'
        for elt in self.podatki: izp += ' : ' + str(elt)
        return izp + ' : VRH'
    
def preveri(sk1, sk2):
    '''vrne True, če se vsi elementi drugega sklada (sk2) nahajajo
    v prvem skladu (sk1) v enakem relativnem vrstnem redu in False sicer'''
    p1 = Sklad()
    p2 = Sklad()
    ali = True
    while not sk1.prazen():
        if not sk2.prazen():
            if sk1.vrh() == sk2.vrh():
                p2.vstavi(sk2.vrh())
                p1.vstavi(sk1.vrh())
                sk1.odstrani()
                sk2.odstrani()
                ali = True
            else:
                p1.vstavi(sk1.vrh())
                sk1.odstrani()
        else:
            p1.vstavi(sk1.vrh())
            sk1.odstrani()
    if not sk2.prazen():
        while not sk2.prazen():
            ali = False
            p2.vstavi(sk2.vrh())
            sk2.odstrani()
    while not p1.prazen():
        sk1.vstavi(p1.vrh())
        p1.odstrani()
    while not p2.prazen():
        sk2.vstavi(p2.vrh())
        p2.odstrani()
    return ali

    
sk1 = Sklad()
sk1.vstavi(3)
sk1.vstavi(10)
sk1.vstavi(1)
sk1.vstavi(9)
sk1.vstavi(5)
sk1.vstavi(7)
print(sk1)

sk2 = Sklad()
sk2.vstavi(1)
sk2.vstavi(5)
sk2.vstavi(70)
print(sk2)
print(preveri(sk1,sk2))

print(sk1)
print(sk2)


sk3 = Sklad()
sk4 = Sklad()
print(preveri(sk3,sk4))