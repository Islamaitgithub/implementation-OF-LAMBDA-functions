# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 13:28:13 2023

@author: Admin
"""

def multiply_by(m):
    def multiply(n):
        return m*n
    return multiply
times_three=multiply_by(3)
print(times_three(5))
print(times_three(100))