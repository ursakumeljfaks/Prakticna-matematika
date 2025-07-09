import turtle

def preproga(risar, n, d):
    """narise preprogo Sierpinskega"""
    if n == 0:
        for i in range(4):
            risar.fd(d)
            risar.lt(90)
        return
    # notranji polni kv.
    risar.fd(d/3)
    risar.lt(90)
    risar.fd(d/3)
    risar.rt(90)
    risar.begin_fill()
    for _ in range(4):
        risar.fd(d/3)
        risar.lt(90)
    risar.end_fill()
    risar.bk(d/3)
    risar.rt(90)
    risar.fd(d/3)
    risar.lt(90)    
    # 1 kvadrat
    preproga(risar, n-1, d/3)
    risar.pu()
    risar.fd(d/3)
    risar.pd()
    # 2 kvadrat
    preproga(risar, n-1, d/3)
    risar.pu()
    risar.fd(d/3)
    risar.pd()
    #3 kvadrat
    preproga(risar, n-1, d/3)
    risar.pu()
    risar.lt(90)
    risar.fd(d/3)
    risar.rt(90)
    risar.pd()
    # 4 kvadrat
    preproga(risar, n-1, d/3)
    risar.pu()
    risar.lt(90)
    risar.fd(d/3)
    risar.rt(90)
    risar.pd()
    # 5 kvadrat
    preproga(risar, n-1, d/3)
    risar.pu()
    risar.lt(180)
    risar.fd(d/3)
    risar.rt(180)
    risar.pd()
    # 6 kvadrat
    preproga(risar, n-1, d/3)
    risar.pu()
    risar.lt(180)
    risar.fd(d/3)
    risar.rt(180)
    risar.pd()
    # 7 kvadrat
    preproga(risar, n-1, d/3)
    risar.pu()
    risar.rt(90)
    risar.fd(d/3)
    risar.lt(90)
    risar.pd()
    preproga(risar, n-1, d/3)
    # nazaj na zacetni polozaj
    risar.pu()
    risar.rt(90)
    risar.fd(d/3)
    risar.lt(90)
    risar.pd()

zelva = turtle.Turtle()
preproga(zelva, 3, 300)
            