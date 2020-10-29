'''
If you want to sort things in some order other than the “natural” or its reverse, you can provide an additional
parameter, the key parameter
'''

L1 = [1, 7, 4, -2, 3]

def absolute(x):
    if x >= 0:
        return x
    else:
        return -x

print(absolute(3))
print(absolute(-119))

for y in L1:
    print(absolute(y))
    
    
'''
Now, we can pass the absolute function to sorted in order to specify that we want the items sorted in order of their
absolute value, rather than in order of their actual value.
'''
L1 = [1, 7, 4, -2, 3]

def absolute(x):
    if x >= 0:
        return x
    else:
        return -x

L2 = sorted(L1, key=absolute)
print(L2)

#or in reverse order
print(sorted(L1, reverse=True, key=absolute))




#To illustrate that the absolute function is invoked once on each item, during the execution of sorted, I have added
#some print statements into the code.
L1 = [1, 7, 4, -2, 3]

def absolute(x):
    print("--- figuring out what to write on the post-it note for " + str(x))
    if x >= 0:
        return x
    else:
        return -x

print("About to call sorted")
L2 = sorted(L1, key=absolute)
print("Finished execution of sorted")
print(L2)


















