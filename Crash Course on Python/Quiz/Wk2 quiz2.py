# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 18:17:54 2020

@author: garyn
"""
"""
This function sorts 2 numbers and returns them in increasing order.
Complete the function call, so that the resulting numbers are displayed in order.
"""

def order_numbers(number1, number2):
    if number2 > number1:
        return number1, number2
    else:
        return number2, number1

(smaller, bigger) = order_numbers(100, 99)


print(smaller, bigger)
