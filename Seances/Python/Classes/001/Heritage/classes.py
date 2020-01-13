class X:
    _x=100
    def reset(self):
        self.x=0
    def add(self,x,y):
        return(x+y)
    def afficheattribut(self):
        print(self.x)

class Y:
    y=100
    def __init__(self):
        self.z=0
        self.toto=20
