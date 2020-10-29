# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 06:36:41 2020

@author: garyn
"""
#What is a dictionary?
x = {}
type(x)
'''
The "toc" dictionary represents the table of contents for a book. Fill in the blanks to do the
following: 1) Add an entry for Epilogue on page 39. 2) Change the page number for Chapter 3 to 24.
3)Display the new dictionary contents. 4) Display True if there is Chapter 5, False if there isn't.
'''
toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
 # Epilogue starts on page 39
toc["Epilogue"] = 39
 # Chapter 3 now starts on page 24
toc["Chapter 3"] = 24
# What are the current contents of the dictionary?
print(toc)
# Is there a Chapter 5?
print("Chapter 5" in toc)

#test
'''Here is your output:
{'Introduction': 1, 'Chapter 1': 4, 'Chapter 2': 11, 'Chapter 3': 24, 'Chapter 4': 30, 'Epilogue':
    39} False

Great work! You've made the changes to the dictionary
exactly as requested.
'''

#Iterating over the Contents of a Dictionary
file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for extensions in file_counts:
    print(extensions)

for ext, amount in file_counts.items():
    print("There are {} fo;es with the .{} extension".format(amount, ext))

#Now, it's your turn! Have a go at iterating over a dictionary!
'''
Complete the code to iterate through the keys and values of the cool_beasts dictionary. Remember
that the items method returns a tuple of key, value for each element in the dictionary
'''

cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for key, value in cool_beasts.items():
    print("{} have {}".format(key, value))

# Here is your output:
# octopuses have tentacles
# dolphins have fins
# rhinos have horns

# Nice job! Your dictionary skills are getting stronger and
# stronger!


#function to count num of letter in a string
def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

count_letters("this")
count_letters("aaaaa")

"""
In Python, a dictionary can only hold a single value for a given key. To workaround this, our single
value can be a list containing multiple values. Here we have a dictionary called "wardrobe" with
items of clothing and their colors. Fill in the blanks to print a line for each item of clothing
with each color, for example: "red shirt", "blue shirt", and so on.
"""

wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for item in wardrobe.keys():
  for colors in wardrobe.get(item):
    print("{} {}".format(colors, item))

# Here is your output:
# red shirt
# blue shirt
# white shirt
# blue jeans
# black jeans

# Woohoo! You're really mastering the Python dictionaries and
# lists!
host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
host_addresses.keys()
host_addresses.items()

colors = ["red", "white", "blue"]
colors.insert(2, "yellow")
print(colors)

animal = "Hippopotamus"
print(animal[3:6])
print(animal[-5])
print(animal[10:])


