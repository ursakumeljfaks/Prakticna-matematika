#### Tega dela kode ne spreminjaj! ###
with open('B1_kraji.txt', 'r') as datoteka:
    kraji = datoteka.read()
    seznam_krajev = kraji.split(' ')

#### Rešitev piši od tu dalje:
delez = 0
prvi = ""
for kraj in seznam_krajev:
    samoglasniki = "AEIOUaeiou"
    stevilo = 0
    for crka in kraj:
        if crka in samoglasniki:
            stevilo += 1
    if (stevilo / len(kraj)) > delez and stevilo != len(kraj):
        prvi = kraj
        delez = stevilo / len(kraj)
print(prvi)
        