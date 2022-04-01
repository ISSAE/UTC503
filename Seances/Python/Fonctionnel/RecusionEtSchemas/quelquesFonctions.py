from lisp import *

# taille d'une liste
taille = lambda l: 0 if null(l) else 1+taille(reste(l))

#Somme des élements d'une liste
somme = lambda l: 0 if null(l) else tete(l)+somme(reste(l))

#Un schemas se dégage
genericRec = \
lambda cond, op, valeur: \
  lambda l: valeur if cond(l) else op(tete(l),genericRec(cond,op,valeur)(reste(l)))

