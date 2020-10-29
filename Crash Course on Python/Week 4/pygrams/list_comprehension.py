multiples = []

for x in range(1,11):
    multiples.append(x*7)
print(multiples)




print("=============")
multiples = [x * 7 for x in range(1,11)]
print(multiples)



print("=============")
languages = ["Python", "Java", "Ruby", "C", "C++", " Pearl", "Go"]

lengths = [len(language) for language in languages]
print(lengths)



print("=============")
z = [x for x in range(0,101) if x % 3 == 0]
print(z)


print("=============")
'''
Complete the skip_elements function to return every other element from the list, this time using a list comprehension to generate
the new list based on the previous one, where elements in odd positions are skipped.
'''
def skip_elements(elements):
    #return [x for x in elements(0:,2]  
    return [elements[i] for i in range(len(elements)) if i % 2 == 0] 

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']















