from KumeljUrsa_vozlanje import Vozel, VerizniSeznam, vstavi_veriga_vozlov, vstavi_verizni_seznam

#VERIGA VOZLOV
print('Veriga Vozlov')
print('==========================================================================================')
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


print('-----------------------------------------------------------------------------------------')
#Primer 2: prazna veriga
print('Primer 2: prazna veriga')
print('')
veriga = None
print('veriga =', '•')

#vstavi število
print('vstavi_veriga_vozlov(veriga, 77)')
veriga = vstavi_veriga_vozlov(veriga, 77)
print(veriga)


print('-----------------------------------------------------------------------------------------')
#Primer 3: en sam element
print('Primer 3: en sam element')
print('')
veriga = Vozel(17)
print('veriga =', veriga)

#vstavi na začetek
print('vstavi_veriga_vozlov(veriga, 5)')
veriga = vstavi_veriga_vozlov(veriga, 5)
print(veriga)

#vstavi na konec
print('')
veriga = Vozel(17)
print('veriga =', veriga)
print('vstavi_veriga_vozlov(veriga, 42)')
veriga = vstavi_veriga_vozlov(veriga, 42)
print(veriga)




print(2*'\n')
#VERIŽNI SEZNAM
print('Verižni Seznam')
print('==========================================================================================')
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


print('-----------------------------------------------------------------------------------------')
#Primer 2: prazen seznam
print('Primer 2: prazen seznam')
print('')
seznam = VerizniSeznam()
print('seznam =', seznam)

#vstavi število
print('vstavi_verizni_seznam(seznam, 77)')
vstavi_verizni_seznam(seznam, 77)
print(seznam)


print('-----------------------------------------------------------------------------------------')
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