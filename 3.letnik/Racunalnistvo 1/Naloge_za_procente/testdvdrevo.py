class Drevo: 
        
    def __init__(self, *args, **kwargs):
        '''Ustvari dvojiško drevo.

        - Drevo() ustvari prazno dvojiško drevo
        - Drevo(podatek, levo, desno) ustvari dvojiško drevo z
          danim podatkom v korenu ter levim in desnim sinom. Če kakšen od sinov
          manjka, se privzame, da je prazen.
        '''
        if args:
            assert len(args) == 1
            self.prazno = False
            self.podatek = args[0]
            # če levega ali desnega sina ne podamo, ustvarimo prazno drevo
            self.levo = kwargs.pop('levo', None) or Drevo()  
            self.desno = kwargs.pop('desno', None) or Drevo()
        else:
            self.prazno = True
        # poleg že obdelanih konstruktor ne sme sprejeti drugih argumentov
        assert not kwargs

    def __repr__(self, zamik=''):
        if self.prazno:
            return 'Drevo()'.format(zamik)
        elif self.levo.prazno and self.desno.prazno:
            return 'Drevo({1})'.format(zamik, self.podatek)
        else:
           return 'Drevo({1},\n{0}      levo = {2},\n{0}      desno = {3})'.\
               format(
                   zamik,
                   self.podatek,
                   self.levo.__repr__(zamik + '             '),
                   self.desno.__repr__(zamik + '              ')
               )

    def __eq__(self, other):
        if self.prazno and other.prazno:
            return True
        elif not self.prazno and not other.prazno:
            return (
                self.podatek == other.podatek and
                self.levo == other.levo and
                self.desno == other.desno
            )
        else:
            return False

    def __hash__(self):
        if self.prazno:
            return hash(())
        else:
            return hash((self.podatek, self.levo, self.desno))


def sestevanje(drevo):
    '''sešteje vrednosti vozlišč, ki imajo samo enega sina'''
    if drevo.prazno:
        return 0
    vsota = 0
    # če levo poddrevo ni prazno, mora biti desno prazno -> vsoti prištejemo vrednost korena
    if not drevo.levo.prazno:
        if drevo.desno.prazno:
            vsota += drevo.podatek
     # če desno poddrevo ni prazno, mora biti levo prazno -> vsoti prištejemo vrednost korena
    if not drevo.desno.prazno:
        if drevo.levo.prazno:
            vsota += drevo.podatek
    # rekurzivno pregledamo še levo in desno poddrevo
    vsota += sestevanje(drevo.levo)
    vsota += sestevanje(drevo.desno)
    return vsota

# Test 1
drevo1 = Drevo(8, levo=Drevo(3, levo=Drevo(1), desno=Drevo(6, levo=Drevo(4), desno=Drevo(7))), 
               desno=Drevo(10, levo=Drevo(), desno=Drevo(14, levo=Drevo(13), desno=Drevo())))
# pričakovani izpis 24
print(sestevanje(drevo1)) 

# Test 2
drevo2 = Drevo(2, levo=Drevo(3, levo=Drevo(6)), desno=Drevo(1, levo=Drevo(7), desno=Drevo(9)))
# pričakovani izpis 3
print(sestevanje(drevo2))

# Test 3
drevo3 = Drevo(1, levo=Drevo(5, levo=Drevo(10, desno=Drevo(12, levo=Drevo(13))), desno=Drevo(6, 
        levo=Drevo(7))), desno=Drevo(11, desno=Drevo(15, levo=Drevo(16, levo=Drevo(1)), desno=Drevo(19, desno=Drevo(3)))))
# pričakovani izpis 74
print(sestevanje(drevo3))

# Test 4
drevo4 = Drevo()
# pričakovani izpis 0
print(sestevanje(drevo4))

# Test 5
drevo5 = Drevo(3, levo=Drevo(4, levo=Drevo(9, levo=Drevo(21))))
# pričakovani izpis 16
print(sestevanje(drevo5))




