n = int(input().split()[0]) # stevilo shopping listkov
# m = int(input().split()[1]) stevilo izdelkov na shopping listku
shopping_listi = set(input().split()) # naredi mnozico vseh vrstic
for vrstica in range(n-1): # skozi vse shopping listke, range zacne z 0
    vrstica1 = input().split() 
    shopping_listi &= set(vrstica1) # primerjamo vsako vrstico posebi kot input (vrstica1) s celotno mnozico inputov shopping_listi
nova_vrstica = "\n"
print(f"{len(shopping_listi)}{nova_vrstica}{nova_vrstica.join(sorted(shopping_listi))}")




