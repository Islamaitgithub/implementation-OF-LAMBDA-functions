# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 13:27:17 2023

@author: Admin
"""


def summation(n,term):
    total,k=0,1
    while k<=n:
        total,k=total+term(k),k+1
    return total
def natural(k):
    return k
def cube(k):
    return k**3
print(summation(3,natural))