def fonc(a=1, b=2, c=3, d=4, e=5):
    print("a =", a, "b =", b, "c =", c, "d =", d, "e =", e)
fonc()
fonc(4)
fonc(b=100,e=100)

#opérateur splat
def f(*params):
    for p in params:
        print(p)

def g(**params):
    for cle in params:
        print("cle={} valeur={}".format(cle,params[cle]))


