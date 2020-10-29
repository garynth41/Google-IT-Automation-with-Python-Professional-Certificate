'''
The is_palindrome function checks if a string is a palindrome. A palindrome is a string that can be equally read from left to right
or right to left, omitting blank spaces, and ignoring capitalization. Examples of palindromes are words like kayak and radar, and
phrases like "Never Odd or Even". Fill in the blanks in this function to return True if the passed string is a palindrome, False
if not.
'''
#1.
def is_palindrome(input_string):
    # We'll create two strings, to compare them
    new_string = ""
    reverse_string = ""
    # Traverse through each letter of the input string
    for i in input_string:
        # Add any non-blank letters to the 
        # end of one string, and to the front
        # of the other string. 
        if input_string == input_string.lower():
            new_string = input_string.replace(' ', '')
            reverse_string =''.join(reversed(new_string))
    # Compare the strings
    if reverse_string == new_string:
      return True
    return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True

print("-------")
#2.
'''
Using the format method, fill in the gaps in the convert_distance function so that it returns the phrase "X miles equals Y km",
with Y having only 1 decimal place. For example, convert_distance(12) should return "12 miles equals 19.2 km".
'''
def convert_distance(miles):
    km = miles * 1.6 
    result = "{} miles equals {:.1f} km".format(miles, km)
    return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km

print("-------")
'''
The group_list function accepts a group name and a list of members, and returns a string with the format: group_name: member1,
member2, … For example, group_list("g", ["a","b","c"]) returns "g: a, b, c". Fill in the gaps in this function to do that.
'''

def group_list(group, users):
  members = users
  return members


print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"

