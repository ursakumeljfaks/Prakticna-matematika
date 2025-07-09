class Vozel:
    """
    Osnovni sestavni del verižnega seznama.
    """
    def __init__(self, podatek, naslednji=None):
        self.podatek = podatek
        self.naslednji = naslednji

    def __str__(self):
        if self.naslednji is not None:
            return '{} -> {}'.format(self.podatek, self.naslednji)
        else:
            return '{} -> X'.format(self.podatek)


def izbrisi_manjse(vrsta):
    '''po vrsti odstranjuje kazalce na verige vozlov, katerih vsota vozlov je manjša 
    od vsote vozlov v verigi, ki se nahaja pred njim.'''

    if not vrsta or len(vrsta) == 1:
        return vrsta

    trenutni_kazalec = vrsta[0]
    prejsnji_kazalec = None
    trenutna_vsota = 0
    prejsnja_vsota = 0

    while trenutni_kazalec is not None:
        trenutna_vsota += trenutni_kazalec.podatek
        
        if trenutna_vsota < prejsnja_vsota:
            vrsta.remove(trenutni_kazalec)
        else:
            prejsnja_vsota = trenutna_vsota
            prejsnji_kazalec = trenutni_kazalec
        trenutni_kazalec = trenutni_kazalec.naslednji
    
    return vrsta
    


v1 = Vozel(2, Vozel(1, Vozel(1)))
v2 = Vozel(5, Vozel(2, Vozel(4)))
v3 = Vozel(6, Vozel(2))
v4 = Vozel(1, Vozel(3, Vozel(5)))
v5 = Vozel(5, Vozel(3, Vozel(2, Vozel(1))))
v6 = Vozel(1, Vozel(2, Vozel(3, Vozel(4))))
v7 = Vozel(2, Vozel(4, Vozel(1, Vozel(4))))
vrsta = [v1, v2, v3, v4, v5, v6, v7]

izbrisi_manjse(vrsta)

# Print the modified list
for node in vrsta:
    print(node)