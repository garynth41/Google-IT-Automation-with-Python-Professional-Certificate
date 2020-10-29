"""
16.2. Optional reverse parameter
The sorted function takes some optional parameters (see the Optional Parameters page). The first optional parameter is a key function, which will be
described in the next section. The second optional parameter is a Boolean value which determines whether to sort the items in reverse order. By default,
it is False, but if you set it to True, the list will be sorted in reverse order.
"""
L2 = ["Cherry", "Apple", "Blueberry"]
print(sorted(L2, reverse=True))
print(sorted(L2, reverse=False))




"""
Note:
This is a situation where it is convenient to use the keyword mechanism for providing optional parameters. It is possible to provide the value True for
the reverse parameter without naming that parameter, but then we would have to provide a value for the second parameter as well, rather than allowing the
default parameter value to be used. We would have had to write sorted(L2, None, True). That’s a lot harder for humans to read and understand.
"""

# Sort the list, lst from largest to smallest. Save this new list to the variable lst_sorted.
lst = [3, 5, 1, 6, 7, 2, 9, -2, 5]
lst_sorted = sorted(lst, reverse=True)

print(lst_sorted)
