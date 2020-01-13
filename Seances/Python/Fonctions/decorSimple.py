def f(x):
    def g(y):
        return x+y
    return g

def decor(f):
    def g(*params, **kparams):
        print("New fonction f")
        res=f(*params,**kparams)
        print("End f")
        return res
    return g

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

