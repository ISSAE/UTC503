def foncRec(l):
    if l:
        #Si la liste n'est pas vide action avec opérateur binaire
        return operation(tete(l),foncRec(reste(l)))
    else:
        #si la séquence est vide
        return valeurInit # valeur par defaut

#l'exemple de la somme des élements d'une liste
def somme_l(l):
    if l:
        #ici l'opérateur est le + 
        return l[0]+somme_l(l[1:])
    else:
        return 0

#ou encore du nombre d'élements d'une liste
def nombre_l(l):
    if l:
        return 1+nombre_l(l[1:])
    else:
        return 0

#ou encore le tri
# a faire en exercice
def tri_l(l):
    if l:
        return inserer_dans_liste_trie_up(l[0],tri_l(l[1:]))
    else:
        #une liste vide est déjà triée
        return l

def inserer_dans_liste_trie_up(e, l):
    print(f"e={e} l={l}")
    if l:
        if (e < l[0]):
            return [e,*l]
        else:
            print("rec")
            return [l[0],*inserer_dans_liste_trie_up(e,l[1:])]
    else:
        print([e])
        return [e]

def reduire(op,vi,l):
    ''' op: operateur 2 parmètres élement liste
      vi: valeur defaut si liste vide
      l: la sequence
    '''
    if l:
        print(f"reduire: tete={l[0]} reste={l[1:]}")
        return op(l[0], reduire(op, vi, l[1:]))
    else:
        return vi
 
#exemple
reduire(inserer_dans_liste_trie_up,[],[-10,-100,5,20,3])
reduire(lambda x,y: 1+y,0,[1,2,3,4,5])
reduire(lambda x,y: x+y,0,[1,2,3,4,5])

#ce shémas c'est reduce : Utilisation de reduce :liste vers scalaire
from functools import reduce

