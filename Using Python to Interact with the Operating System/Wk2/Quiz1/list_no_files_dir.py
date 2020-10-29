#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 18:32:39 2020

@author: garyt
"""
"""
The new_directory function creates a new directory inside the current working directory, then creates a new empty file inside the new directory, and returns the list of files in that directory. Complete the function to create a file "script.py" in the directory "PythonPrograms".
"""

import os
def new_directory(directory, filename):
    os.makedirs(directory, exist_ok=True)
    os.chdir(directory)
    with open(filename, 'w') as file:
        file.write("")
    os.chdir("..")
    return(os.listdir(directory))
print(new_directory("PythonPrograms", "script.py"))
