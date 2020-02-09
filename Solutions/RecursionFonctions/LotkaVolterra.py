import time
## Donnéss du problème
'''
u: number of preys (for example, rabbits)
v: number of predators (for example, foxes)

    a, b, c, d are constant parameters defining the behavior of the population:
        a is the natural growing rate of rabbits, when there's no fox
        b is the natural dying rate of rabbits, due to predation
        c is the natural dying rate of fox, when there's no rabbit
        d is the factor describing how many caught rabbits let create a new fox
'''
a=0.09 #1
b=0.00001 #0.1
c=0.25 #1.5
d=0.000005 #0.75*0.1=0.075


Uinit=53000
Vinit=9000

# U(n+1) = U(n) * (1+a-bV(n)) = U(n) + aU(n) -bU(n)V(n)
# V(n+1) = V(n) * (1 -c + d*b*U(n)) = V(n) -cV(n) + dU(n)V(n)
def uv(n, a=0.09, b=0.00001, c=0.25, d=0.000005):
    if n:
        un_1,vn_1=uv(n-1)
        return(un_1*(1+a-b*vn_1),vn_1*(1-c+d*un_1))
    else:
        return (Uinit,Vinit)
d=time.time()
UVR=[uv(i) for i in range(200)]
print("rec ", time.time() - d)
def uv_imp(n,a=0.09, b=0.00001, c=0.25, d=0.000005):
    u,v=Uinit,Vinit
    i=0
    while i< n:
        i = i+1
        u,v=u*(1+a-b*v),v*(1-c+d*u)
    return (u,v)
d=time.time()
UVI=[uv_imp(i) for i in range(200)]
print("imp ", time.time() - d)
def uv_gen(a=0.09, b=0.00001, c=0.25, d=0.000005):
    '''
       Fournir la prochaine génération
       Pas besoin de n
    '''
    u,v=Uinit,Vinit
    while True:
        yield (u,v)
        u,v=u*(1+a-b*v),v*(1-c+d*u)
d=time.time()
UVG=[(u,v) for _,(u,v) in zip(range(200),uv_gen())]
print("gen ", time.time() - d)

import matplotlib.pyplot as plt
def plotEvolution(n):
    plt.plot([(u,v) for _,(u,v) in zip(range(n),uv_gen())])
    plt.show()
## 
plotEvolution(250)
LU=[]
LV=[]
def U(n):
    if n:
        vm1=V(n-1)
        um1=LU[-1]
        un=um1 * (1+a-b*vm1)
        LU.append(un)
        return un
    else:
        LU.append(Uinit)
        return Uinit
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
