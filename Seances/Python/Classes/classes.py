class MaClass:
    x=3

mc=MaClass()
print(mc.x)

#Constructeur (ou initialisation de la classe)
class Personne:
    def __init__(self, nom, age):
        self.nom=nom
        self.age=age

p1=Personne("Un nom",10)
print(p1.nom,p1.age)
 v          
# Methodes
class Personne2:
    #self represente le premier paramètre l'objet lui meme
    #Pas obligé qu'il s'appel self
    def __init__(moi, nom, age):
        moi.nom=nom
        moi.age=age
    def uneMethode(self):
        print("Mon nom {} et age {}".format(self.nom,self.age))

p2=Personne2("Un nom",10)
p2.uneMethode()

class Exemple:
    def f(self):
        return 1
    def f(self,x):
        return x

