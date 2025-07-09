def vr_komb(kombinacija, tab_vr):
    '''Sešteje vrednosti iz tab_vr na tistih mestih,
       kjer je v kombinacija znak 1'''
    vrednost = 0
    for znak, vr in zip(kombinacija, tab_vr):
        if znak == '1':
            vrednost += vr
    return vrednost

def kovanci_naj_kombinacija(tab_vr):
    '''Vrne maksimalni znesek, ki ga lahko
       dobimo iz tab_vr'''
    st_kovancev = len(tab_vr)
    # ustvari vse možne veljavne kombinacije
    naj_k = -1
    for i in range(2**st_kovancev):
        v_dv = bin(i)[2:]
        v_dv = '0' * (st_kovancev - len(v_dv)) + v_dv
        if '11' not in v_dv:
            # veljavna kombinacija
            vrednost_kombinacije = vr_komb(v_dv, tab_vr)      
            # ali imamo boljsega kandidata
            if vrednost_kombinacije > naj_k:
                naj_k = vrednost_kombinacije
                dbest_kom = v_dv # niz najboljse kombinacije do sedaj
    return naj_k, dbest_kom
        


tab = [2, 1, 5, 1, 3, 8, 1, 4, 2, 5]
print(kovanci_naj_kombinacija(tab))