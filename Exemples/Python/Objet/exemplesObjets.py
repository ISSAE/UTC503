class MaClasse:
    x=5

mc=MaClasse()
print(mc.x)
mc.y=3
print(mc.x,mc.y)
class SousClasse(MaClasse):
    #y=3
    __y=3
    def bizare(self):
        return self.y+self.x

sc=SousClasse()
print(sc.bizare())
sc.x=10
sc.y=20
print("x={},y={},bizare={}".format(sc.x,sc.y,sc.bizare()))