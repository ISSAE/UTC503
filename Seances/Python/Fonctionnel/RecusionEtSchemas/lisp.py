''' 
Définition des primitives de liste à la lisp
'''
creer  = lambda  : []
null   = lambda l: not l
tete   = lambda l: l[0]
reste  = lambda l: l[1:]
cons   = lambda a, l: [a, *l]