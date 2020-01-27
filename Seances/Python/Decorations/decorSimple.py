#Une fonction qui renvoie une fonction
#i.e Une fabrique de fonction
def f(x):
    def g(y):
        return x+y
    return g

#add3 est la fonction g telque x est 3
add3=f(3)

#On aurait pu écrire avec lambda
fl=lambda x: lambda y: x+y

#exemple add4
add4=fl(4)

#essayer
print(add3(10),add4(10))

#Rappel nombre de paramétre inconnu : 
#comment définir les paramétres de fonction?
def inconnu0(*p):
    print(p)

def inconnu1(**p):
    print(p)

def inconnu3(*p, **pk):
    print(*p,**pk)

#essayer
print(inconnu0(1,2,3,4,5),inconnu1(a=1,b=2,c=3,d=4,e=5))
print(inconnu3(1,2,3,a=1,b=2,c=3))


#Première utilisation, redéfinir le comportement d'une fonction
def decorSimple(f):
    ''' f est une fonction
        remvoie la fonction f modifiée
    '''
    def newF(*param, **paramk):
        ''' Ne sachant pas quels sont les paramétres
            de la fonction f on utilise * et **
        '''
        print("Cette fonction a modifié celle ci",f.__name__)
        res=f(*params,**params) # On appel la fonction f
        print("Le résultat de l'appel de f est ",res)
        return res
    return newF

def decor(f):
    def g(*params, **kparams):
        print("New fonction f")
        res=f(*params,**kparams)
        print("End f")
        return res
    return g

def inc(x): return x+1

ninc = f(inc)

def decorSimple(f):
    ''' f est une fonction
        remvoie la fonction f modifiée
    '''
    def newF(*param, **paramk):
        ''' Ne sachant pas quels sont les paramétres
            de la fonction f on utilise * et **
        '''
        print("Cette fonction a modifié celle ci",f.__name__)
        res=f(*params,**params) # On appel la fonction f
        print("Le résultat de l'appel de f est ",res)
        return res
    return newF

@decor
def add(x,y):
    return x+y

# equiv de mult=decor(mult)   
@decor
def mult(x,y):
    return x*y

def app(f, x, y):
    return f(x,y)

def myF():
    print("MyF")

def f(x):
    def g(y):
        return x+y
    return g

