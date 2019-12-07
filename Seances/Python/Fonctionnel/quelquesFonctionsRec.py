#Calcul de la taille d'une liste version récursive
def taille(l):
    if l:
        return 1+ taille(l[1:])
    else:
        return 0

#Version Lambda
tailleL=lambda l: l and 1+ tailleL(l[1:]) or 0

# Calcul de la somme des elément d'une liste
# Version récursive
'''
si n le nombre d'élement
        somme(l)=l[0]+...+l[i]+....+l[n-1]

        ou récursivement
        somme(l)=l[0]+somme(reste(l)) reste(l) est l[1:]
        somme([])=0 
'''
def somme(l):
    ''' Somme de tous les éléments de la liste
        
        :param l: la liste
        :return: la somme de tous les élément de la liste
    '''
    print("Appel de somme avec ",l)
    if l:
        return l[0]+ somme(l[1:])
    else:
        return 0

#Version Lambda
sommeL=lambda l: l[0]+sommeL(l[1:]) if l else 0