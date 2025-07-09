from merilnik import izmeri_cas, oceni_potreben_cas, narisi_in_pokazi_graf, izpisi_case, primerjava_dveh_funkcij, test_gen_sez, izvoz_podatkov

def urejanje_z_ustavlanjem(seznam):
    '''vrne urejen seznam z metodo urejanje z ustavljanjem'''
    i = 1
    while i < len(seznam):
        j = i 
        while j > 0 and seznam[j-1] > seznam[j]:
            seznam[j-1], seznam[j] = seznam[j], seznam[j-1]
            j -= 1
        i += 1
    return seznam
# print(urejanje_z_ustavlanjem([6,5,3,1,8,7,2,4]))

def urejenaje_z_zlivanjem(seznam):
    '''vrne urejen seznam z metodo urejanje z zlivanjem'''
    if len(seznam) > 1:
        
        n = len(seznam) // 2
        leva = seznam[:n]
        desna = seznam[n:]

        urejenaje_z_zlivanjem(leva)
        urejenaje_z_zlivanjem(desna)

        i = j = k = 0
        while i < len(leva) and j < len(desna):
            if leva[i] <= desna[j]:
                seznam[k] = leva[i]
                i += 1
            else:
                seznam[k] = desna[j]
                j += 1
            k += 1

        while i < len(leva):
            seznam[k] = leva[i]
            i += 1
            k += 1
            
        while j < len(desna):
            seznam[k] = desna[j]
            j += 1
            k += 1
        return seznam
# print(urejenaje_z_zlivanjem([6,5,3,1,8,7,2,4]))
        

if __name__ == '__main__':
    # izvoz_podatkov(urejenaje_z_zlivanjem, 'ustavlanje_obraten.txt', lambda x: list(range(x)), [i * 10 for i in range(1, 51)], k=100)
    print(izpisi_case(urejanje_z_ustavlanjem, test_gen_sez, [i * 10 for i in range(3201)], k=1))
    # narisi_in_pokazi_graf(urejanje_z_ustavlanjem, test_gen_sez, [i * 10 for i in range(1, 11)], k=100)
    # primerjava_dveh_funkcij([urejanje_z_ustavlanjem, urejenaje_z_zlivanjem], test_gen_sez, [i * 10 for i in range(1, 51)], k=100)