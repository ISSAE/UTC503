# coding: utf-8
# Décorateur / Wrapping de fonction
# Un exemple
def mon_decorateur(fonction):
    """Entourer une fonction Aspect O P"""
    def autre_fonction(*param, **param2):
        print("Action avant .............. ", param, param2)
        res=fonction(*param, **param2)
        print("Action après ..............", res)
        return res
    return autre_fonction


@mon_decorateur
def do_that(v, x):
    """Une fonction simple pour montrer l'utilisation
    du wrapping"""
    print("Execution des instructions %s %d" % (v, x))
    return(v,x)

# @mon_decorateur equivalent a do_that=mon_decorateur(do_that)

print(f"Je print {do_that(1,2)}")