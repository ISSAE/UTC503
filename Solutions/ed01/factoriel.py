#Factoriel Recursive
def fact(n):
    assert n>=0, "Factoriel d'un nombre positif ou nul uniquement!"
    if (n==0): return 1
    else: return n*fact(n-1)

def factWhile(n):
    #0!=1
    F=1
    i=0
    while (i<n):
        i+=1
        F=F*i
    return F


def factIter(n):
    assert n>=0, "Factoriel d'un nombre positif ou nul uniquement!"
    F=1
    # Verifier comment fonctionne range
    for i in range(n):
        # Range de 0 à n-1 (donc i+1 pour 1 à n)
        F=F*(i+1)
    return F

#Factoriel recusive en pure fonction (lambda)
factL = lambda n: n*factL(n-1) if n else 1

#Une astuce pour tester le module quand on lance le programme directement 
# python factoriel.py
# si import __name__ n'est pas égal à __main__
if __name__ == "__main__":
    assert fact(0)==1
    assert fact(2)==2
    assert fact(4)==24
    assert fact(5)==120
    #On suppose que fact est correct!
    for i in range(10):
        assert fact(i)==factIter(i)
        assert fact(i)==factWhile(i)
        assert fact(i)==factL(i)
    print("Test OK")