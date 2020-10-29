#Working with lists
fruits = ['Pineapple', 'Banana', 'Apple', 'Melon']

fruits.append('Grapes')
print(fruits)

print("====================================================================")
fruits.insert(0,'Cherries')
print(fruits)

print("====================================================================")
fruits.remove('Melon')
print(fruits)

print("====================================================================")
fruits.pop(2)
print(fruits)

print("=================================================")
#The skip_elements function returns every other element from the list, starting from the first. Complete this function to do that.
def skip_elements(elements):
    return elements[::2]

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []


#Lists and Tuples
#list are muatble, tuples are immutable.






















