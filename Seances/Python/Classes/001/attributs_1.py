class Point: 
    def reset(self): 
        self.x = 0 
        self.y = 0 
    def f(self):
        print(self.v)
 
p = Point()
p.x=10
p.y=20
print(p.x, p.y)
p.reset() 
print(p.x, p.y)