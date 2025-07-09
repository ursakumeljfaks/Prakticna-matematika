def je_prastevilo(n):
    stej = 0
    i = 2
    while i <= (n//2):
        if n % i == 0:
            stej += 1
            break
        i += 1
    if stej == 0 and n != 1:
        return True
    else:
        return False
    
def vsota_prastevil(n):
    vsota = 0
    for stevilo in range(2, n+1):
        i = 2
        for i in range(2, stevilo):
            if int(stevilo % i == 0):
                i = stevilo
                break
        if i is not stevilo:
            vsota += stevilo
    return vsota