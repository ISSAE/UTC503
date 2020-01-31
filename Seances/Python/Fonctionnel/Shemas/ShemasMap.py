'''
   Appliquer une fonction f a tus les éléments d'une liste
   renvoie la liste [...f(ei)...]
'''
cons=lambda a,l: [a,*l]
def tete(l): return l[0]

def reste(l): return l[1:]


def myMap(f,l):
    if l:
        return cons(f(tete(l)), myMap(f,reste(l)))
    else:
        return []

#map existe dans python