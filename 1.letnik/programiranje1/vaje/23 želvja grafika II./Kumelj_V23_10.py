import turtle

def koch(zelva, n, d):
    if n == 0:
        zelva.fd(d)
    else:
        koch(zelva, n-1, d/3)
        zelva.rt(60)
        koch(zelva, n-1, d/3)
        zelva.lt(120)
        koch(zelva, n-1, d/3)
        zelva.rt(60)
        koch(zelva, n-1, d/3)


zelva = turtle.Turtle()
for i in range(6):
    koch(zelva, 3, 100)
    zelva.rt(60)



