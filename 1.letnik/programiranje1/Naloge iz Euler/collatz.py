def naslednji_clen(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

def dolzina_zaporedja(n):
    dolzina = 1
    while n != 1:
        n = naslednji_clen(n)
        dolzina += 1
    return dolzina

def najdaljse_zaporedje(m, n):
    dolzina = 0
    for k in range(m, n + 1):
        dolzina = max(dolzina_zaporedja(k), dolzina)
    return dolzina
