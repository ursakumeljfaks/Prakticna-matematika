def h(n):
    """ali je stevilo harshadovo"""
    a = n #nastavimo nek drug parameter za stevilo n, ker se bo drugace n konstantno spreminjal
    imenovalec = 0
    while n != 0:
        b = n % 10 #enice stevila n
        imenovalec += b #damo v imenovalec 
        n //= 10 #gledamo naslednje desetice, stotice, ...
    if (a % imenovalec == 0): #preverimo ali je stevilo deljivo z vsoto njenih stevk
        return True
    else:
        return False

spodnja = int(input("Spodnja meja: ")) #10
zgornja = int(input("Zgornja meja: ")) #40
produkt = 1
for stevilo in range(spodnja, zgornja+1):
    if h(stevilo) == True:
        produkt *= stevilo
        print(stevilo, produkt)
