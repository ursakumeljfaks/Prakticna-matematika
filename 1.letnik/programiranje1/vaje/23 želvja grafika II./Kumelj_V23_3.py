import turtle

def zmajnica(zelva, n, a, h):
    """narise zmajnico"""
    if n < 1:
        zelva.fd(h)
        return
    zmajnica(zelva, n-1, 90, h)
    zelva.rt(a)
    zmajnica(zelva, n-1, -90, h)

zelva = turtle.Turtle()
zmajnica(zelva, 10, 30, 5)