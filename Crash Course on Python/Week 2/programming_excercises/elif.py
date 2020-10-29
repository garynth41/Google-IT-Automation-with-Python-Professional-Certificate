# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 23:34:38 2020

@author: garyn
"""

"""
def valid_username(name):
    name = input("please enter a valid name")
    if len(name) < 3:
        print("please enter a name longer than 3 characters")
    elif len(name) > 15:
        print("nopes!, that name is too long")
    else:
        print("valid name")
"""


'''The number_group function should return "Positive" if the number received is positive,
"Negative" if it's negative, and "Zero" if it's 0. Can you fill in the gaps to make that happen?
'''

def number_group(number):
  if number > 0:
    return "Positive"
  elif number < 0:
    return "Negative"
  else:
    return "Zero"

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative