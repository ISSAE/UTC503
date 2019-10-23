# coding: utf-8
# Décorateur / Wrapping de fonction
# Un exemple
def mon_decorateur(fonction):
    """Entourer une fonction Aspect O P"""
    def autre_fonction(*param, **param2):
        print("Action avant .............. ", param, param2)
        fonction(*param, **param2)
        print("Action après ..............", param, param2)
    return autre_fonction


@mon_decorateur
def do_that(v, x):
    """Une fonction simple pour montrer l'utilisation
    du wrapping"""
    print("Execution des instructions %s %d" % (v, x))

