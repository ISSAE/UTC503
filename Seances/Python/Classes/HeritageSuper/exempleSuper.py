class Vehicule: 
       
    # Constructeur 
    def __init__(self, marque, vitesse):
        self._marque = marque
        self.vitesse = vitesse 
        
    # Pour récupérer la marque
    def getMarque(self): 
        return self._marque 
    
    def setMarque(self,marque):
        self._marque=marque
   
    # Pour vérifier si cette vehicule est une voiture
    def estUneVoiture(self): 
        return False
   
   
# Sous classe
class Voiture(Vehicule): 
    '''
       Vehicule.__init__ pourrait être remplacé par super().__init__
    '''
    def __init__(self, marque, vitesse, nbPort):
        Vehicule.__init__(self, marque, vitesse)
        self.nbPort = nbPort
        
    def estUneVoiture(self): 
        return True
   
# code de test 
vh = Vehicule("Moto", 100)  # Un objet de vehicule
print(vh.getMarque(), vh.estUneVoiture()) 
   
vt = Voiture("Mercedes", 300, 4) # Un objet de voiture
print(vt.getMarque(), vt.estUneVoiture())