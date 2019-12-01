# R0: résoudre équation du premier degré ax+b=0

## R01: Lire donnée a et b
## R02: Claculer la solution
## R03: Afficher la solution

###R021: Verifier a!=0
###R022: calculer -b/a
'''
   bla bla bla
'''
"""
  bli bli bli
"""
# premDegre calcul -b/a a condition d'être sure que a!=0
def premDegre(a,b):
    # assert permet de faire de la programation deffensive
    assert a!=0,"A ne doit pas être nul"
    return -b/a

def controleEntreeEtSol(a,b):
    if a == 0:
        if b==0:
            return "Infinité de solutions"
        else:
            return "Impossible pas de solutions"
    else:
        return premDegre(a,b)
    



def pgmPremDegre1():
    ''' 
       C'est le calcule de la solution 
       d'une equation du premier degré
    '''
    
    print("saisir a et b pour calculer ax+b=0")
    x=int(input("Donner a "))
    y=int(input("Donner b "))
    rep=premDegre(x,y)
    print("la solution de",x,"x +",y,"= 0 est ",rep)

def pgmPremDegre2():
    print("saisir a et b pour calculer ax+b=0")
    x=int(input("Donner a "))
    y=int(input("Donner b "))
    rep=controleEntreeEtSol(x,y)
    print("la solution de",x,"x +",y,"= 0 est ",rep)


