'''
Module lisp : LISt Processing inspiré du langage Lisp du même nom

Exemple d'utilisation et test:

>>> tete(cons(1,[]))
1
>>> reste(cons(1,[]))
[]
>>> reste(cons(1,[2,3]))
[2, 3]
>>> tete([])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/pascalfares/mesgit/UTC503/util/lisp.py", line 12, in tete
    assert l, "La tete n'existe pas ! si la liste est vide..."
AssertionError: La tete n'existe pas ! si la liste est vide...
>>> tete([1,2,3,4])
1

>>> cons(tete([1,2,3]),reste([1,2,3])) == [1,2,3]
True
'''
# tête de la liste : car en lisp
# tete = lambda l: l[0]
def tete(l):
    ''' l      : IN liste
        return : la tete, le premier élément de la liste

        propriété: cons(tete(l),reste(l)) = l
    '''
    assert l, "La tete n'existe pas ! si la liste est vide..."
    return l[0]  

#reste de la liste : cdr en lisp
# reste = lambda l : l[1:]
def reste(l):
    ''' l      : IN liste
        return : reste de la liste (sans le premier élément)

        propriété: cons(tete(l),reste(l)) = l
    '''
    return l[1:]
#_Cons version fabrique : _cons(tete(l))(reste(l)) = l
#permet de définir une fonction de construction d'un élément
#aux liste : c1=_cons(e) c1 est la fonction qui ajoute en 
# tête e à une liste
# _cons = lambda a: lambda l: [a,*l]
def _cons(t):
    ''' Fabrique la fonction cons a partir de l'élément t
        à ajouter
        t:   IN la nouvelle tête

        return: La fonction interne qui pour une liste l ajoute t en tête
            fonction interne:
            ajoute en tete de l un element t issue de la fermeture de 
            cette fonction

            l: IN la liste 
            return : la nouvelle liste avec t en tete [t,les elements de l]
            propriété: _cons(tete(l))(reste(l)) = l
        
        equivalent à , lambda t: lambda l: [t,*l]   
    '''
    def ajouterTete(l):
        return [t,*l]
    return ajouterTete

#cons version fonction 2 paramétres
# cons = lambda a,l: _cons(a)(l)
def cons(t,r):
    '''
       t: un élément
       r: une liste

       résulta: la nouvelle liste t,les élements de r
       propriété: cons(tete(l),reste(l)) = l
    '''
    return _cons(t)(r)


if __name__ == '__main__':
    ''' Pour tester utilise les commentaire du code '''
    import doctest
    doctest.testmod()