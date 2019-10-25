class Point:
    #pas necessasirement self 
    #(tous seimplement un nom de variable)
    def reset(this): 
        this.x = 0 
        this.y = 0 
 
p = Point()
p.x=10
p.y=20
print(p.x, p.y)
#Appel de la methode reset comme une fonction!
#Comme les méthode static en Java (méthode de classe)
Point.reset(p) 
print(p.x, p.y)