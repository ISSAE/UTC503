tete=lambda l: l[0]
reste=lambda l: l[1:]

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
        return l[0] + somme(l[1:])
    else:
        return 0


def unique(l):
    '''
       elimine les doublons d'une liste
    '''
    def _unique(reste):
        if (l[0] in reste): return reste
        else: return reste + [l[0]]
    if l: return _unique(l[1:])
    else: return l

def uniqueSemiFonc(l):
    if not l: return l
    else:
        u=unique(l[1:])
        if (l[0] in u): return u
        else: return [l[0]]+u

#Version Lambda
sommeL=lambda l: l[0]+sommeL(l[1:]) if l else 0

#Quelues exemples et tests
if __name__ == '__main__':
    l=[1,2,3,4.5,-2]
    assert tailleL(l) == 5
    print(tailleL(l))
    assert sommeL(l) == 8.5
    print(sommeL(l))
