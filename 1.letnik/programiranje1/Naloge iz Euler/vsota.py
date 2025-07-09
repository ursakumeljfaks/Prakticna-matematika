def je_prastevilo(n):
    stejmo = 0
    for i in range(1, n+1):
        if n % i == 0:
            stejmo += 1
    if stejmo == 2:
        return 1
    else:
        return 0

x=int(input("Vnesi stevilo: "))
n = 1
c = 0
while(c < x):
    n += 1
    for i in range(2, n+1):
        if n % i == 0:
            break
    if i == n:
        c += 1
print(n)
    
    
