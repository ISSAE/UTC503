#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import m1
def f(x):
    return m1.x+x

x='tititototo'

def g(x):
    return m1.f(100)
    
def jeSuis():
    print("dans m2")

print("Dans le fichier m2.py", __name__)