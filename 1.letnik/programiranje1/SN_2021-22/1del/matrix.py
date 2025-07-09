testni_primer = 0
while True:
    testni_primer += 1
    try:
        mesto_1_1, mesto_1_2 = map(int, input().split()) 
    except:
        break
    mesto_2_1, mesto_2_2 = map(int, input().split())
    input()  
    determinanta_je = (mesto_1_1 * mesto_2_2) - (mesto_2_1 * mesto_1_2)
    inverz_1_1 = mesto_2_2 / determinanta_je
    inverz_1_2 = -1 * (mesto_1_2 / determinanta_je)
    inverz_2_1 = -1 * (mesto_2_1 / determinanta_je)
    inverz_2_2 = mesto_1_1 / determinanta_je
    print(f"Case {testni_primer}:\n{int(inverz_1_1)} {int(inverz_1_2)} \n{int(inverz_2_1)} {int(inverz_2_2)}")