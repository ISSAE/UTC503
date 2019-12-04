class X:
   def m(self):
     return "dans X"

class Y(X):
   def m(self,x):
       print(X.m(self)) 
       return "dans Y"

