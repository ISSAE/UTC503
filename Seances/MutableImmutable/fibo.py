'''
procedure de calcul de la suite de fibonacci

f(0) = 0
f(1) = 1
f(n) = fn(n-1)+f(n-2)
'''

# état initial
l=[0, 1]

def fibo(n, lfibo):
    '''
    Calcul des éléments de la suite de fibonacci

    n : le nombre d'éléments nouveaux souhaités
    lfibo: La liste des élements de la suite
      IN : les élements initiaux
      OUT : La suite des n premiers éléments 
    '''
    for i in range(n):
        lfibo.append(lfibo[-1]+lfibo[-2])


fibo(3,l)
print(l)
fibo(3,l)
print(l)
fibo(10,l)
print(l)
fibo(100,l)
print(l)
