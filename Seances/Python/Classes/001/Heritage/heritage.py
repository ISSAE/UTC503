class base:
  def pasmethode():
    return "Pas Methode"
  def affiche(self):
    print("je suis la base")
  def uneM(self):
        self.x=10
        return f"uneM dans base {self.x}"  


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

class filleComplexe(filleC,filleD):
   def affiche(self):
         filleC.affiche()

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
