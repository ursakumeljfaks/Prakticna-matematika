import turtle

def belokranjski_kvadrat(zelva, n, d):
    if n == 0:
        for i in range(4):
            zelva.fd(d)
            zelva.lt(90)
    else:
        # 1 kvadrat
        belokranjski_kvadrat(zelva, n-1, d/3)
        # pot do naslednjega
        zelva.pu()
        zelva.fd(2*d/3)
        zelva.pd()
        # 2 kvadrat
        belokranjski_kvadrat(zelva, n-1, d/3)
        # pot do naslednjega
        zelva.pu()
        zelva.lt(90)
        zelva.fd(2*d/3)
        zelva.rt(90)
        zelva.pd()
        # 3 kvadrat
        belokranjski_kvadrat(zelva, n-1, d/3)
        # pot do naslednjega
        zelva.pu()
        zelva.lt(180)
        zelva.fd(d/3)
        zelva.rt(90)
        zelva.pd()
        # 4 kvadrat
        belokranjski_kvadrat(zelva, n-1, d/3)
        # pot do naslednjega
        zelva.pu()
        zelva.rt(180)
        zelva.fd(d/3)
        zelva.lt(90)
        zelva.pd()
        # 5 kvadrat
        belokranjski_kvadrat(zelva, n-1, d/3)
        # pot na zacetni polozaj
        zelva.pu()
        zelva.rt(90)
        zelva.fd(d/3)
        zelva.rt(90)
        zelva.fd(d/3)
        zelva.rt(180)
        zelva.pd()


zelva = turtle.Turtle()
belokranjski_kvadrat(zelva, 4, 300)
