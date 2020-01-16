def rendreMonnai(s,sm):
    '''s : somme a rendre,
       sm: système de monnaie en oredre décroissant
    '''
    print(s,sm)
    if sm:
       nbPieceMax=s//sm[0]
       reste = rendreMonnai(s-(nbPieceMax*sm[0]), sm[1:])
       # print([nbPieceMax] + rep)
       return ((sm[0],nbPieceMax),)+ reste
    else:
        return ()

rendreMonnai(353,(100,50,10,5,1))