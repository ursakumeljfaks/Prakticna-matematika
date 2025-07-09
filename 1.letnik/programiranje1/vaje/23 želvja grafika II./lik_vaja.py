import turtle

def lik(risar, n, d):
    if n == 0:
        for i in range(4):
            risar.fd(d)
            risar.lt(90)
    else:
        lik(risar, 0, d)
        # pot do drugega
        risar.pu()
        risar.fd(d/3)
        risar.rt(90)
        risar.fd(d/6)
        risar.lt(90)
        risar.pd()
        # 1. kvadrat
        lik(risar, n-1, d/3)
        # pot do 2. kvadrata
        risar.pu()
        risar.fd(d/3)
        risar.lt(90)
        risar.fd(d/6)
        risar.rt(90)
        risar.fd(d/3)
        risar.lt(90)
        risar.fd(d/3)
        risar.lt(90)
        risar.fd(d/6)
        risar.rt(180)
        risar.pd()
        # 2. kvadrat
        lik(risar, n-1, d/3)
        # pot do 3. kvadrata
        risar.pu()
        risar.fd(d/6)
        risar.lt(90)
        risar.fd(2*d/3)
        risar.lt(90)
        risar.fd(2*d/3)
        risar.lt(90)
        risar.fd(d/6)
        risar.lt(90)
        risar.pd()
        # 3. kvadrat
        lik(risar, n-1, d/3)
        # pot do 3. kvadrata
        risar.pu()
        risar.lt(90)
        risar.fd(d/6)
        risar.lt(90)
        risar.fd(d/3)
        risar.lt(90)
        risar.fd(2*d/3)
        risar.rt(90)
        risar.fd(d/6)
        risar.rt(180)
        risar.pd()
        # 4. kvadrat
        lik(risar, n-1, d/3)
        # pot do zacetnega polozaja
        risar.pu()
        risar.fd(d/6)
        risar.rt(90)
        risar.fd(d/3)
        risar.lt(90)
        risar.pd()

zelva = turtle.Turtle()
lik(zelva, 3, 100)