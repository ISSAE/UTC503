def exFonc(x):
    return x+1

exFoncL=lambda x: x+1

print("exFonc(1)= ",exFonc(1))
print("exFoncL(1)= ",exFonc(1))

print("L'attribut nom de la fonction exFonc.__qualname__= ",exFonc.__qualname__)
print("L'attribut nom de la fonction exFoncL.__qualname__= ",exFoncL.__qualname__)

#Le nom d'une fonction est un nom comme tout autre type de donnée
exFoncL1=exFoncL
print("exFoncL.__qualname__= ",exFoncL.__qualname__)
print("exFoncL1.__qualname__= ",exFoncL1.__qualname__)
exFoncL1.__qualname__='MaFonction inc lambda'
print("exFoncL1.__qualname__= ",exFoncL1.__qualname__)

#La fonction est un objet (tout est objet en python) le fonction sont dites 
#fonction de première classe (en opposition aux langage ou les fonctions ne sont pas
# des objets comme les autres)
print("type exFoncL1",type(exFoncL1))
print("type exFonc",type(exFonc))
print("id exFoncL",id(exFoncL))
print("id exFoncL1",id(exFoncL1))
print("id exFonc",id(exFonc))