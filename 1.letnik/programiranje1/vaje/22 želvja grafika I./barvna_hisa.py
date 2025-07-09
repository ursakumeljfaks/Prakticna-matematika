import turtle
import math


def hisa(zelva, dolzina, barva_strehe, barva_fasade):
    zelva.color(barva_fasade)
    zelva.begin_fill()
    for i in range(4):
        zelva.fd(dolzina)
        zelva.rt(90)
    zelva.end_fill()
    zelva.color(barva_strehe)
    zelva.begin_fill()
    zelva.lt(45)
    zelva.fd(dolzina/2 * math.sqrt(2))
    zelva.rt(90)
    zelva.fd(dolzina/2 * math.sqrt(2))
    zelva.end_fill()
    zelva.pu()
    zelva.lt(45)
    zelva.fd(dolzina)
    


platno = turtle.Screen()
zelva = turtle.Turtle()
hisa(zelva, 40, "blue", "green")
platno.exitonclick()