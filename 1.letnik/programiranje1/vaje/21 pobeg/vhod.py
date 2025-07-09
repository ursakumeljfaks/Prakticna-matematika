with open("kamere.txt", encoding="UTF-8") as dat:
    slovar = {}
    for vrstica in dat:
        ime = vrstica.split("_")[0]
        pomembnost = vrstica.split("_")[1]
        podatek = slovar.get(ime, "Nimamo")
        if podatek == "Nimamo":
            slovar[ime] = 0
        slovar[ime] += int(pomembnost)
rezultat = []
for k, p in slovar.items():
    rezultat.append((p, k))

rezultat.sort(reverse = True)
for pomb, ime in rezultat[:3]:
    print(f"{ime}{pomb}")

