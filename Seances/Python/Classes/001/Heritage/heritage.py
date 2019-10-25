class base:
	def affiche(self):
		print("je suis la base")
 
class filleA(base):
	def affiche(self):
		base.affiche(self)
		print ("filleA")
 
class filleB(base):
	def affiche(self):
		print ("filleB")
 
class filleC(base):
	pass

class filleD(base):
    def affiche(self, plus):
        base.affiche(self)
        print ("filleB", plus)
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
