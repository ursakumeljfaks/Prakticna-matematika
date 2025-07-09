import turtle

def puscica(zelva, dolzina, barva):
    zelva.color(barva)
    zelva.begin_fill()
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
    zelva.end_fill()




platno = turtle.Screen()
zelva = turtle.Turtle()
puscica(zelva, 100, "green")
platno.exitonclick()