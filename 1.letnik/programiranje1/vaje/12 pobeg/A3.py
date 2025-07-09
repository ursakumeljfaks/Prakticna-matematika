def naslednji_clen(n):
    """izracuna naslednji clen Collatzovega zaporedja"""
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

def dolzina_zaporedja(n):
    if n == 1:
        return 1
    else:
        return dolzina_zaporedja(naslednji_clen(n)) + 1

print(1934 - dolzina_zaporedja(1718) + 1)