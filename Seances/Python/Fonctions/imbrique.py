def f(x):
    def g(y):
        return x+y
    return g(x)+100

