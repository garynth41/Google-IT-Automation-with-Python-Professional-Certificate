#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 18:34:08 2020

@author: garyt
"""
"""
The file_date function creates a new file in the current working directory, checks the date that the file was modified, and returns just the date portion of the timestamp in the format of yyyy-mm-dd. Fill in the gaps to create a file called "newfile.txt" and check the date that it was modified.
"""
#import os
#import datetime
#
#def file_date(filename):
#  # Create the file in the current directory
#  full_name = os.path.join(filename)
#  file = open(full_name, "w")
#  timestamp = os.path.getmtime(filename)
#  # Convert the timestamp into a readable format, then into a string
#  result = datetime.datetime.fromtimestamp(timestamp)
#  # Return just the date portion 
#  # Hint: how many characters are in “yyyy-mm-dd”? 
#  return ("{:<9}".format(str(result)))
#
#print(file_date("newfile.txt")) 
## Should be today's date in the format of yyyy-mm-dd

import os
import datetime

def file_date(filename):
  
# Create the file in the current directory
  open(filename,"w").close()
  timestamp = os.path.getmtime(filename)
 #Convert the timestamp into a readable format, then into a string
  result = datetime.datetime.fromtimestamp(timestamp).isoformat()

# Return just the date portion
# Hint: how many characters are in “yyyy-mm-dd”?
  return ("{}".format(result[:10]))

print(file_date("newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd




