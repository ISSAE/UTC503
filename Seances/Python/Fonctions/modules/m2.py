import m1
def f(x):
    return m1.x+x

def g(x):
    return m1.f(100)
    
def jeSuis():
    print("dans m2")

print(__name__)