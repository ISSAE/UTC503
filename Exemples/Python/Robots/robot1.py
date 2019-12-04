#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Robot:
    """ Robot qui sait avancer d'une case et pivoter à droite de 90°.
        Il est repéré par son abscisse x, son ordonnée y et sa direction.
    """
    def _nomDirection(idDirection):
        return 'nord est sud ouest'.split()[idDirection]

    def _idDirection(nomDirection):
        return ' nord est sud ouest'.split().index(nomDirection)

    def __init__(self, x, y, direction):
        """ Initialiser le robot self à partir de sa position (x, y) et sa direction. """
        self.x = x
        self.y = y
        self.direction = Robot._idDirection(direction)

    def avancer(self):
        """ Avancer d'une case dans la direction. """
        # mettre à jour self.x
        if self.direction == 1: # est
            self.x += 1
        elif self.direction == 3: # ouest
            self.x -= 1
        # mettre à jour self.y
        if self.direction == 0: # nord
            self.y += 1
        elif self.direction == 2: # sud
            self.y -= 1

    def pivoter(self):
        """ Pivoter ce robot de 90° vers la droite. """
        self.direction = (self.direction + 1) % 4

    def afficher(self, prefix=''):
        print(f"{prefix}Robot(x={self.x}, y={self.y}, direction={Robot._nomDirection(self.direction)})")

# Exemple et test
if __name__ == '__main__':
    r1=Robot(4,10,'est')
    r1.afficher(prefix='r1 = ')
    r2 = Robot(15, 7, 'sud')
    r2.afficher(prefix='r2 = ')
    r1.pivoter()
    r1.afficher(prefix='pivoter r1 = ')
    r2.avancer()
    r2.afficher(prefix='avancer r2 = ')
    #Utilisation comme fonction dans un namespace ... 
    Robot.pivoter(r2)
    Robot.afficher(r2, prefix='r2 = ')
    print('Robot.pivoter :', Robot.pivoter)
    print('r2.pivoter :', r2.pivoter)


    




