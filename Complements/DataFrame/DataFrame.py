class DataFrame:
    def __init__(self,champs):
        self.champs=champs
        self.donnees=[]

    def insert(self,ligne):
        self.donnees.append(ligne)

    def _strLigne(ligne):
        from functools import reduce
        return reduce(lambda acc,s: f"{acc}\t{s}",ligne)

    def _strMultiLigne(mligne):
        from functools import reduce
        return reduce(lambda acc,s: f"{acc}\n{DataFrame._strLigne(s)}",mligne,'---')

    def __str__(self):
        return f"""
                {DataFrame._strLigne(self.champs)}
                {DataFrame._strMultiLigne(self.donnees)}
        """
    #On peut écrire les méthodes comme ceci aussi
    _getIndex = lambda self, nomChamp: self.champs.index(nomChamp)
    
    def _projection(self,l,*param):
        if param:
            return [l[self._getIndex(p)] for p in param]
        else:
            return l
    
    def _conditions(self,l,**params):
        if params:
            return all([params[p](l[self._getIndex(p)]) for p in params])
        else:
            return l

    def selectWhere(self,*param,**params):
        print(param,params)
        return [self._projection(l,*param) for l in self.donnees if self._conditions(l,**params)]

df=DataFrame(['Nom', 'Prenom', 'tel', 'email']) # create table ;)
df.insert(['Emile', 'Dupont', '336xxyyzzww', 'de@isae.edu.lb'])
df.insert(['Pascal', 'Fares', '03xxxyyy', 'pf@isae.edu.lb'])

print(df._conditions(['Emile', 'Dupont', '336xxyyzzww', 'de@isae.edu.lb'],
               Nom=lambda n: n=='Emile'))

print(df._projection(['Emile', 'Dupont', '336xxyyzzww', 'de@isae.edu.lb'],
               'Nom'))

df.selectWhere('Nom', 'tel', Nom=lambda n: n>'F')
