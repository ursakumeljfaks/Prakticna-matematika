import time
zacetek = time.time()
def vr_komb(kombinacija, tab_vr):
    '''Sešteje vrednosti iz tab_vr na tistih mestih,
       kjer je v kombinacija znak 1'''
    vrednost = 0
    for znak, vr in zip(kombinacija, tab_vr):
        if znak == '1':
            vrednost += vr
    return vrednost

def kovanci(tab_vr):
    '''Vrne maksimalni znesek, ki ga lahko
       dobimo iz tab_vr'''
    st_kovancev = len(tab_vr)
    # ustvari vse možne veljavne kombinacije
    naj_k = -1
    for i in range(2**st_kovancev):
        v_dv = bin(i)[2:]
        v_dv = '0' * (5 - len(v_dv)) + v_dv
        if '11' not in v_dv:
            # veljavna kombinacija
            vrednost_kombinacije = vr_komb(v_dv, tab_vr)      
            # print(f'{v_dv} : {vrednost_kombinacije}')
            naj_k = max(vrednost_kombinacije, naj_k)
    return naj_k

tab = [3, 7, 6, 1, 6, 10, 5, 4, 2, 7, 8, 11, 13, 15, 14, 17, 19, 5, 8, 10]
print(kovanci(tab))

konec = time.time()
print(konec-zacetek)