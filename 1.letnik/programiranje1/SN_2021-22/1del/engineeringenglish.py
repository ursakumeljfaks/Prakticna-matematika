import sys #omogoča delovanje v terminalu, ker omogoča dostop do spremenljivk in funkcij, ki sodelujejo s terminalom oz. tolmačem

ze_uporabljene_besede = set()
for vrstica in sys.stdin: #metoda stdin interno pokliče metodo input(), prav tako samodejno doda \n po vsakem stavku
    izpis = ""
    for beseda in vrstica.split():
        if beseda.lower() in ze_uporabljene_besede: #če je beseda že nastopila prej, doda pikice
            izpis += "." + " "
        else:
            ze_uporabljene_besede.add(beseda.lower()) #če besede do sedaj še ni bilo jo doda v množico
            izpis += beseda + " " #in doda besedo v izpis
    print(izpis) 