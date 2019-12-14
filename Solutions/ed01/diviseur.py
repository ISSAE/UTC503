def _diviseur(i , n):
    '''
       i est l'étape tel que
       aucun x avant i ne divise n
    '''
    if (n%i == 0):
        # Nou avons trouver le diviseur c'est i
        return i
    else:
        # Vhercher le diviseur dans la suite
        return _diviseur(i+1,n)

def diviseur(n):
    return _diviseur(2,n)

def deviseurIter(n):
    i=2
    while n%i != 0:
        i +=1
    return i

    

if __name__ == '__main__':
    assert diviseur(2)==2
    assert diviseur(3)==3
    assert diviseur(6)==2
    assert diviseur(9)==3
    assert diviseur(15)==3
    assert diviseur(17)==17
    for i in range(100):
        assert diviseur(n) == deviseurIter(n)