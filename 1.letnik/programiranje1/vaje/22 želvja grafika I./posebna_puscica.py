import turtle

def posebna_puscica(zelva, dolzina):
    # tri perja na koncu puscice
    for i in range(3):
        zelva.pu()
        zelva.fd(dolzina/20)
        zelva.pd()
        zelva.rt(45)
        zelva.fd(dolzina/10)
        zelva.rt(90)
        zelva.fd(dolzina/10)
        zelva.pu()
        zelva.rt(180)
        zelva.fd(dolzina/10)
        zelva.lt(90)
        zelva.fd(dolzina/10)
        zelva.rt(135)
        zelva.fd(dolzina/10)
        zelva.pd()
    # palica puscice
    zelva.pu()
    zelva.rt(45)
    zelva.fd(dolzina/10)
    zelva.lt(45)
    zelva.pd()

    for i in range(7):
        zelva.fd(dolzina/10)
        zelva.pu()
        zelva.fd(dolzina/10)
        zelva.pd()
    
    zelva.pu()
    zelva.lt(135)
    zelva.fd(dolzina/10)
    zelva.rt(180)
    zelva.pd()
    zelva.fd(dolzina/10)
    zelva.rt(90)
    zelva.fd(dolzina/10)

    # da lepse vidimo puscico
    zelva.pu()
    zelva.fd(dolzina)

def puscica_2(zelva, dolzina):
    # tri perja na koncu puscice
    for i in range(3):
        zelva.pu()
        zelva.fd(dolzina/20)
        zelva.pd()
        zelva.rt(45)
        zelva.fd(dolzina/10)
        zelva.rt(90)
        zelva.fd(dolzina/10)
        zelva.pu()
        zelva.rt(180)
        zelva.fd(dolzina/10)
        zelva.lt(90)
        zelva.fd(dolzina/10)
        zelva.rt(135)
        zelva.fd(dolzina/10)
        zelva.pd()
    
    zelva.pu()
    zelva.rt(45)
    zelva.fd(dolzina/10)
    zelva.lt(45)
    zelva.pd()
    # palica
    zelva.fd(dolzina)

    # konec puscice
    zelva.pu()
    zelva.lt(135)
    zelva.fd(dolzina/10)
    zelva.rt(180)
    zelva.pd()
    zelva.fd(dolzina/10)
    zelva.rt(90)
    zelva.fd(dolzina/10)

    # da lepse vidimo puscico
    zelva.pu()
    zelva.fd(dolzina)

def puscica_3(zelva, dolzina):
    # tri perja na koncu puscice
    for i in range(3):
        zelva.pu()
        zelva.fd(dolzina/20)
        zelva.pd()
        zelva.rt(45)
        zelva.fd(dolzina/10)
        zelva.rt(90)
        zelva.fd(dolzina/10)
        zelva.pu()
        zelva.rt(180)
        zelva.fd(dolzina/10)
        zelva.lt(90)
        zelva.fd(dolzina/10)
        zelva.rt(135)
        zelva.fd(dolzina/10)
        zelva.pd()
    
    zelva.pu()
    zelva.rt(45)
    zelva.fd(dolzina/10)
    zelva.lt(45)
    zelva.pd()
    # palica
    zelva.fd(dolzina)

    # obarvan konec
    zelva.begin_fill()
    zelva.pu()
    zelva.lt(135)
    zelva.fd(dolzina/10)
    zelva.rt(180)
    zelva.pd()
    zelva.fd(dolzina/10)
    zelva.rt(90)
    zelva.fd(dolzina/10)
    zelva.rt(135)
    zelva.fd(dolzina/7)
    zelva.end_fill()

    # da lepse vidimo puscico
    zelva.pu()
    zelva.fd(dolzina)


platno = turtle.Screen()
zelva = turtle.Turtle()
puscica_3(zelva, 100)
posebna_puscica(zelva, 100)
puscica_2(zelva, 100)

platno.exitonclick()