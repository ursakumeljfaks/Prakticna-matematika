import turtle

def Pean(zelva, n, a, h):
    """narise peanovo krivuljo"""
    if n == 0:
        return
    zelva.rt(a)
    Pean(zelva, n-1, -a, h)
    zelva.fd(h)
    Pean(zelva, n-1, a, h)
    zelva.fd(h)
    Pean(zelva, n-1, -a, h)
    zelva.lt(a)

zelva = turtle.Turtle()
Pean(zelva, 6, 90, 10)