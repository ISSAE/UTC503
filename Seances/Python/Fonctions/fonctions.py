def f(x):
    x=100
    toto=500
    return x

def add(x,y):
    return x+y

def mult(x,y):
    return x*y

def aplique(f,x,y):
    return f(x,y)

def modifie(l,index,valeur):
    l[index]=valeur

def fact(n):
    if (n==0):
        return 1
    else:
        return n*fact(n-1)

def fact(n):
    if n:
        return n*fact(n-1)
    else:
        return 1

#Calcul de la taille d'une liste version récursive
def taille(l):
    if l:
        return 1+ taille(l[1:])
    else:
        return 0

# Calcul de la somme des elément d'une liste
# Version récursive
def somme(l):
    ''' Somme de tous les éléments de la liste
        
        :param l: la liste
        si n le nombre d'élement
        somme(l)=l[0]+...+l[i]+....+l[n-1]

        ou récursivement
        somme(l)=l[0]+somme(reste(l)) reste(l) est l[1:]
        somme([])=0 
    '''
    print("Appel de somme avec ",l)
    if l:
        return l[0]+ somme(l[1:])
    else:
        return 0

def calculette():
    while (True):
        exp=input("Entrer votre expression : ")
        if(exp == '.'):
            return None
        print(eval(exp))



def f(x):
    def g(y):
        return x+y
    return g

def gf(*args, **kargs):
    print(args, kargs)
    # return ggf(**kargs)

def ggf(a=1,b=2,c=3):
    return(a,b,c)

def trace(f):
    def g(*args):
        print(f"Avant appel f {id(f)} {args}")
        x=f(*args)
        print(f"Apres appel de f resultat={x}")
        return x
    return g

@trace
def uneFonc(x):
    return x+1

@trace
def factAndOr(n):
    return(n and n*factAndOr(n+1 if n<0 else n-1) or 1)

fonc=uneFonc

#uneFonc=decorer(uneFonc)


#Pour le passage de param1ètre
def f(x):
    print(id(x))
    x=100
    print(id(x))
    print(id(100))

