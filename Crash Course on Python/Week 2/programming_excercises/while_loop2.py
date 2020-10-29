# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 16:01:11 2020

@author: garyn
"""

def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")

attempts(5)