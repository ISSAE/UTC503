class Exp:
    ''' class (interface) racine
        des expressions arithmetiques simple
    '''
    def eval(self):
        ''' Valeur résultat de l'expression '''
        assert not isinstance(self, Exp), "Uniquement eval des sous classe!"
        return self.eval()

    def simplifie(self):
        ''' Simplifier l'expression '''
        assert not isinstance(self, Exp), "Uniquement simplifie des sous classe!"
        return self.simplifie()

    def postFixe(self):
        assert not isinstance(self, Exp), "Uniquement postfixe des sous classe!"
        return self.posteFixe()

    def __str__(self):
        ''' Representation textuelle de l'expression '''
        pass

class Const(Exp):
    def __init__(self, v):
        self.e=v

    def eval(self):
        ''' L'evaluation d'une constante est sa valeur représenté
            par e (numérique en principe)
        '''
        return self.e

    def simplifie(self):
        ''' Une constante est déjà la version 
            la plus simplifié possible 
        '''
        return self

    def postFixe(self):
        return str(self)

    def __str__(self):
        return f"C:{self.e}"


''' Exemple
>>> e1=Const(2)
>>> e1
<__main__.Const object at 0x7fe3f19bcbe0>
>>> str(e1)
'C:2'
>>> print(e1)
C:2
>>> e2=Const(3.0)
>>> e2
<__main__.Const object at 0x7fe3f19bcc50>
>>> print(e2)
C:3.0
>>> e2.e
e2.e      e2.eval(  
>>> e2.eval()
3.0
>>> Exp.eval(e2)
>>> Const.eval(e2)
3.0
>>> 
'''

def myEval(e):
    return e.eval()