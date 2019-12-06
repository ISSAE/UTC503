#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Robot:
    """ Robot qui sait avancer d'une case et pivoter à droite de 90°.
        Il est repéré par son abscisse x, son ordonnée y et sa direction.
    """
    _directions=('nord', 'est', 'sud', 'ouest') # Direction en claire attribut de classe
    _dx = (0, 1, 0, -1) # incrément sur X en fonction de la direction pour éviter le if
    _dy = (1, 0, -1, 0) # incrément sur Y en fonction de la direction pour éviter le if

    def _nomDirection(idDirection):
        return Robot._directions[idDirection]

    def _idDirection(nomDirection):
        return Robot._directions.index(nomDirection)

    def __init__(self, x, y, direction):
        """ Initialiser le robot self à partir de sa position (x, y) et sa direction. """
        self.x = x
        self.y = y
        self.direction = Robot._idDirection(direction)

    # l'utilisation de _dx et _dx facilite cette méthode
    def avancer(self):
        """ Avancer d'une case dans la direction. """
        self.x += Robot._dx[self.direction]
        self.y += Robot._dy[self.direction]

    def pivoter(self):
        """ Pivoter ce robot de 90° vers la droite. """
        self.direction = (self.direction + 1) % 4

    def afficher(self, prefix=''):
        print(f"{prefix}Robot(x={self.x}, y={self.y}, direction={Robot._nomDirection(self.direction)})")

# Exemple et test
if __name__ == '__main__':
    r1=Robot(4,10,'est')
    assert r1.x==4 and r1.y==10 and r1.direction==1
    r1.afficher(prefix='r1 = ')
    r2 = Robot(15, 7, 'sud')
    assert r2.x==15 and r2.y==7 and r2.direction==2
    r2.afficher(prefix='r2 = ')
    r1.pivoter()
    assert r1.x==4 and r1.y==10 and r1.direction==2
    r1.afficher(prefix='pivoter r1 = ')
    r2.avancer()
    assert r2.x==15 and r2.y==6 and r2.direction==2
    r2.afficher(prefix='avancer r2 = ')
    #Utilisation comme fonction dans un namespace ... 
    Robot.pivoter(r2)
    Robot.afficher(r2, prefix='r2 = ')
    print('Robot.pivoter :', Robot.pivoter)
    print('r2.pivoter :', r2.pivoter)


    




