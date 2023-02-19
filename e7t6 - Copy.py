# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 13:30:03 2023

@author: Admin
"""

add_one=lambda x:x+1
square=lambda x:x*x
def composite_identity(f,g):
    def foo(x):
        return f(g(x))==g(f(x))
    return foo 
a1=composite_identity(add_one,square)
print(a1(0))
print(a1(4))   