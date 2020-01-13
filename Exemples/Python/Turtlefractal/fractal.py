import turtle,random,sys


_color=('black', 'red', 'blue', 'yellow', 'purple', 'cyan', 'Burlywood', 'Aquamarine')
def getColor():
    return _color[random.randrange(0,7)]

def _fract1(turt, taille,min):
    if (taille<=min):
        turt.color(getColor())
        turt.forward(taille)
    else:
        _fract1(turt, taille/3,min)
        turt.left(60)
        _fract1(turt, taille/3,min)
        turt.right(120)
        _fract1(turt, taille/3,min)
        turt.left(60)
        _fract1(turt, taille/3,min)


def fract1(taille, min=5):
    ''' Taille initiale du segment
        min taille d'arret du fractal
    '''
    t=turtle.Turtle()
    t.pensize(3)
    t.up()
    t.goto(-taille/2,0)
    t.down()
    _fract1(t,taille,min)

taille=1000
min=25
if len(sys.argv) ==  2:
   taille=int(sys.argv[1])
   min=int(sys.atgv[2])


fract1(taille,min)
input("Une touche pour terminer")

