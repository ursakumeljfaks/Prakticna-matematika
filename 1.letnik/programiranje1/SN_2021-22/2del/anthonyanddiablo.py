import math

A, N = map(float, input().split())
# obseg = 2 * pi * r, od tukaj lahko izracunamo maksimalen r iz materiala N, ki ga imamo
r = N / (2 * math.pi)
# povrsina = pi * (r ** 2), ki jo lahko ustavrimo s tem radijem r, dobljenim iz materiala N
S = math.pi * (r ** 2)
if A <= S:
    print("Diablo is happy!")
else:
    print("Need more materials!")

