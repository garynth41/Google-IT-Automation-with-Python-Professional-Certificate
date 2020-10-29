# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 19:11:38 2020

@author: garyn
"""

def print_prime_factors(number):
  # Start with two, which is the first prime
  factor =2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor+=1

  return "done"

print_prime_factors(100) # Should print 2,2,5,5