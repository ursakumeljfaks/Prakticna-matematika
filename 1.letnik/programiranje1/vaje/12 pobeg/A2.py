def je_prastevilo(n):
    """vrne true, ce je n prastevilo in false drugace"""
    if n == 1:
        return False
    for stevilo in range(2, n-1):
        if n % stevilo == 0:
            return False
    return True

def prastevila_ki_delijo(a):
    """prastevila, ki delijo to stevilo a"""
    seznam = []
    if a == 0:
        return 0
    for stevilo in range(1, a):
        if je_prastevilo(stevilo):
            if a % stevilo == 0:
                seznam.append(stevilo)
    return seznam

def vsota_prastevil(seznam):
    vsota = 0
    for stevilo in seznam:
        vsota += stevilo
    return vsota

print(vsota_prastevil(prastevila_ki_delijo(25395793920000))) #17

def stevilo_b(b):
    vsota = 0
    pomnozeno_100 = b * 100
    razlika = pomnozeno_100 - b
    for stevilo in str(razlika):
        vsota += int(stevilo) 
    return vsota

print(stevilo_b(99)) #18

#resitev = 1718

