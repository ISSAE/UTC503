import premierDeg as pd

def _delta(a,b,c):
    return b**2 - 4*a*c

def secondDeg(a,b,c):
    if (a==0): return pd.premierDegre(b,c)
    else:
        delta=_delta(a,b,c)
        if (delta >0): 
            da= 2*a
            return ((-b -delta**0.5)/da,(-b+delta**0.5)/da)
        elif delta<0:
            return "Pas de solutions"
        else: return -b/2*a

#test et exemples
if __name__ == '__main__':
    assert secondDeg(0,1,-1)==1
    print(secondDeg(0,1,-1))
    assert secondDeg(1,1,-2)==(-2.0, 1.0)
    print(secondDeg(1,1,-2))
    assert secondDeg(1,3,2)==(-2.0, -1.0)
    print(secondDeg(1,3,2))
    assert secondDeg(1,1,1)=='Pas de solutions'
    print(secondDeg(1,3,2))
    assert secondDeg(1,2,1)==-1.0
    print(secondDeg(1,2,1))
    

