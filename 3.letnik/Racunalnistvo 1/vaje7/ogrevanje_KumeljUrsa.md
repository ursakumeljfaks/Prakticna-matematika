# Poročilo

**Ime:** Urša Kumelj

**Datum:** 8.12.2023

---

Na vajah smo delali nalogo ogrevanje, kjer smo napisali štiri funkcije in zanje naredili testne primere, da smo analizirali pravilno delovanje le teh.

## Organizacija dela

Nalogo sem delala sama.

## Komentarji in opombe

Najprej bo predstavljena vsaka funkcija posebej, na koncu pa bodo sledili testi.

# Prva funkcija 

**Navodilo:** Napišite funkcijo vrni_koren(drevo), ki vrne podatek v korenu drevesa, če pa je drevo prazno pa vrne None.

**Rešitev:**
```python
from dvojisko_drevo import Drevo
def vrni_koren(drevo):
    '''vnre podatek v korenu drevesa'''
    if drevo.prazno:
        return None
    return drevo.podatek 
```

# Druga funkcija 

**Navodilo:** Napišite funkcijo je_list(drevo), ki preveri ali je podano drevo list.

```python
from dvojisko_drevo import Drevo
def je_list(drevo):
    '''preveri ali je drevo list'''
    if drevo.prazno:
        return True
    return drevo.levo.prazno and drevo.desno.prazno
```

# Tretja funkcija

**Navodilo:** Napišite funkcijo nikoli_levo(drevo), ki preveri, da ima vsako vozlišče drevesa kvečjemu desno poddrevo.

```python
from dvojisko_drevo import Drevo
def nikoli_levo(drevo):
    '''preveri, da ima vsako vozlisce drevesa kvecjemu desno poddrevo'''
    if drevo.prazno:
        return True
    return drevo.levo.prazno and not drevo.desno.prazno
```

# Četrta funkcija

**Navodilo:** Napišite funkcijo visina(drevo), ki izračuna višino dvojiškega drevesa.

```python
from dvojisko_drevo import Drevo
def visina(drevo):
    '''izracuna visino dvojiskega drevesa'''
    if drevo.prazno:
        return 0
    else:
        return max(1 + visina(drevo.levo), 1 + visina(drevo.desno))
```

# Testi za funkcije

## Test 1
```python
drevo1 = Drevo()
print("Koren (R: None)",vrni_koren(drevo1))
print("List (R: True)", je_list(drevo1))
print("Nikoli levo (R: True)", nikoli_levo(drevo1))
print("Visina (R: 0)", visina(drevo1))
print("\n")
```

## Test 2 
```python
drevo2 = Drevo(2, levo=Drevo(3, levo=Drevo(6)), desno=Drevo(1, levo=Drevo(7), desno=Drevo(9)))
print("Koren (R: 2)",vrni_koren(drevo2))
print("List (R: False)", je_list(drevo2))
print("Nikoli levo (R: False)", nikoli_levo(drevo2))
print("Visina (R: 3)", visina(drevo2))
print("\n")
```

## Test 3 
```python
drevo3 = Drevo(3, levo=Drevo(4, levo=Drevo(9, levo=Drevo(21))))
print("Koren (R: 3)",vrni_koren(drevo3))
print("List (R: False)", je_list(drevo3))
print("Nikoli levo (R: Flase)", nikoli_levo(drevo3))
print("Visina (R: 4)", visina(drevo3))
print("\n")
```

## Test 4 
```python
drevo4 = Drevo(21, desno=Drevo(77, desno=Drevo(123, desno=Drevo(5))))
print("Koren (R: 21)",vrni_koren(drevo4))
print("List (R: False)", je_list(drevo4))
print("Nikoli levo (R: True)", nikoli_levo(drevo4))
print("Visina (R: 4)", visina(drevo4))
print("\n")
```

## Test 5
```python
drevo5 = Drevo(4)
print("Koren (R: 4)",vrni_koren(drevo5))
print("List (R: True)", je_list(drevo5))
print("Nikoli levo (R: False)", nikoli_levo(drevo5))
print("Visina (R: 1)", visina(drevo5))
```

---

# Viri

1. Cone, M., Markdown Cheat Sheet, pridobljeno s [https://www.markdownguide.org/cheat-sheet/] https://www.markdownguide.org/cheat-sheet/), 30. 9. 2020.