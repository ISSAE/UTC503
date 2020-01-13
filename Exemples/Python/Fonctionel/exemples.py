inc = lambda x: x+1
applique10 = lambda f: f(10)

applique10(inc)
# >>> 11

LunOuLautre = lambda c : lambda ev : lambda ef : ev if c else ef

LunOuLautre(10)('vraie apparement')(-1) 
# 'vraie apparement'
LunOuLautre(0)('vraie apparement')(-1) 
# -1
LunOuLautre(False)('vraie apparement')(-1) 
# -1
LunOuLautre(['liste Non vide'])('vraie apparement')(-1) 
# 'vraie apparement'