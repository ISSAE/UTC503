"""
Module polynome : à tester avec -m doctest -v


>>> p=Polynome0([1,2,3,4])
>>> print(p(10))
1234
"""

def polynome(coef):
    """ 
        coef coefficient d'un polynome P(x)=co_0 + co_1*x^1 + ... co_n*c^n 
        résultat fonction p(x) : la fonction définissant le polynome 
        
        Exemples :
        
        >>> polynome([1,1])(2)  
        3
        >>> polynome([1,1])(10) 
        11
        >>> polynome([1,2])(10) 
        21
        >>> polynome([1,2,3,4])(10) 
        4321
        >>> P1234=polynome([1,2,3,4]) 
        >>> P1234(10)
        4321
        >>> P1234(1)  
        10
        >>> P1234(2) 
        49
        """
    def p(x):
        if coef:
            return coef[0]+ x*polynome(coef[1:])(x)
        else:
            return 0
    return p

#Version avec Objet callable
class Polynome0:
    def __init__(self,coefs):
        self.coefs=coefs

    def __call__(self, x):
        ''' Traduction de l'algorythme récursif en
            impératif 
            
        >>> p=Polynome([1,2,3,4])
        >>> print(p(10))
        1234
        '''
        # return coef[0]+ x*polynome(coef[1:])(x)
        # Pnext = coef[0] + x*Pprecedent
        # Pprecedent avec le parametre coef = coef[1:]
        # ce qui donne
        coef=self.coefs
        P=0
        while(coef):
            P=coef[0]+x*P
            coef = coef[1:]
        return P

class Polynome:
    '''
       Polynome : 
         attrinut d'instance coefs

    Exemples:

    >>> p=Polynome([1,2,3,4])
    '''
    def __init__(self,coefs):
        self.coefs=coefs

    def __call__(self, x):
        ''' Traduction de l'algorythme récursif en
            impératif 
        
        Exemple:
        >>> print(Polynome([1,2,3,4])(10))
        1234
        '''
        P=0
        tete=0
        # optimisation pour éviter coefs=coef[1:]
        while(tete < len(self.coefs)):
            P=self.coefs[tete]+x*P
            tete = tete + 1
        return P

p=Polynome([1,2,3,4])
print(p(10))
