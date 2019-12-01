class MaClass:
    x=3

mc=MaClass()
print(mc.x)

#Constructeur (ou initialisation de la classe)
class Personne:
    def __init__(moi, nom, age):
        moi.nom=nom
        moi.age=age

p1=Personne("Un nom",10)
print(p1.nom,p1.age)
       
# Methodes
class Personne2:
    #self represente le premier paramètre l'objet lui meme
    #Pas obligé qu'il s'appel self
    def __init__(moi, nom, age):
        moi.nom=nom
        moi.age=age
    def uneMethode(x):
        print("Mon nom {} et age {}".format(x.nom,x.age))
    def m():
        print("m")

p2=Personne2("Un nom",10)
p2.uneMethode()

class Exemple:
    """Exemple pour montrer qu'en Python
    Pas de surcharge"""
    #Pas de surcharge
    def f(self):
        return 1
    #Pas de surcharge
    def f(self,x):
        return x
    def m():
        return 1

