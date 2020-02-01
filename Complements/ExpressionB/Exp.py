class Exp:
    def __str__(self):
        pass
    def postfixe(self):
        pass
    def prefixe(self):
        pass

class Const(Exp):
  """ Les constante des expression arithmétique""" 
  def __init__(self,v):
    """ e attribut d'objet contenant le nombre"""
    self.e=v
  # def __str__(self):
  #  return f"C:{self.e}"
  def __str__(self):
    return "C:"+str(self.e)
  def postfixe(self):
        return f"C:{self.e}"
  def prefixe(self):
        return f"C:{self.e}"
    
class ExpB(Exp):
    """ Les Expression binaire des expression arithmétique""" 
    def __init__(self, op, e1, e2):
        """ Expression binaire est définit par
            un operateur : op exemple + - *
            Une expression gauche e1: par exemple 2 ou (2+3)
            Une expression droite e2:
            (e1 op e2)
            """
        self.op=op
        self.e1=e1
        self.e2=e2
    def __str__(self):
        return f"""({self.e1} {self.op} {self.e2})"""
    # def __str__(slef):
    #    return "("+str(self.e1)+" "+str(self.op)+ " "+str(self.e2)+")"
    def postfixe(self):
        return f"{self.e1.postfixe()} {self.e2.postfixe()} {self.op}"
    
    def prefixe(self):
        return f"{self.op}({self.e1.prefixe()},{self.e2.prefixe()})"
       
  