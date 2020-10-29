'''
Iterating Over Dictionaries:
You can iterate over dictionaries using a for loop, just like with strings, lists, and tuples. This will iterate over the sequence
of keys in the dictionary. If you want to access the corresponding values associated with the keys, you could use the keys as
indexes. Or you can use the items method on the dictionary, like dictionary.items().

This method returns a tuple for each element
in the dictionary, where the first element in the tuple is the key and the second is the value. If you only wanted to access the
keys in a dictionary, you could use the keys() method on the dictionary: dictionary.keys(). If you only wanted the values, you
could use the values() method: dictionary.values().

Complete the code to iterate through the keys and values of the cool_beasts dictionary. Remember that the items method returns a
tuple of key, value for each element in the dictionary.
'''

cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}

for key, value in cool_beasts.items():
    print("{} have {}".format(key, value))
    
    
print("---------------")
# In Python, a dictionary can only hold a single value for a given key. To workaround this, our single value can be a list containing
# multiple values. Here we have a dictionary called "wardrobe" with items of clothing and their colors. Fill in the blanks to print
# a line for each item of clothing with each color, for example: "red shirt", "blue shirt", and so on.

wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for item in wardrobe.keys():
  for colors in wardrobe.get(item):
    print("{} {}".format(colors, item))