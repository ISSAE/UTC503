n=int(input("Donner un nombre: "))
def diviseur_l(n):
    res=[1]
    i=2
    while i<n:
        if n%i == 0:
            res.append(i)
        i=i+1
    return res
print(diviseur(n))

def diviseur_lc(n):
    return [i for i in range(n) if n%i == 0]
print(diviseur(n))

def diviseur_g(n):
    yield 1
    i=2
    while i<n:
        if n%i == 0:
            yield i
        i=i+1

def diviseur_gc(n):
    return (i for i in range(n) if n%i == 0)