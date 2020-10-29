# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 00:14:31 2020

@author: Gary N. Thomas
"""

def smallest_prime_factor(x):
    """Returns the smallest prime number that is a divisor of x"""
    # Start checking with 2, then move up one by one
    n = 2
    while n <= x:
        if x % n == 0:
            return n
        n+=1 # increase n by 1 so it tests 2, then 3, then 4 ...

print(smallest_prime_factor(12)) # should be 2
print(smallest_prime_factor(15)) # should be 3







#Infinite loop bug concept
'''
if x != 0:
    while x % 2 == 0:
        x = x / 2

s

while x != 0 and x % 2 == 0:
    x = x / 2
'''
