def maxSum(seznam):
    '''vrne največjo vsoto podseznama'''
    rezultat = 0
    for i in range(len(seznam)):
        for j in range(i + 1, len(seznam)):
            vsota = 0
            for k in range(i, j + 1):
                vsota += seznam[k]
            rezultat = max(vsota, rezultat)
    return rezultat

# print(maxSum([-6,12,-7,0,14,-7,5]))


def kadane(seznam):
    '''vrne največjo vsoto podseznama'''
    maxVsota = 0
    trenutnaVsota = 0
    for i in range(len(seznam)):
        trenutnaVsota = max(seznam[i], trenutnaVsota + seznam[i])
        maxVsota = max(maxVsota, trenutnaVsota)
    return maxVsota


print(kadane([-6,-12,-303]))

def kadane2(seznam):
    '''vrne največjo vsoto podseznama'''
    maxVsota = 0
    trenutnaVsota = 0
    
    for i in range(len(seznam)):
        print("število: ", seznam[i], "trenutnaVsotaPrej = ", trenutnaVsota, end="")
        trenutnaVsota = max(seznam[i], trenutnaVsota + seznam[i])

        maxVsota = max(maxVsota, trenutnaVsota)
        print("trenutanVsotaNova = ", trenutnaVsota, "maxVsota = ", maxVsota)
    return maxVsota

# print(kadane2([-3,10,-9,80,-75,3,-10,20,41,3,-7,81,203,17,-306,-33]))

def maxPodukt(seznam):
    '''vrne največji produkt podseznama'''
    rezultat = 0
    for i in range(len(seznam) - 1):
        for j in range(i + 1, len(seznam)):
            prod = 1
            for k in range(i, j + 1):
                prod *= seznam[k]
            rezultat = max(rezultat, prod)
    return rezultat

print(maxPodukt([-3,10,-9,80,-75,3,-10,20,41,3,-7,81,203,17,-306,-33]))

def produktKadane(seznam):
    '''vrne največji produkt podseznama s pomočjo Kadanovega algoritma'''
    lokalni_min = 1
    lokalni_max = 1
    globalni_max = 1

    for i in range(len(seznam)):
        if seznam[i] < 0:
            lokalni_max, lokalni_min = lokalni_min, lokalni_max
        lokalni_max = max(seznam[i], seznam[i] * lokalni_max)
        lokalni_min = min(seznam[i], seznam[i] * lokalni_min)
        globalni_max = max(globalni_max, lokalni_max)
    return globalni_max

print(produktKadane([14,-7,5,0,-6, 12, -7]))

print(maxPodukt([14,-7,5,0,-6, 12, -7]))


