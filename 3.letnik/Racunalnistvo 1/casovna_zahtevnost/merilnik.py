import time                         # Štoparica
import matplotlib.pyplot as plt     # Risanje grafov
import random                       # Za generiranje primerov
import io

def izmeri_cas(fun, primer):
    """Izmeri čas izvajanja funkcije `fun` pri argumentu `primer`."""

    zacetek = time.perf_counter()
    fun(primer)
    konec = time.perf_counter()
    izvajanje = konec - zacetek
    return izvajanje
    


def oceni_potreben_cas(fun, gen_primerov, n, k):
    """Funkcija oceni potreben čas za izvedbo funkcije `fun` na primerih velikosti `n` 
    kot povprečje `k` ponovitev."""
    cas = 0
    for i in range(k):
        cas += izmeri_cas(fun, gen_primerov(n))
    return cas/k


def narisi_in_pokazi_graf(fun, gen_primerov, sez_n, k=10):
    """Funkcija vrne graf porabljenega časa za izračun `fun` glede na velikosti 
    primerov v `sez_n`. Za oceno časa uporabi `k` ponovitev. """

    sez_y = [oceni_potreben_cas(fun, gen_primerov, sez_n[i], k) for i in range(len(sez_n))]
    plt.title('Časovna odvisnot')
    plt.xlabel('velikost vnosa (input size)')
    plt.ylabel('čas [s]')
    plt.plot(sez_n, sez_y, 'r')
    plt.legend([fun.__name__], loc ="upper left")
    plt.show()



def izpisi_case(fun, gen_primerov, sez_n, k=10):
    """Funkcija vrne tabelo časa za izračun `fun` glede na velikosti primerov v `sez_n`. 
    Za oceno uporabi `k` ponovitev."""

    casi = [oceni_potreben_cas(fun, gen_primerov, sez_n[i], k) for i in range(len(sez_n))] 

    pad = len(str(sez_n[-1])) 

    # izpiši glavo tabele
    """ POJASNILO: če uporabimo `{:n}` za f-niz, bo metoda vstavila
    argument, in nato na desno dopolnila presledke, dokler ni skupna dolžina
    niza enaka vrednosti `n`. Če želimo širino prilagoditi glede na neko
    spremenljivko, to storimo kot prikazuje spodnja vrstica (torej s
    `{:{pad}}` kjer moramo nato podati vrednost za `pad`)."""
    izpis = "{:{pad}} | Čas izvedbe [s]".format("n", pad=pad) + '\n'
    # horizontalni separator
    str_casi = list(map(str, casi))
    naj = len(str_casi[0])
    for i in str_casi:
        if len(i) > naj:
            naj = len(i)
    
    sep_len = naj + pad + 3 
    izpis += "-"*sep_len + '\n'

    for i in range(len(casi)):
        izpis += "{:{pad}} | {}".format(sez_n[i], casi[i], pad=pad) + '\n'
    return izpis
    


def primerjava_dveh_funkcij(fun, gen_primerov, sez_n, k=10):
    for j in range(2):
        sez_y = [oceni_potreben_cas(fun[j], gen_primerov, sez_n[i], k) for i in range(len(sez_n))]
        plt.plot(sez_n, sez_y)
    plt.title('Primerjava časovne odvisnoti dveh funkcij')
    plt.xlabel('velikost vnosa (input size)')
    plt.ylabel('čas [s]')
    # fun[0].__name__ bo dal dejansko ime funkcije drugače dobim <function test_fun_kvad at 0x110ad8400>, če f'{fun[0]}
    plt.legend([fun[0].__name__, fun[1].__name__], loc ="upper left")
    plt.show()

def izvoz_podatkov(fun, datoteka, gen_primerov, sez_n, k=10):
    with open(datoteka, "w", encoding='utf8') as dat:
        dat.write('Tabela časovne odvisnosti:\n') 
        dat.write(izpisi_case(fun, gen_primerov, sez_n, k=10))
        dat.write('\n')



# -----------------------------------------------------------------------------
# Nekaj preprostih testnih funkcij

def test_fun_lin(sez):
    "Testna funkcija z linearno časovno zahtevnostjo."
    x = 0
    for n in sez:
        x += n
    return x


def test_fun_kvad(sez):
    "Testna funkcija s kvadratično časovno zahtevnostjo."
    x = 0
    for n in sez:
        for n in sez:
            x += n
    return x


def test_gen_sez(n):
    "Generira testni seznam dolžine n."
    return [random.randint(-n, n) for _ in range(n)]

# -----------------------------------------------------------------------------
# Ker je datoteka mišljena kot knjižnica, imejte vse 'primere izvajanja'
# zavarovane z `if __name__ == '__main__':`, da se izvedejo zgolj, če datoteko
# poženemo kot skripto, in se ne izvedejo, če datoteko uvozimo kot knjižnico.

if __name__ == '__main__':
    print(izpisi_case(test_fun_lin, test_gen_sez, [i * 10 for i in range(1, 101)], k=10))
    # narisi_in_pokazi_graf(test_fun_lin, test_gen_sez, [i * 10 for i in range(1, 11)], k=10)
    # primerjava_dveh_funkcij([test_fun_kvad, test_fun_lin], test_gen_sez, [i * 10 for i in range(1, 11)], k=10)
    # izvoz_podatkov(test_fun_lin, 'test.txt', test_gen_sez, [i * 10 for i in range(1, 11)], k=10)