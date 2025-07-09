stevilo1 = int(input("Vnesi število: "))
print(stevilo1)
stevilo2 = int(input("Vnesi število: "))
print(stevilo1*stevilo2)
while stevilo1 * stevilo2 <= 100:
    stevilo3 = int(input("Vnesi število: "))
    stevilo2 * stevilo3
    if stevilo1 == 0 or stevilo2 == 0 or stevilo3 == 0:
        print(0)
    break
print("To je pa prevec!")


#resitev
produkt = 1
while True:
    stevilo = int(input("vnesi število: "))
    produkt *= stevilo
    if produkt > 100:
        print("To je prevec!")
        break
    print(produkt)
    if produkt == 0:
        break

# test v terminualu vrne:
# Vnesi stevilo: 5
# 5
# Vnesi stevilo: 3
# 15
# Vnesi stevilo: 7
# To je pa prevec!