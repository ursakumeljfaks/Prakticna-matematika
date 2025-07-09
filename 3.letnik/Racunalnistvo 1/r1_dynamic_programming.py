def largestSumArray(array):
    '''vrne največjo vsoto v podseznamu seznama array'''
    najvecja_vsota = array[0]
    vsota_do_sedaj = array[0]

    for i in array[1:]:
        vsota_do_sedaj = max(i, vsota_do_sedaj + i)
        najvecja_vsota = max(najvecja_vsota, vsota_do_sedaj)
    return najvecja_vsota

print(largestSumArray([-6,12,-7,0,14,-7,5]))

# i = 12: vsota_do_sedaj = max(12, -6+12=6) = 12, najvecja_vsota = max(-6, 12) = 12
# i = -7: vsota_do_sedaj = max(-7, 12-7=5) = 5, najvecja_vsota = max(12, 5) = 12
# i = 0: vsota_do_sedaj = max(0, 5+0=12) = 5, najvecja_vsota = max(12, 5) = 12
# i = 14: vsota_do_sedaj = max(14, 5+14=19) = 19, najvecja_vsota = max(12, 19) = 19
# i = -7: vsota_do_sedaj = max(-7, 19-7=12) = 12, najvecja_vsota = max(19, 12) = 19
# i = 5: vsota_do_sedaj = max(5, 12+5=17) = 17, najvecja_vsota = max(19, 17) = 19

def largestProductArray(array):
    '''vrne največji produkt v podseznamu seznama array'''
    najvecji_produkt = array[0]
    produkt_do_sedaj = array[0]

    for i in array[1:]:
        produkt_do_sedaj = max(i, produkt_do_sedaj * i)
        najvecji_produkt = max(najvecji_produkt, produkt_do_sedaj)
    return najvecji_produkt

