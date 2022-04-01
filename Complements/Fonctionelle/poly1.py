def poly1(a, b):
    ''' a et b les coéficients du polynome ax+b
    '''
    def calcul(x):
        ''' A partir de a et b calculer a*x+b '''
        return a*x + b
    return calcul