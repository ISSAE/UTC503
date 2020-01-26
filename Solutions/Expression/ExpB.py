from Exp import Exp,Const

class ExpB(Exp):
    _operateurs = {'+':'plus', '-':'moins'}
    def __init__(self,op, eg, ed):
        assert op in ExpB._operateurs, "Doit être un operateur connu"
        self.op = op
        assert isinstance(eg, Exp) and isinstance(ed, Exp), "eg et ed doivbent être des Exp"
        self.eg = eg
        self.ed = ed

    def eval(self):
        ''' Donner un sens au opération '''
        if self.op == '+':
            return self.eg.eval() + self.ed.eval()
        elif self.op == '-':
            return self.eg.eval() - self.ed.eval()
        else:
            raise ValueError('Pas opérateur encore connu')

    def simplifie(self):
        return Const(self.eval())

    def __str__(self):
        return f"({self.eg} {ExpB._operateurs[self.op]} {self.ed})"

    def postFixe(self):
       return f"{self.eg.postFixe()} {self.ed.postFixe()} {ExpB._operateurs[self.op]}"
    


e2=ExpB('+', Const(1), Const(2))
e3=ExpB('-', Const(3), e2)






