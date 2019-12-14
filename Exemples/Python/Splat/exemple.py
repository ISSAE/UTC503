def f(*params):
    print(params)

def g(**kparams):
    print(kparams)

def fg(*params, **kparams):
    print(params,kparams)

def add(x,y):
    return x+y