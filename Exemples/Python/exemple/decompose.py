# -*- coding: utf-8 -*- 
# décomposition en facteurs premiers 
def _estFacteur(i,n):
    return (n%i == 0)

def _decompose(n, i):
    ''' Decompose à partitr du facteur i '''
    #print(n,i)
    if (i > n): return []
    else:
        if n % i == 0: return [i] + _decompose(n/i,i)
        else: return  _decompose(n,i+1)

def decomposeRec(n):
    return _decompose(n,2)

def decompose(n): 
    res=[]
    i=2 
    while n>1: 
        while n%i==0: 
           res += [i]
           n=n/i 
        i=i+1 
    return res

def recalcul(facteurs):
    res=1
    for f in facteurs:
        res *= f
    return res

if __name__ == '__main__':
    for n in range(1,100+1):
        assert recalcul(decompose(n)) == n
        assert recalcul(decomposeRec(n)) == n
        facteurs=decompose(n)
        print(f"decompose({n})={facteurs}")
        


 