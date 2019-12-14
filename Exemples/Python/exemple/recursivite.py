def taille(l):
    if l == []: return 0
    else: return 1+ taille(l[1:])

def somme(l):
    if l == []: return 0
    else: return l[0]+somme(l[1:])