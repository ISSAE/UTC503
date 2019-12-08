def is_number(s):
    try:
        f=float(s)
        return (True, f) 
    except ValueError:
        return (False, s)

def next_num():
    num=is_number(input("Entrer un nombre: "))
    while not num[0]:
        num=is_number(input(" Erreur Entrer un nombre: "))
    return(num[1])
