testni_primer = 0
while True:
    testni_primer += 1
    try:
        stevilo1, stevilo2 = map(int, input().split())
    except:
        break
    razlika = abs(stevilo1 - stevilo2)
    print(f"{razlika}")