while True:
    n = input()
    if n == "END":
        break

    rezultat = 1 # zaradi tega, ker moramo na koncu upoštevati še dolžino niza "1"
    while n != "1": 
        n = str(len(n)) # od vsakega števila dobimo niz njegove dolžine 
        rezultat += 1 
    print(rezultat)

# n = 42 -> str(len(42)) = "2" (rezultat = 1) -> n = str(len("2")) = "1" (rezultat = 2) -> program se ustavi ampak moramo
# upoštevati še dolžino na koncu od "1", končni rezultat = 3
