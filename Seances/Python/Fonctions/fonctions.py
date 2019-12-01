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

def calculette():
    while (True):
        exp=input("Entrer votre formule : ")
        if(exp == '.'):
            return None
        print(eval(exp))

