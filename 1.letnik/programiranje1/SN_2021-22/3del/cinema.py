# N = število sedežev, M = število skupin od 1-10 ljudi je v njej
N, M = map(int, input().split())

skupine = list(map(int, input().split()))

izpadlih = 0
for skupina in skupine:
    # v primeru, da je večja sploh ne pride v poštev
    if skupina > N:
        izpadlih += 1
    # ce pa je v redu, jo upoštevamo in samo zmanjšamo število sedežev
    else:
        N -= skupina
print(izpadlih)




