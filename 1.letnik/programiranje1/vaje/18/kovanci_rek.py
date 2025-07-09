import time

def rek_resitev(i, vrednosti):
   '''
      vrne maksimalno vrednost vsote,
      ki jo lahko dobimo iz tabele vrednosti[:i]
      če v vsoti ne smemo imeti sosednjih elementov
    '''
   if i == 1:  # imamo le eno vrednost
      return vrednosti[0]
   if i == 2:  # imamo dve vrednosti
      return max(vrednosti[0], vrednosti[1])
  
   brez = rek_resitev(i - 1, vrednosti) # i-tega ne vzamemo
   z = rek_resitev(i - 2, vrednosti) + vrednosti[i - 1]
                    # i-tega vzamemo
   return max(brez, z)

def opt_vsota(stevila):
    '''Vrne maksimalno vsoto, če ne smemo vzeti sosednjih elementov'''
    return rek_resitev(len(stevila), stevila)

tab = [3, 7, 6, 1, 6, 10, 5, 4, 2, 7, 8, 11, 13, 15, 14]

zacetek = time.time()
for _ in range(100):
    n = opt_vsota(tab)
print(n)
konec = time.time()
print((konec-zacetek)/100)