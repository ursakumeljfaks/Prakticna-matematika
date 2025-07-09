def najvec(stevila):
    '''koliko je najvecja vsota dobljena iz
       tabele stevila, ce ne smemo izbrati dveh
       zaporednih elementov'''
    
    return najvecja_vsota(len(stevila), stevila)

def najvecja_vsota(i, tab):
    '''Vrne najvecjo vsoto iz prvih i elementov
       tabele tab, ce ne smemo vzeti dveh sosednjih'''
    if i == 0:  # ni nobenih števil
        return (0, "")
    if i == 1:  # imamo le eno število
        return (tab[0], "1")
    
    if i == 2:# imamo dve števili
        if tab[0] > tab[1]:
            return (tab[0], "10")
        else:
            return (tab[1], "01")
    
    rez_im2 = najvecja_vsota(i - 2, tab)
    rez_im1 = najvecja_vsota(i - 1, tab)
    vr_z = tab[i-1] + rez_im2[0]
    vr_brez = rez_im1[0]
    if vr_z > vr_brez:
        return (vr_z, rez_im2[1] + "01")
    else:
        return (vr_z, rez_im1[1] + "0")