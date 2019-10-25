import m1
def f(x):
    return m1.x+x

def g(x):
    m1.f(100)
print(__name__)