# Testno poročilo

**Ime:** Urša Kumelj

**Datum:** 19.11.2023

---

Na vajah smo delali z verigo vozlov in verižnim seznamom. Za verižni seznam smo naredili razred ter še druge metode. Vseskozi pa smo razred potrebovali, saj ostalih nalog ni bilo mogoče rešiti brez njih. Nato pa smo še ustvarili dve funkciji in sicer vstavi_veriga_vozlov in vstavi_verizni_seznam. Ti dve funkciji smo nato stestirali s testi od sošolcev.

## Organizacija dela

V večini sem delala sama, če pa se mi je zataknilo, mi je pa pomagal sošolec.

## Komentarji in opombe

Vaje so se mi zdele poučne.

# Veriga vozlov 

**Navodilo:** Napišite funkcijo vstavi_veriga_vozlov(veriga, stevilo), ki prejme naraščajoče urejeno verigo vozlov ter število vstavi na pravilno mesto v zaporedju vrednosti. Če vrednost že obstaja, naj vozel vstavi za zadnjega z enako vrednostjo . Funkcija naj strukturo spremeni na mestu (angl. in place), torej naj ustvari največ en nov vozel (lahko pa seveda ustvarite dodatne "kazalce" na vozle).

Predpostavite, da so vsi elementi števila in urejeni po vrsti. Prav tako lahko predpostavite, da ima struktura vsaj en element.

**Rešitev:**
```python
from verizni_seznam import Vozel
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
```
**Komentar:** Imamo dva kazalca prejsnjega in enega pred njim (predhodnika). Premikamo se toliko časa dokler ne najdemo pravega mesta, kamor bomo število vstavili. Ko smo dosegli to mesto potrebujemo kazalce samo pravilno povezati. Prejsnjega na novega (nov je vozel, ki vsebuje to stevilo) ter novega na predhodnika od prejsnega. 

**Testi:** 
```python
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
```
```python
    1->2->3->4->5
```
```python
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
```
```python
    1->2->4->5->5
```
```python
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
```
```python
    1->1->2->4->5
```
**Kolegovi testi (Miha Rakovec):**

```python
#Primer 1: več elementov
print('Primer 1: več elementov')
veriga = Vozel(1, Vozel(4, Vozel(5, Vozel(12, Vozel(27, Vozel(29, Vozel(43, Vozel(97, None))))))))
print('veriga =', veriga)
print('')

#vstavi na sredino
print('veriga = vstavi_veriga_vozlov(veriga, 14)')
veriga = vstavi_veriga_vozlov(veriga, 14)
print(veriga)

#vstavi na konec
print('veriga = vstavi_veriga_vozlov(veriga, 100)')
veriga = vstavi_veriga_vozlov(veriga, 100)
print(veriga)

#vstavi na začetek
print('veriga = vstavi_veriga_vozlov(veriga, -2)')
veriga = vstavi_veriga_vozlov(veriga, -2)
print(veriga)
```
```python
Primer 1: več elementov
veriga = <KumeljUrsa_vozlanje.Vozel object at 0x7fa7963552e0>

veriga = vstavi_veriga_vozlov(veriga, 14)
<KumeljUrsa_vozlanje.Vozel object at 0x7fa7963552e0>
veriga = vstavi_veriga_vozlov(veriga, 100)
<KumeljUrsa_vozlanje.Vozel object at 0x7fa7963552e0>
veriga = vstavi_veriga_vozlov(veriga, -2)
<KumeljUrsa_vozlanje.Vozel object at 0x7fa7963551c0>
```

**Komentar na kolegove teste:** Pri vseh testih bi potrebovala narediti enako kot pri svojih, da bi mi njegovo delovalo. Jaz sem namreč iterirala skozi vse vozle in pri tem izpisovala vsak podatek posebaj.

---

## Verižni seznam
**Navodilo:** Napišite funkcijo vstavi_verizni_seznam(veriga, stevilo), ki prejme naraščajoče urejeni verizni seznam ter število vstavi na pravilno mesto v zaporedju vrednosti. Če vrednost že obstaja, naj vozel vstavi za zadnjega z enako vrednostjo . Funkcija naj strukturo spremeni na mestu (angl. in place), torej naj ustvari največ en nov vozel (lahko pa seveda ustvarite dodatne "kazalce" na vozle).

Predpostavite, da so vsi elementi števila in urejeni po vrsti. Prav tako lahko predpostavite, da ima struktura vsaj en element.

**Rešitev:**
```python
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
```
**Komentar:** Imamo dva kazalca prejsnjega in enega pred njim (predhodnika). Premikamo se toliko časa dokler ne najdemo pravega mesta, kamor bomo število vstavili. Ko smo dosegli to mesto potrebujemo kazalce samo pravilno povezati. Prejsnjega na novega (nov je vozel, ki vsebuje to stevilo) ter novega na predhodnika od prejsnega. Edino kar moramo tukaj paziti je, če moramo število vstaviti na konec verižnega seznama, saj se nam bo potem spremnil kazalec za konec, drugače pa končni kazalec ostaja vseskozi nespremenjen.


**Moji testi:**

```python
# vstavi 10 v 1->2->4->5
s1 = VerizniSeznam()
vstavi_verizni_seznam(s1, 1)
vstavi_verizni_seznam(s1, 2)
vstavi_verizni_seznam(s1, 4)
vstavi_verizni_seznam(s1, 5)
print(vstavi_verizni_seznam(s1,10))# 1->2->4->5->10
```
```python
    1->2->4->5->10
```
```python
# vstavi 2 v prazen
s2 = VerizniSeznam()
print(vstavi_verizni_seznam(s2,2)) # 2->
```
```python
    2->
```
```python
# vstavi 1 v 1->2->4->5
s3 = VerizniSeznam()
vstavi_verizni_seznam(s3, 1)
vstavi_verizni_seznam(s3, 2)
vstavi_verizni_seznam(s3, 4)
vstavi_verizni_seznam(s3, 5)
print(vstavi_verizni_seznam(s3,1)) # 1->1->2->4->5
```
```python
    1->1->2->4->5
```
```python
# vstavi 3 v 1->2->4->5
s4 = VerizniSeznam()
vstavi_verizni_seznam(s4, 1)
vstavi_verizni_seznam(s4, 2)
vstavi_verizni_seznam(s4, 4)
vstavi_verizni_seznam(s4, 5)
print(vstavi_verizni_seznam(s4,3)) # 1->2->3->4->5
```
```python
    1->2->3->4->5
```

**Kolegovi testi (Miha Rakovec):**
```python
#Primer 1: več elementov
print('Primer 1: več elementov')
seznam = VerizniSeznam()
seznam._zacetek = Vozel(1, Vozel(4, Vozel(5, Vozel(12, Vozel(27, Vozel(29, Vozel(43, Vozel(97, None))))))))
print('seznam =', seznam)
print('')

#vstavi na sredino
print('vstavi_verizni_seznam(seznam, 14)')
vstavi_verizni_seznam(seznam, 14)
print(seznam)

#vstavi na konec
print('vstavi_verizni_seznam(seznam, 100)')
vstavi_verizni_seznam(seznam, 100)
print(seznam)

#vstavi na začetek
print('vstavi_verizni_seznam(seznam, -2)')
vstavi_verizni_seznam(seznam, -2)
print(seznam)
```
```python
Primer 1: več elementov
seznam = 1 -> 4 -> 5 -> 12 -> 27 -> 29 -> 43 -> 97 -> •

vstavi_verizni_seznam(seznam, 14)
1 -> 4 -> 5 -> 12 -> 14 -> 27 -> 29 -> 43 -> 97 -> •
vstavi_verizni_seznam(seznam, 100)
1 -> 4 -> 5 -> 12 -> 14 -> 27 -> 29 -> 43 -> 97 -> 100 -> •
vstavi_verizni_seznam(seznam, -2)
-2 -> 1 -> 4 -> 5 -> 12 -> 14 -> 27 -> 29 -> 43 -> 97 -> 100 -> •
```

```python
#Primer 2: prazen seznam
print('Primer 2: prazen seznam')
print('')
seznam = VerizniSeznam()
print('seznam =', seznam)

#vstavi število
print('vstavi_verizni_seznam(seznam, 77)')
vstavi_verizni_seznam(seznam, 77)
print(seznam)
```

```python
Primer 2: prazen seznam

seznam = •
vstavi_verizni_seznam(seznam, 77)
77 -> •
```

```python
#Primer 3: en sam element
print('Primer 3: en sam element')
print('')
seznam = VerizniSeznam()
seznam._zacetek = Vozel(17)
print('seznam =', seznam)

#vstavi na začetek
print('vstavi_verizni_seznam(seznam, 5)')
vstavi_verizni_seznam(seznam, 5)
print(seznam)

#vstavi na konec
print('')
seznam = VerizniSeznam()
seznam._zacetek = Vozel(17)
print('seznam =', seznam)
print('vstavi_verizni_seznam(seznam, 42)')
vstavi_verizni_seznam(seznam, 42)
print(seznam)
```
```python
Primer 3: en sam element

seznam = 17 -> •
vstavi_verizni_seznam(seznam, 5)
5 -> 17 -> •

seznam = 17 -> •
vstavi_verizni_seznam(seznam, 42)
17 -> 42 -> •
```

---

# Viri

1. Cone, M., Markdown Cheat Sheet, pridobljeno s [https://www.markdownguide.org/cheat-sheet/] https://www.markdownguide.org/cheat-sheet/), 30. 9. 2020.