import turtle

def heksa(zelva, dolzina):
    zelva.lt(60)
    for i in range(6):
        zelva.fd(dolzina)
        zelva.rt(60)

def slika(zelva, dolzina):
    # sredinski sestkotnik
    heksa(zelva, dolzina)
    # pot do naslednjega
    zelva.pu()
    zelva.lt(120)
    zelva.fd(dolzina)
    zelva.lt(60)
    zelva.fd(dolzina)
    zelva.lt(120)
    zelva.pd()
    # 1 sestkotnik
    heksa(zelva, dolzina)
    # pot do naslednjega 
    zelva.fd(dolzina)
    zelva.lt(60)
    zelva.fd(dolzina)
    zelva.rt(120)
    # 2 sestkonik
    heksa(zelva, dolzina)
    # pot do naslednjega
    zelva.pu()
    zelva.fd(dolzina)
    zelva.rt(60)
    zelva.fd(dolzina)
    zelva.pd()
    # 3 sestkonik
    heksa(zelva, dolzina)
    # pot do nalsednjega
    zelva.pu()
    zelva.fd(dolzina)
    zelva.rt(60)
    zelva.fd(dolzina)
    zelva.rt(60)
    zelva.fd(dolzina)
    zelva.pd()
    # 4 sestkonik
    heksa(zelva, dolzina)
    # pot do naslednjega
    zelva.pu()
    zelva.fd(dolzina)
    zelva.rt(60)
    zelva.fd(dolzina)
    zelva.rt(60)
    zelva.fd(dolzina)
    zelva.pd()
    # 5 sestkotnik
    heksa(zelva, dolzina)
    # pot do naslednjega
    zelva.pu()
    zelva.fd(dolzina)
    zelva.rt(60)
    zelva.fd(dolzina)
    zelva.rt(60)
    zelva.fd(dolzina)
    zelva.pd()
    # 6 sestkotnik
    heksa(zelva, dolzina)

platno = turtle.Screen()
zelva = turtle.Turtle()
slika(zelva,30)
platno.exitonclick()