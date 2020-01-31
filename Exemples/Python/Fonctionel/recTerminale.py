# Recusivité
def somme_(n):
    ''' Calcule de somme(n)=0+1+2+3+...+(n-1)+n '''
    if (n==0):
        return 0
    else:
        return n+somme_(n-1)

# Récursion terminale
def somme_aux(a,n):
    if (n==0):
        return a
    else:
        return somme_aux(a+n,n-1)

def somme(n):
    return somme_aux(0,n)

