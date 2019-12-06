# Un commentaire

'''
  Un grand commenatire sur plusieurs lignes
  bla bla
'''

x=3+2
y=(x+5)
z=x+y
print(z)

s=input("Saisir un nombre ")
print(s)
print(type(s))
x=int(s)
print(x,type(x))
if (x==0):
  x=2
  print("Dans if vrai",x)
else:
  x=10
  print("Dans if faux",x)
print("Fin du if")