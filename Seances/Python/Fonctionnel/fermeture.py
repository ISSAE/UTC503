def f(x):
    def g(y):
        return x+y
    return g

f=lambda x: lambda y: x+y