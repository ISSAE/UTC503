def call_(f, *param, **params):
    return f(*param, **params)

def timeExe(f):
    def calculTemps(*param, **params):
        import time
        debut=time.time()
        res=call_(f,*param,**params)
        print(f"temps de {f.__name__}={time.time()-debut}")
        return res
    return calculTemps

@timeExe
def fact(n):
    F=1 #si n ==0  on rentre pas dans la bouble
    #issue de la definition récursive f(n) = n* f(n-1) si n sinon 1
    while (n>0):
        F *= n
        n -= 1
    return F

@timeExe
def add(x,y):
    return x+y

@timeExe
def exemple(a, a1, b=1,c=2):
    return a+a1+b+c


print(exemple(1, 2, c=3))
print(fact(100))