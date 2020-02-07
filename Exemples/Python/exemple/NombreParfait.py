'''
   Ensemble de fonctions diviseurs d'un nombre: 
      fonctionnel récursive et récursive terminale
      impérative, lazy (génerateur), protocole itérateur
      pour récupérer l'ensemble des diviseurs d'un nombre n
'''
## Version fonctionnel récursive
def diviseurFonc(n):
    def _diviseurs(n,i):
        if i<n:
            if n%i == 0:
                return [i, *_diviseurs(n,i+1)]
            else:
                return _diviseurs(n,i+1)
        else:
            return []
    return _diviseurs(n,1)

print(diviseurFonc(6))

## récusions terminale
def diviseursRecTerminale(n):
    def _diviseurs(n,acc,i):
        if i<n:
            if n%i == 0:
                return _diviseurs(n,[*acc, i],i+1)
            else:
                return _diviseurs(n,acc,i+1)
        else:
            return acc
    return _diviseurs(n,[],1)
print(diviseursRecTerminale(6))

## Version impérative
def diviseurImp(n):
    res=[]
    for i in range(1,n//2 + 1):
        if n%i == 0:
            res.append(i)
    return res
print(diviseurImp(6))

#Version générateur
def diviseurLazy(n):
    i=1
    while i<n//2 +1:
        if n%i ==0: yield i
        i = i+1
print(list(diviseurLazy(6)))

def diviseursFilter1(n):
    return [i for i in range(1,n//2+1) if n%i==0]
print(diviseursFilter1(6))

def diviseursFilter2(n):
    return (i for i in range(1,n//2+1) if n%i==0)
print(list(diviseursFilter2(6)))

class Diviseurs:
    def __init__(self,n):
        self.n = n
        self.lastDiv=0
    def __iter__(self):
        return self
    def __next__(self):
        rechercheDiv=self.lastDiv+1
        while self.n%rechercheDiv != 0:
           if self.n//2 +1 < rechercheDiv: raise StopIteration()
           rechercheDiv += 1
        # en sortie de boucle on a self.n%self.lastDiv == 0
        self.lastDiv=rechercheDiv
        return self.lastDiv
print(list(Diviseurs(6)))

toutesLesFonctions=[diviseurFonc,diviseurImp,diviseurLazy,diviseursFilter1,diviseursFilter2,diviseursRecTerminale]

def evalTime(f,n):
    import time
    d=time.time()
    res=f(n)
    return f"{f.__name__} {time.time()-d}"