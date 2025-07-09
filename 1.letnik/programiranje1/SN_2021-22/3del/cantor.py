while True:
    try:
        n = float(input())
    except:
        break
    
    stevilo = []
    for i in range(10):
        n = n * 3
        stevilo.append(int(n))
        n -= int(n)

    ali_je = "MEMBER"
    for i in stevilo:
        if i == 1:
            ali_je = "NON-MEMBER"
            break
    
    print(ali_je)

# link do racunala: https://madformath.com/calculators/basic-math/base-converters/decimal-to-base-3-converter-with-steps/decimal-to-base-3-converter-with-steps

