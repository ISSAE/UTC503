def f(x):
    ''' Fonction pour essayer l'imbrication

        Contient une sous fonction g
    '''
    def g(y):
        return x+y
    return g(x)+100

def g1(y):
    return x+y

def f1(x):
    return g1(x)+100