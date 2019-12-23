import turtle



def _fract1(turt, taille,min):
    if (taille<=min): turt.forward(taille)
    else:
        _fract1(turt, taille/3,min)
        turt.left(60)
        _fract1(turt, taille/3,min)
        turt.right(120)
        _fract1(turt, taille/3,min)
        turt.left(60)
        _fract1(turt, taille/3,min)

def fract1(taille, min=5):
    t=turtle.Turtle()
    t.goto(-taille/2,0)
    _fract1(t,taille,min)
    t.done()

fract1(500)

