def taille_(l):
    if l:
        return 1+taille_(l[1:])
    else:
        return 0

def sommeL(l):
    if l:
        return l[0]+sommeL(l[1:])
    else:
        return 0

def moyenne(l):
    return (sommeL(l)/taille_(l))

def coupleRep(l, st):
    return (1+st[0], l[0]+st[1])

def sommeTaille(l):
    if l:
        # st=sommeTaille(l[1:])
        # return (1+st[0], l[0]+st[1])
        return coupleRep(l, sommeTaille(l[1:]))
    else:
        return (0,0)

def moyenne_(st):
    return(st[1]/st[0])

def moyenneOpt(l):
    moyenne_(sommeTaille(l))