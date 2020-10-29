# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 17:58:09 2020

@author: garyn
"""

'''
Complete the body of the format_name function. This function receives first_name and last_name,
then prints a formatted string of "Name: last_name, first_name" if both names are not blank,
or "Name: " with just one of the names, if the other one is blank, and nothing if both are blank.
'''

def format_name(first_name, last_name):
  # code goes here
  if len(first_name)< 0 and len(last_name)< 0:
    return ""

  elif len(first_name)> 0 and len(last_name)>0:
    return "Name: "+last_name+ ", " +first_name

  elif len(first_name)< 0 and len(last_name)>0:
    return "Name: "+last_name+ ", " +first_name

  else:
    return "Name: " +""+ ", " +""


print(format_name("Ernest", "Hemingway"))
# Should be "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should be "Name: Madonna"

print(format_name("Voltaire", ""))
# Should be "Name: Voltaire"

print(format_name("", ""))
# Should be ""

# "Name: "+last_name+ ", " +first_name