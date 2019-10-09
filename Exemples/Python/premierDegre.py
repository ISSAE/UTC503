# R0: résoudre équation du premier degré ax+b=0

## R01: Lire donnée a et b
## R02: Claculer la solution
## R03: Afficher la solution

###R021: Verifier a!=0
###R022: calculer -b/a

def premDegre(a,b):
    assert a!=0,"A ne doit pas être nul"
    return -b/a

def pgmPremDegre():
    print("saisir a et b pour calculer ax+b=0")
    x=int(input("Donner a "))
    y=int(input("Donner b "))
    rep=premDegre(x,y)
    print("la solution de",x,"x +",y,"= 0 est ",rep)


