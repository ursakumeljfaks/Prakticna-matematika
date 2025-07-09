import sys

razdalja = 0
prejsnji_cas = 0
prejsnja_hitrost = 0

for vrstica in sys.stdin:
    vrstica1 = vrstica.split()

    zdejsnji_cas = vrstica1[0].split(":")
    zdejsnji_cas = int(zdejsnji_cas[0]) * 3600 + int(zdejsnji_cas[1]) * 60 + int(zdejsnji_cas[2])

    if len(vrstica1) == 2:
        preteceni_cas = zdejsnji_cas - prejsnji_cas
        hitrost = float(vrstica1[1])
        razdalja += prejsnja_hitrost * preteceni_cas
        prejsnja_hitrost = hitrost
    
    else:
        preteceni_cas = zdejsnji_cas - prejsnji_cas
        razdalja += prejsnja_hitrost * preteceni_cas
        pot = (razdalja / 3600)
        # {pot:.2f} je formatni niz, ki bo na izracunani pot-i zaokrozil na dve decimalki, v vseh primerih bosta dve 0
        print(f'{vrstica1[0]} {pot:.2f} km')

    prejsnji_cas = zdejsnji_cas
    

    
    

    
    