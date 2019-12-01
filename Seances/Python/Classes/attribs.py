class UneClasse:
    """En Python une classe est un espace de nom
    Particulier"""
    def __init__(self):
        self.x=2
    def f(self):
        """self represente l'objet lui meme, self n'est pas
        un mot clé"""
        return self.x   
#On peut ecceder a x
print(UneClasse.x)
#f est un attrubut fonction : cad méthode dans le jatgon objet
type(UneClasse.f)
#Creation d'un objet UneClasse
c=UneClasse()
#Utilisation de la méthode
UneClasse.f(c)
#ou
c.f()

