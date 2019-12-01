class Point: 
    def tester(self):
        print(self.x) 
 
p1 = Point() 
p2 = Point() 

#Création dynamique d'attribut!
p1.x = 5 
p1.y = 4 
 
p2.x = 3
p2.y = 6 
 
print(p1.x, p1.y) 
print(p2.x, p2.y) 