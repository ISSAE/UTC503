# fonction declarative par matching et substitution
fdouble = lambda x: 2*x

# fonction impérative (passage de paramètres par affectation dans une pile)
def idouble(x):
    return 2*x

# pgcd declaratif
pgcd = lambda a, b: a if a == b  else pgcd (a-b,b) if a > b  else pgcd (a, b-a)

# factorielle declarative
fact = lambda n: 1 if n==0 else n*fact(n-1)

# pgcd impératif
def ipgcd(a,b):
    while a != b:
        if a > b:
            a=a-b
        else:
            b=b-a
    
    return a





