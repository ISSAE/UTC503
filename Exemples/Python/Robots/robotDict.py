#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Modèle très limité de robot qui ne sait qu'avancer d'une
    case et pivoter à droite de 90°. Il est repéré par son abscisse x,
    son ordonnée y et sa direction (un entier dans 0..3).
'''

_directions = ('nord', 'est', 'sud', 'ouest') # direction en clair
_dx = (0, 1, 0, -1) # incrément sur X en fonction de la direction
_dy = (1, 0, -1, 0) # incrément sur Y en fonction de la direction

def robot(x, y, direction):
    """ Créer un nouveau robot. définit par position x,y et direction"""
    return { 'x': x, 'y': y, 'direction': _directions.index(direction) }

def avancer(r):
    """ Avancer le robot r d'une case en fonction de la direction courante. """
    direction = r['direction']
    r['x'] += _dx[direction]
    r['y'] += _dy[direction]

def pivoter(r):
    """ Pivoter de 90° à droite le robot r. """
    r['direction'] = (r['direction'] + 1) % 4

def afficher(r, prefix=''):
    """ Afficher le robot r. """
    print(f"{prefix}Robot(x={r['x']}, y={r['y']}, direction={_directions[r['direction']]})")
