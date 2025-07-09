def kara(n):
    """izrise karo visoko 2n-1 vrstic"""
    for vrstica in range(n):
        print(" " * (n - vrstica) + "*" * (2 * vrstica - 1))
    for vrstica in range(n-1, -1, -1):
        print(" " * (n - vrstica) + "*" * (2 * vrstica - 1))

print(kara(10))