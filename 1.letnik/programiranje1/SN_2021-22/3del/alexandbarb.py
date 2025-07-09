k, m, n = map(int, input().split())
if k % (n+m) < m: # zmagovalna strategija igra Normal
    print("Barb")
else:
    print("Alex")

# primer: k = 25, m = 3, n = 10 (v zadnjem ciklu se morata na kupčku nahajati 1 ali 2 karti in tako je 
# igralec na potezi izgubil; tisti, ki bo nasprotniku prepustil tako stanje kart bo zmagovalec)
# cikel:                zadnji   predzadnji     predpredzadnji
# št. kart na kupčku:      1     14 = 3+10+1       14+10+3=27    (po tej varianti naj A ne igra, ker izgubi)
# št. kart na kupčku:      2     15 = 3+10+2       15+10+3=28    (A zmaga -> vzame 10 kart da pride do 15, potem pa karkoli B vzame
# bo A kupček izpraznil tako, da ostaneta 2 karti in pripravi B da vzame te 2 in tako zmaga)