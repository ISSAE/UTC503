#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Un exemple de fonction f(x)=x**2-3
def f(x):
    return x**2 - 3

# Un autre exemple de fonction g(x)=x**3-5
def g(x):
    return x**3-5

# trouverZero recherche la silution de fonc(x)=0 entre u et v
# Avec précision 10**-n. Version itérative
def trouveZero(fonc,u,v,n):
    ''' recherche la solution de fonc(x)=0 entre u et v
        avec une précision infieur a 10 puissane -n

        :param fonc: la fonction
        :param u,v: l'interval [u,v] avec u<v
        :param n: la précision 10 puissance -n
        :return: la solution aproché
    '''
    while (v-u)>=10**(-n):   
        w=(u+v)/2
        # print("dans la boucle", u,v,f(u)*f(w))
        if fonc(u)*fonc(w) < 0:
            v=w
        else:
            u=w
    return (u+v)/2

# zero recherche la silution de fonc(x)=0 entre u et v
# Avec précision 10**-n. Version récusive
def zero(fonc,u,v,n):
    ''' recherche la solution de fonc(x)=0 entre u et v
        avec une précision infieure à 10 puissane -n

        :param fonc: la fonction
        :param u,v: l'interval [u,v] avec u<v
        :param n: la précision 10 puissance -n
        :return: la solution aproché

        :Remarque: 
        
        on verifie qu'une solution peut exister fonc(u)*fonc(v) <0
    '''
    assert fonc(u)*fonc(v)<0,"pas de solution entre "+str(u)+" et "+ str(v)
    # print(u,fonc(u),v,fonc(v))
    if (v-u)<10**(-n):
        # la présion est suffisante solution entre u et v on choisi le milieu
        return (u+v)/2
    else:
        # w milieu de u,v
        w=(u+v)/2
        if fonc(u)*fonc(w) < 0:
            #La solution est entre u et w
            return zero(fonc,u,w,n)
        else:
            #la solution est entre w et v
            return zero(fonc,w,v,n)


u=int(input("u="))
v=int(input("v="))
n=int(input("n="))
reponse=trouveZero(f,u,v,n)
print(reponse)
print(f(reponse))
reponse=zero(f,u,v,n)
print(reponse)
print(f(reponse))
deff=input("entrer la definition de la fonction avec une variable x=")
inf=eval(f"lambda x: {deff}")
print(zero(inf,u,v,n))



