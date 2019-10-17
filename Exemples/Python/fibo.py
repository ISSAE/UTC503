#Version récursive

def fibr(n):
    if n < 2:
        return n
    else:
        return fibr(n - 1) + fibr(n - 2)

#Version avec générateur
def fibg():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

#Version avec série
def fibs(n):
    res=[]
    a,b=0,1
    while(a<n):
        res.append(a)
        a,b=b,a+b
    return res


