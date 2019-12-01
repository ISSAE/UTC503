# -*- coding: utf-8 -*-

import math

"""Exemple méthodes magique:
Les méthodes magiques (également appelées dbr comme
abréviation de double-trait de soulignement) 
en Python ont un objectif similaire à la surcharge d'opérateurs 
dans d'autres langages. Ils permettent à une classe de définir 
son comportement lorsqu'elle est utilisée comme opérande dans 
des expressions d'opérateur unaires ou binaires. 
Ils servent également d'implémentations appelées par certaines 
fonctions intégrées.
"""

class Vecteur:
    # instantiation
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # unary negation (-v)
    def __neg__(self):
        return Vecteur(-self.x, -self.y)

    # addition (v + u)
    def __add__(self, other):
        return Vecteur(self.x + other.x, self.y + other.y)

    # subtraction (v - u)
    def __sub__(self, other):
        return self + (-other)

    # equality (v == u)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # abs(v)
    def __abs__(self):
        # sqrt(x**2+y**2)
        return math.hypot(self.x, self.y)

    # str(v)
    def __str__(self):
        return '<{0.x}, {0.y}>'.format(self)

    # repr(v)
    def __repr__(self):
        return 'Vecteur({0.x}, {0.y})'.format(self)