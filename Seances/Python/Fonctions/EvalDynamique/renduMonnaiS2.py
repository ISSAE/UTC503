_systemePieces=[100,50,20,10,5,1]
_somme=153

#un système de pièce doit toujour contenir 1 comme plus petite pièce
def rendreUneSolution(somme=_somme,sp=_systemePieces):
    if(sp[0] == 1):
        return {1:somme} #nous n'avons plus que 1 donc la réponse est somme pièce de 1 {1:somme}
    else:
        pg=sp[0] #La plus grande piece de l'ensenble
        q=somme//pg # Le nombre possible de rendu pour la piece pg par exemple 353 avec 100 donne 3
        r=somme%pg # ce qui reste a rendre avec les autres pièces exemple 353 (si 3*100 reste 53)
        return {pg:q,**rendreUneSolution(r,sp[1:])} #renvoyer q pièce et continuer le rendu avec le reste sans la première pièce

# Exemple
# >>> rendreUneSolution()
#{100: 1, 50: 1, 20: 0, 10: 0, 5: 0, 1: 3}

def rendreTouteSolution(somme=_somme,sp=_systemePieces):
    # print(somme,sp,sp[0])
    if sp[0] == 1:
        #La somme restante doit être rendu entièrement avec des pièces de 1
        return [{1:somme}]
    else:
        # En principe il y a encore plusieurs pièces dans le système
        pg=sp[0]
        q=somme//pg # nombre max de pièce pg
        return flatten([ensemblePossibilité(somme, sp[0],v,sp[1:]) for v in range(q+1)]) #flatten pour éviter d'avoir une liste de liste

#exemple
#>>> rendreTouteSolution(17,(10,5,1))
#[{10: 0, 5: 0, 1: 17}, {10: 0, 5: 1, 1: 12}, {10: 0, 5: 2, 1: 7}, {10: 0, 5: 3, 1: 2}, {10: 1, 5: 0, 1: 7}, {10: 1, 5: 1, 1: 2}]


#Pour un nombre de piece pour une piece donne {piece:mbPiece} renvoit le système rendu en 
#concaténant {piece:nbPice} a toute les solutions
#réponse un eliste de solution
def ensemblePossibilité(somme, piece, nbPieces, restePieces):
    # print(f"dans ensemble {rendreTouteSolution(somme-nbPieces*piece,restePieces)}")
    return [{piece:nbPieces,**t} for t in rendreTouteSolution(somme-nbPieces*piece,restePieces)]
#Exemple
''' rendre 17 sachant 1 pièce de 10 avec le reste de pièce (5,1)
>>> ensemblePossibilité(17,10,1,(5,1))
7 (5, 1) 5
7 (1,) 1
dans ensemble [{1: 7}]
7 (1,) 1
2 (1,) 1
dans ensemble [{1: 2}]
2 (1,) 1
dans ensemble [{5: 0, 1: 7}, {5: 1, 1: 2}]
7 (5, 1) 5
7 (1,) 1
dans ensemble [{1: 7}]
7 (1,) 1
2 (1,) 1
dans ensemble [{1: 2}]
2 (1,) 1
[{10: 1, 5: 0, 1: 7}, {10: 1, 5: 1, 1: 2}]
'''

#Liste de liste devient une liste simple
flatten = lambda l: [item for sublist in l for item in sublist]

#exemple et test
if __name__ == '__main__':
    assert rendreUneSolution() == [(100, 1), (50, 1), (20, 0), (10, 0), (5, 0), (1, 3)]
    print(rendreUneSolution(153,[100,50,20,10,5,1]))
    assert rendreTouteSolution() == [[(100, 0), (50, 3), (20, 0), (10, 0), (5, 0), (1, 3)], [(100, 1), (50, 1), (20, 0), (10, 0), (5, 0), (1, 3)]]
    print(rendreTouteSolution(153,[100,50,20,10,5,1]))
