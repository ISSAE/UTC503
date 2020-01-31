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
    ''' op: operateur 2 parmètres élement et liste
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
reduire(lambda t,r: 1+r,0,[11,2,3,4,5])
reduire(lambda t,r: t+r,0,[1,2,3,4,5])

#Un shémas appelé reduce dans Python existe: Utilisation de reduce :liste vers scalaire
from functools import reduce

#Reduce en Python est différent de reduire 
# par exemple
# reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calcul
# ((((1+2)+3)+4)+5)
# essayer reduire(lambda x,y: 1+y,[1,2,3,100]) et reduce(lambda x,y: 1+y,[1,2,3,100])
# reduce de Python traitement au niveaux des éléments reduire schémas de récursivité

#Quelques exemple de reduce
# Une liste initiale... en style fonctionnel
lis = lambda : [ 1 , 3, 5, 6, 2, ] 
# Au lieu d'une affectation 
# lis=[ 1 , 3, 5, 6, 2, ]
  
# using reduce to compute sum of list 
print ("The sum of the list elements is : ",end="") 
print (reduce(lambda a,b : a+b,lis())) 
  
# using reduce to compute maximum element from list 
print ("The maximum element of the list is : ",end="") 
print (reduce(lambda a,b : a if a > b else b,lis())) 

#TODO: Ecrire le résulat pour min


##  Complément fold_left et fold_right (le reduce de python)
def tete(l): return l[0]
def reste(l): return l[1:]
## Fold_left et Fold_right
def fold_left(op, a, l):
    if l:
        return fold_left(op, op(a,tete(l)), reste(l))
    else:
        return a

#fold est recursive terminale.... voici sa version impérative
def foldLeft(op,a,l):
    fl=a
    while(l):
        fl=op(fl,tete(l))
        l=reste(l)
    return fl

''' exemple
>>> fold_left(lambda x,y: x+y,0, [1,2,3,4])
10
>>> foldLeft(lambda x,y: x+y,0, [1,2,3,4])
10
'''
cons=lambda a,l: [a,*l]

