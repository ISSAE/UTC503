def pair0(n):
    i=0
    l=[]
    while (i<=n):
        if (i%2 == 0):
           l=[*l,i]
        i = i+1
    return l

def pair():
    i=0
    while True:
        if (i%2 == 0):
            yield i
        i = i+1

def pair2(n):
    i=0
    while (i<n):
        if (i%2 == 0):
            yield i
        i = i+1

toto=pair()
for i in range(10):
    next(toto)

for _,p in zip(range(10), pair()):
    print(p)


## Lazy avec iterable

class Pair:
    def __init__(self):
        self.i=0   
    def __iter__(self):
        return self
    def __next__(self):
        self.i=self.i+2
        return self.i

class V:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return V(self.x+other.x, self.y + other.y)
    
