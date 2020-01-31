'''
    Les espèces animales
    1 Mammifères. 1.1 Cétacés. 1.2 Marsupiaux. 1.3 Chiroptères. 1.4 Insectivores. 1.5 Primates. ...
    2 Oiseaux.
    3 Reptiles. 3.1 Tortues. 3.2 Lézards. 3.3 Serpents.
    4 Amphibiens.
    5 Poissons.
    6 Insectes. 6.1 Éphémèroptères. 6.2 Orthoptères. 6.3 Odonates. 6.4 Coléoptès. 6.5 Lépidoptères. ...
    7 Crustacés.
    8 Mollusques. 8.1 Gastéropodes. 8.2 Bivalves.
'''
class Mammiferes:
    espece='Mammifères' #Attribut de classe
    def __init__(self,nom='', age=0):
        if (isinstance(nom,str)):
            self._nom=nom #attribut d'instance
        else:
            self._nom=str(nom)
        self._age=age
    def getNom(self):
        return(self._nom)
    def setNom(self,nom):
        self._nom=nom
    def setEspece(self,esp):
        Mammiferes.espece=esp
    def setNespece(self,esp):
        self.espece=esp
    def setDespece(self,esp):
        espece=esp



