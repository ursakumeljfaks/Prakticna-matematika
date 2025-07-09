import turtle
import math

def hisa(zelva, dolzina):
    for i in range(4):
        zelva.fd(dolzina)
        zelva.rt(90)
    zelva.lt(45)
    zelva.fd(dolzina/2 * math.sqrt(2))
    zelva.rt(90)
    zelva.fd(dolzina/2 * math.sqrt(2))
    
platno = turtle.Screen()
zelva = turtle.Turtle()
# zelva.fd(100)
hisa(zelva, 100)

platno.exitonclick()