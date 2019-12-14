class base:
  def pasmethode():
    return "Pas Methode"
  def affiche(self):
    print("je suis la base")
  def uneM(self):
    return "uneM dans base"  


class filleA(base):
  def affiche(this):
    base.affiche(this)
    print ("filleA")

## meme celle ci marche!
class marchePas:
  def affiche(this):
    base.affiche(this)
    print ("marchePas")

class filleB(base):
  def affiche(self):
    print ("filleB")
 
class filleC(base):
  pass

class filleD(base):
  def affiche(self, plus):
    base.affiche(self)
    print("filleB", plus)

class filleComplexe(filleA,filleD):
  def affiche(self):
    	  filleA.affiche()

a=filleA()
a.affiche()
#je suis la base
#filleA
 
b=filleB()
b.affiche()
#filleB
 
c=filleC()
c.affiche()
#je suis la base
