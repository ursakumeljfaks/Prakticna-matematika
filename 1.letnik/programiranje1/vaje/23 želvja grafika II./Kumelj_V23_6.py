import turtle
def PTS(risar, n, d, barve):
    '''Nariše pobarvan trikotnik Serpinskega.'''
    if n == 0:
        for _ in range(3):
            risar.fd(d)
            risar.lt(120)
        
    else:
        PTS(risar, n-1, d/2, barve[1:])
        risar.pu()
        risar.fd(d/2)
        risar.pd()
        PTS(risar, n-1, d/2, barve[1:])
        risar.lt(120)
        risar.fd(d/2)
        risar.rt(120)
        PTS(risar, n-1, d/2, barve[1:])
        risar.fillcolor(barve[0])
        risar.begin_fill()
        for _ in range(3):
            risar.fd(d/2)
            risar.rt(120)
        risar.end_fill()
        risar.pu()
        risar.rt(120)
        risar.fd(d/2)
        risar.lt(120)
        risar.pd()
    
if __name__ == '__main__':
    špelca = turtle.Turtle()
    PTS(špelca, 4, 300, ['yellow', 'red', 'green', 'black'])