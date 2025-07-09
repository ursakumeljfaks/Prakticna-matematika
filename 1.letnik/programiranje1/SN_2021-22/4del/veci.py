import itertools
stevilo = input()
tabela = []
stevila = []

# naredi vse permutacije posameznega stevila, join rabis ker permutations dela nabor
for i in itertools.permutations(stevilo):
    stevila.append(int("".join(i)))

for posamezno_stevilo in stevila:
    if posamezno_stevilo > int(stevilo):
        tabela.append(posamezno_stevilo)

if len(tabela) > 0:
    print(min(tabela))
else:
    print(0) 
