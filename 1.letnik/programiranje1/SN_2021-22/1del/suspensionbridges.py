import math

d, s = map(int, input().split()) #če dela na spodnji način moram potem spodaj spreminjati vrednosti iz str v int
#d_in_s = str(input())
#d = d_in_s.split(" ")[0]
#s = d_in_s.split(" ")[1] 

#delamo po metodi bisekcije, izberemo zacetno in koncno vrednost med katerima naj bi se nahajala ničla
#zgornjo in spodnjo mejo sem določila s probavanjem, saj mora imeti "funkcija" na zgornji meji pozitivno
#vrednost, na spodnji meji pa negativno vrednost (to je metoda bisekcije)
zgornja_meja = 10000000000
spodnja_meja = 0.0000000001
while zgornja_meja - spodnja_meja > 0.0000000001:
    a = (zgornja_meja + spodnja_meja) / 2
    if (a + s) < (a * math.cosh(d / (2*a))):
        spodnja_meja = a 
    else:
        zgornja_meja = a

print(2 * a * math.sinh(d / (2*a)))
