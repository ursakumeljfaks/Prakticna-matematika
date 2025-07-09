import turtle

zelva = turtle.Turtle()
platno = turtle.Screen()

def narisi_stranico(zelva, dolzina, n):
    if n == 1:
        zelva.fd(dolzina)
    else:
        zelva.fd(dolzina/3)
        zelva.lt(90)
        zelva.fd(dolzina/3)
        zelva.rt(90)
        narisi_stranico(zelva, dolzina/3, n-1)
        zelva.rt(90)
        zelva.fd(dolzina/3)
        zelva.lt(90)
        zelva.fd(dolzina/3)
        
for i in range(4):
    narisi_stranico(zelva, 100, 5)
    zelva.rt(90)

platno.exitonscreen()