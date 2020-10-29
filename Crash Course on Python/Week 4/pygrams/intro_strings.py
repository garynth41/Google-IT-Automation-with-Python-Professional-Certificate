'''
Want to give it a go yourself? Be my guest! Modify the first_and_last function so that it returns True if the first letter of
the string is the same as the last letter of the string, False if they’re different. Remember that you can access characters
using message[0] or message[-1]. Be careful how you handle the empty string, which should return True since nothing is equal
to nothing.
'''

def first_and_last(message):
  if len(message) == 0:
    return True
  elif message[0] == message[-1]:
    return True
  else:
    return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))

print("-------------------------")
word = "supercalifragilisticexpialidocious"
print(word.index('x'))


























