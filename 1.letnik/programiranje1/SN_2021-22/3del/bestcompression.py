while True:
    try:
        N, b = map(int, input().split())
    except:
        break
    if N < 2 ** (b+1):
        print("yes")
    else:
        print("no")


        