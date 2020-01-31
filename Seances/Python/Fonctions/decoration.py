# coding: utf-8
# Décorateur / Wrapping de fonction
# Un exemple
def mon_decorateur(fonction):
    """Entourer une fonction Aspect O P"""
    def autre_fonction(*param, **param2):
        print("Action avant .............. ", param, param2)
        if (param and param2): 
            fonction(*param, **param2)
        elif param:
            fonction(*param)
        else:
            fonction(**param2)
        print("Action après ..............", param, param2)
    return autre_fonction

def fact(n):
    if n==0: return 1
    else: return n*fact(n-1)

@mon_decorateur
def do_that(v, x):
    """Une fonction simple pour montrer l'utilisation
    du wrapping"""
    print("Execution des instructions %s %d" % (v, x))
    return(v,x)

# @mon_decorateur equivalent a do_that=mon_decorateur(do_that)

print(f"Je print {do_that(1,2)}")