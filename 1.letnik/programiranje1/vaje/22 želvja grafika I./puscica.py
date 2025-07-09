import turtle

def puscica(zelva, dolzina):
    zelva.fd(dolzina)
    zelva.lt(90)
    zelva.fd(dolzina/2)
    zelva.rt(135)
    zelva.fd(dolzina)
    zelva.rt(90)
    zelva.fd(dolzina)
    zelva.rt(135)
    zelva.fd(dolzina/2)
    zelva.lt(90)
    zelva.fd(dolzina)
    zelva.rt(90)
    zelva.fd(dolzina/2 - 9)



platno = turtle.Screen()
zelva = turtle.Turtle()

puscica(zelva, 100)
puscica(zelva, 200)
puscica(zelva, 150)

platno.exitonclick()