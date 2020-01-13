def fonc(a=1, b=2, c=3, d=4, e=5):
    print("a =", a, "b =", b, "c =", c, "d =", d, "e =", e)
fonc()
fonc(4)
fonc(b=100,e=100)

#opérateur splat
def f(*params):
    print(type(params), params)
    for p in params:
        print(p)
f(1,2,3,4)

def g(**params):
    print(type(params), params)
    for cle in params:
        print(f"cle={cle} valeur={params[cle]}")
g(x=2,k=5,w=9)

def fg(*params, **kparams):
    print(f"params {type(params)}:{params} kparams {type(kparams)}:{kparams}")
    for p in params:
        print(p)
    for k in kparams:
        print(f"cle={k} valeur={kparams[k]}")

fg(1,2,3,d=10,w=30)

def g2(**params):
    for cle in params:
        print("cle={} valeur={}".format(cle,params[cle]))

def add(x,y):
    return x+y



