import turtle

def drevo(zelva, d):
    
    zelva.fillcolor('brown')
    zelva.lt(90)

    zelva.begin_fill()
    zelva.fd(d)
    zelva.rt(90)
    zelva.fd(25)
    zelva.rt(90)
    zelva.fd(d)
    zelva.rt(90)
    zelva.fd(25)
    zelva.rt(90)
    zelva.fd(d)
    zelva.end_fill()

    zelva.fillcolor('green')
    zelva.begin_fill()
    zelva.circle(40)  # 25
    zelva.end_fill()

    zelva.pu()
    zelva.rt(90)
    zelva.fd(3)
    zelva.pd()
    zelva.begin_fill()
    zelva.circle(45) # 30
    zelva.end_fill()
    

    zelva.pu()
    zelva.rt(90)
    zelva.fd(3)
    zelva.pd()
    zelva.begin_fill()
    zelva.circle(45) # 30
    zelva.end_fill()

    zelva.pu()
    zelva.lt(180)
    zelva.fd(20)
    zelva.rt(90)
    zelva.fd(30)
    zelva.pd()
    zelva.begin_fill()
    zelva.circle(35) # 20
    zelva.end_fill()

    zelva.pu()
    zelva.lt(120)
    zelva.fd(3)
    zelva.pd()
    zelva.begin_fill()
    zelva.circle(40)
    zelva.end_fill()

    zelva.pu()
    zelva.lt(60)
    zelva.fd(2)
    zelva.fillcolor("red")
    zelva.begin_fill()
    zelva.circle(10)
    zelva.end_fill()  

    zelva.pu()
    zelva.lt(120)
    zelva.fd(50)
    zelva.begin_fill()
    zelva.circle(10)
    zelva.end_fill()  

    
    zelva.rt(170)
    zelva.fd(80)
    zelva.begin_fill()
    zelva.circle(10)
    zelva.end_fill()

    zelva.lt(120)
    zelva.fd(60)
    zelva.begin_fill()
    zelva.circle(10)
    zelva.end_fill()

    zelva.rt(90)
    zelva.fd(40)
    zelva.begin_fill()
    zelva.circle(10)
    zelva.end_fill()

    zelva.rt(130)
    zelva.fd(110)
    zelva.begin_fill()
    zelva.circle(10)
    zelva.end_fill()

    zelva.lt(120)
    zelva.fd(60)
    zelva.begin_fill()
    zelva.circle(10)
    zelva.end_fill()

platno = turtle.Screen()
zelva = turtle.Turtle()
drevo(zelva, 200)


platno.exitonclick()
