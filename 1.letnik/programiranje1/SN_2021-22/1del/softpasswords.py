
S = input()
P = input()

#druga točka pogoja, da "prependamo"/pripnemo prvotnemu P število od 0-9
druga_tocka = [] 
for i in range(10):
    druga_tocka.append(str(i)+P)

#tretja točka pogoja, da "appendamo"/dodamo na koncu prvotnemu P število od 0-9
tretja_tocka = [] 
for i in range(10):
    tretja_tocka.append(P+str(i))

#sprejem, če sta enaka
if S == P: 
    print("Yes")
#swapcase() zamnja vse male crke z velikimi in obratno, to je 4. pogoj
elif S.swapcase() == P: 
    print("Yes")
elif S in druga_tocka:
    print("Yes")
elif S in tretja_tocka:
    print("Yes")
else:
    print("No")