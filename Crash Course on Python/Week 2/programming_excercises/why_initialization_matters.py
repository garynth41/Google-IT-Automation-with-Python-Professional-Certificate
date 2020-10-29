# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 16:11:59 2020

@author: Gary N. Thomas
"""

def count_down(start_number):
  start_number = 0
  current = 3

  while (current > 0):
    print(current)
    current -= 1
  print("Zero!, blast off!!")

count_down(3)