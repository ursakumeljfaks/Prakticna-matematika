# moja resitev, ki ni pravilna:
# slovar = dict()
# while True:
#     ime = input()
#     cena = int(input())
#     slovar[ime] = cena
#     if slovar.keys() == "Konec":
#         break
# print(f"Njavec je ponudil (so ponudili): {max(slovar.items())})")



naj_ponudba = -1
ponudniki = [] #tabela tistih, ki so ponudili najvec
while True:
    #preberemo posamezno ponudbo
    ime_ponudnika = input("Vnesi ponudnika (Konec za konec): ")
    if ime_ponudnika == "Konec":
        #zakljucimo
        break
    #preberemo ponudbo
    ponudba = int(input("Koliko ponuja: "))
    #smo dobili boljso ponudbo
    if ponudba > naj_ponudba:
        naj_ponudba = ponudba
        #edini ponudnik s to ponudbo je do sedaj ta ponudnik
        ponudniki = [ime_ponudnika]
    elif ponudba == naj_ponudba:
        ponudniki.append(ime_ponudnika)
#prebrali smo vse podatke
print("Njavec je ponudil (so ponudili):", str(ponudniki)[1:-1])

# test v terminalu vrne:
# Vnesi ponudnika (Konec za konec): Joze
# Koliko ponuja: 100
# Vnesi ponudnika (Konec za konec): Janez
# Koliko ponuja: 50
# Vnesi ponudnika (Konec za konec): Franci
# Koliko ponuja: 1000
# Vnesi ponudnika (Konec za konec): Jaka
# Koliko ponuja: 1000
# Vnesi ponudnika (Konec za konec): Konec
# Njavec je ponudil (so ponudili): 'Franci', 'Jaka'