import turtle

def antena(risar, n, d):
    if n == 0:
        risar.bk(d/2)
        risar.fd(d)
        risar.bk(d/2)
        return
    
    risar.fd(d/2)
    risar.rt(90)
    antena(risar, n-1, 0.75*d)

    risar.lt(90)
    risar.bk(d)
    risar.rt(90)
    antena(risar, n-1, 0.75*d)

    risar.lt(90)
    risar.fd(d/2)

if __name__ == "__main__":
    jaka = turtle.Turtle()
    antena(jaka, 4, 200)
