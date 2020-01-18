_systemePieces=[100,50,20,10,5,1]
_somme=153
#exemple redre 153 => [(100,1),(50,1),(20,0),(5,0),(1,3)]
def rendreUneSolution(somme=_somme,sp=_systemePieces):
    #la priece la plus grande
    if sp:
        pg=sp[0]
        #somme=q*pg+r
        q=somme//pg
        r=somme%pg
        return [(pg,q),*rendreUneSolution(r,sp[1:])]
    else:
        return []

def rendreTouteSolution(somme=_somme,sp=_systemePieces):
    print(somme,sp,sp[0])
    if sp[0] == 1:
        #La somme restante doit être rendu entièrement avec des pièces de 1
        return [[{1:somme}]]
    else:
        # En principe il y a encore plusieurs pièces dans le système
        pg=sp[0]
        #somme=q*pg+r
        q=somme//pg
        # r=somme%pg
        return [ensemblePossibilité(somme, sp[0],v,sp[1:]) for v in range(q+1)]

def ensemblePossibilité(somme, piece, nbPieces, restePieces):
    print(f"dans ensemble {rendreTouteSolution(somme-nbPieces*piece,restePieces)}")
    return [{piece:nbPieces,**t} for t in flatten(rendreTouteSolution(somme-nbPieces*piece,restePieces))]

flatten = lambda l: [item for sublist in l for item in sublist]

#exemple et test
if __name__ == '__main__':
    assert rendreUneSolution() == [(100, 1), (50, 1), (20, 0), (10, 0), (5, 0), (1, 3)]
    print(rendreUneSolution(153,[100,50,20,10,5,1]))
    assert rendreTouteSolution() == [[(100, 0), (50, 3), (20, 0), (10, 0), (5, 0), (1, 3)], [(100, 1), (50, 1), (20, 0), (10, 0), (5, 0), (1, 3)]]
    print(rendreTouteSolution(153,[100,50,20,10,5,1]))
