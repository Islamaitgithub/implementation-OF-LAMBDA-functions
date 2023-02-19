# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 13:28:18 2023

@author: Admin
"""

def make_keeper(n):
    def foo(cond):
        for x in range(1,n+1):
            if cond(x):
                print(x,end=" ")
        print()
    return foo
def is_even(n):
    return(n%2==0)
def is_odd(n):
    return(n%2!=0)
make_keeper(6)(is_even)
make_keeper(10)(is_odd)