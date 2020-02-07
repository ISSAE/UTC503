Uinit=53000
Vinit=9000

# U(n+1) = U(n) * (1+a-bV(n))
# V(n+1) = V(n) * (1 -c + dU(n))

def U(n):
    if n:
        vm1=V(n-1)
        um1=LU[-1]
        un=um1 * (1+a-b*vm1)
        LU.append(un)
        return un
    else:
        LU.append(Unit)
        return Uinit

LU=[]
LV=[]
def V(n):
    if n:
        vm1=LV[-1]
        um1=U(n-1)
        vn = vm1 * (1 -c + d*um1) 
        LV.append(vn)
        return vn       
    else:
        LV.append(Vinit)
        return Vinit

def UV(a=0.09, b=0.00001, c=0.25, d=0.000005, U=53000, V=9000):
    while True:
        yield (U,V)
        U,V=U * (1+a-b*V), V*(1 -c + d*U)