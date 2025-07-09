def ali_je_idd(seznam):
    '''preveri ali je dani seznam, ki predstavlja premi pregled, iskalno dvojiško drevo ali ne'''
    if seznam == []:
        return True
    # ker je seznam premi pregled vemo, da je prvi element drevesa ravno koren
    koren = seznam[0]   
    for i in range(1, len(seznam)-1):
        # naletimo na stevilo vecje od korena, ce je naslednje stevilo do tega stevila manjse ali enako od korena to ni idd
        if seznam[i] > koren and seznam[i+1] <= koren:
            return False
    return True

print(ali_je_idd([8,4,2,1,6,5,10,9,30,11])) #True
print(ali_je_idd([1,2,3]))                  #True
print(ali_je_idd([8,10,9,30,11]))           #True
print(ali_je_idd([3,2,1]))                  #True
print(ali_je_idd([3,1,2]))                  #True
print(ali_je_idd([8,4,10,2]))               #False  
print(ali_je_idd([8,4,2,1,6,5,10,7,30,11])) #False
print(ali_je_idd([1,2,4,1]))                #False
print(ali_je_idd([40,30,25,35,30,45,60]))   #True
print(ali_je_idd([25,15,10,4,12,22,18,24,50,35,31,44,70,66,90])) #True
print(ali_je_idd([8,3,1,6,4,7,10,14,2]))    #False

