# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 13:29:16 2023

@author: Admin
"""

def square(x):
    return x*x
def triple(x):
    return 3*x
def compose(a,b):
    def foo(x):
        return(a(b(x)))
    return foo
squiple=compose(square,triple)
tripare=compose(triple,square)
print(squiple(3))
print(tripare(3))