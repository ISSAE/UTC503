class Base:
    
    def add(x,y):
        return x+y
    
    def m(self, x=0):
        return f"Dans Base {x}"

class A(Base):
    def m(self,x):
        return f"Dans A {x}"

class B(Base):
    def m(self,x):
       return f"Dans B {x}"
class C(A,B):
    pass
class D(A,B):
    def m(self,x):
        return Base.m(self, x)

base=Base()
a=A()
b=B()
c=C()
d=D()
print(base.m())
print(a.m(1))
print(b.m(2))
print(c.m(3))
print(d.m(4))


