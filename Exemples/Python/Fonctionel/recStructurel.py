#tete de liste
tete =lambda l: l[0]
#reste de la liste
reste=lambda l: l[1:]
(lambda l: f"tete={tete(l)} reste={reste(l)}")([1,2,3,4])
##Taille d'une liste résursive
def taille_(l):
    if l:
        return 1+taille_(l[1:])
    else:
        return 0

##taille d'une liste en ecriture lambda##
taille_ll = lambda l: 1+taille_ll(reste(l)) if l else 0
##

##Somme des éléments d'une liste
def somme_l(l):
    if l:
        return l[0]+somme_l(l[1:])
    else:
        return 0
somme_ll = lambda l: tete(l)+somme_ll(reste(l))

##Calcul de la moyenne 
def moyenne_l(l):
    return (somme_l(l)/taille_(l))

moyenne_ll = lambda l: somme_ll(l)/taille_ll(l)

#Cette manière de calculer la moyenne a un défaut
# On parcourt la liste 2 fois!

#Une fonction pour éviter l'affectation
def coupleRep(l, st):
    return (1+st[0], l[0]+st[1])

def sommeTaille(l):
    ''' somme Traille renvoie le couple (taille,somme)
        où taille est la taille de la liste
        et somme est la somme des éléments de la liste
    '''
    if l:
        # st=sommeTaille(l[1:])
        # return (1+st[0], l[0]+st[1])
        return coupleRep(l, sommeTaille(l[1:]))
    else:
        return (0,0)

def moyenne_(st):
    return(st[1]/st[0])

def moyenneOpt(l):
    moyenne_(sommeTaille(l))