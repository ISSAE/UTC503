class X:
   class Z:
      x=100
   x=3
   def add(x,y):
          return x+y
   def m(self):
     return "dans X"

class Y(X):
   def m(self,x):
       print(X.m(self)) 
       return "dans Y"

