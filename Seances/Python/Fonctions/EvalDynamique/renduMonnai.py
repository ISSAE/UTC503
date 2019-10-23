systemePieces=[100,50,20,10,5,1]
somme=1523
#exemple redre 153 => [(100,1),(50,1),(20,0),(5,0),(1,3)]
def rendreUneSolution(somme,sp=systemePieces):
    #la priece la plus grande
    if sp:
        pg=sp[0]
        #somme=q*pg+r
        q=somme//pg
        r=somme%pg
        return [(pg,q),*rendreUneSolution(r,sp[1:len(sp)])]
    else:
        return []

def rendreTouteSolution(somme,sp=systemePieces):
    #la priece la plus grande
    if sp:
        pg=sp[0]
        #somme=q*pg+r
        q=somme//pg
        # r=somme%pg
        return [[(pg,v),*rendreUneSolution(somme-v*pg,sp[1:len(sp)])] for v in range(q+1)]
    else:
        return []

