#gre skozi inpute
for i in range(int(input())):
    stopnja_polinoma_1 = int(input())
    koeficienti_polinoma_1 = list(map(int, input().split())) #vsak koeficient bo ločil in naredil tabelo

    stopnja_polinoma_2 = int(input())
    koeficienti_polinoma_2 = list(map(int, input().split()))

    #m = len(koeficienti_polinoma_1)
    #n = len(koeficienti_polinoma_2)
    #produkt = [0] * (m + n - 1)
    #for i in range(m):
    #   for j in range(n):
    #       ostalo naprej enako
    produkt = [0] * (stopnja_polinoma_1 + stopnja_polinoma_2 + 1)
    for i in range(stopnja_polinoma_1+1):
        for j in range(stopnja_polinoma_2+1):
            produkt[i+j] += koeficienti_polinoma_1[i] * koeficienti_polinoma_2[j]
        
    print(f"{stopnja_polinoma_1+stopnja_polinoma_2}")
    print(" ".join(str(stevilo) for stevilo in produkt))

