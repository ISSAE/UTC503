def P(l,x):
    ''' Calcul P(x)= 
        a_0 + a_1 * x**1 + ... a_i x**i + ... + x_n x**n
        avec l = [a_0,a_1,...a_i,...a_n]
    '''
    if l == []: return 0
    else: return l[0]+x*P(l[1:],x)

def PIter(l,x):
    P=0
    while l:
        P = x*P + l[0]
        l=l[1:]
    return l

def PWhile(l,x):
    i=0
    P=0
    xk=1
    while (i< len(l)):
        P= P+ l[i]*xk
        xk=x*xk
        i=i+1
    return P

if __name__ == '__main__':
    assert P([],10) == 0
    assert P([1,1],10) == 11 
    assert P([1,1,1],10) == 111
    assert P([8,5,1],10) == 158

