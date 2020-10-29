'''
# Modify the student_grade function using the format method, so that it returns the phrase "X received Y% on the exam". For
# example, student_grade("Reed", 80) should return "Reed received 80% on the exam".
# '''
# 
# def student_grade(name, grade):
#     return "{0} received {1}% on the exam".format(name, grade)
# 
# print(student_grade("Reed", 80))
# print(student_grade("Paige", 92))
# print(student_grade("Jesse", 85))
# 
# 
# print("-------")
# price = 7.5
# with_tax = price * 1.09
# #print(price, with_tax)
# print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))
# 
# 
# print("-------")
# def to_celsius(x):
#     return (x-32)*5/9
# 
# for x in range(0,101, 10):
#     print("{:>3} F | {:6.2f} C".format(x, to_celsius(x)))
# 
# print("-------------------------------")
# def convert_seconds(seconds):
#     hours = seconds // 3600
#     minutes = (seconds - hours * 3600) // 60
#     remaining_seconds = seconds - hours * 3600 - minutes * 60
#     return hours, minutes, remaining_seconds
# 
# result = convert_seconds(5000)
# print(type(result))
# print(result)
# 
# print("1-------")
# hours, minutes, remnaining_seconds = result
# print(hours, minutes, remnaining_seconds)
# 
# print("2-------")
# hours, minutes, remnaining_seconds = convert_seconds(1000)
# print(hours, minutes, remnaining_seconds)
# 
# """
# The guest_list function reads in a list of tuples with the name, age, and profession of each party guest, and prints the sentence
# "Guest is X years old and works as __." for each one. For example, guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'),
# ('Amanda', 25, "Engineer")) should print out:
# 
# Ken is 30 years old and works as Chef.
# Pat is 35 years old and works as Lawyer.
# Amanda is 25 years old and works as Engineer.
# Fill in the gaps in this function to do that.
# """
# def guest_list(guests):
#     for name, age, occup in guests:
#       print("{0} is {1} years old and works as {2}".format(name, age, occup))
# guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])
# 
# 
# 
# 
# print("=======================================")
# animals = ['Lion', 'Zebra', 'Dolphin', 'Monkey']
# 
# chars = 0
# for animal in animals:
#     chars = chars + len(animal)
# print("Total characters: {}, Average length: {}".format(chars, chars/ len(animals)))
# 
# 
# 
# 
# 
# print("=======================================")
# winners = ["Ashley", "Dylan", "Reese"]
# 
# for index, person in enumerate(winners):
#     print("{} - {}".format(index + 1, person))
# 
# 
# 
# print("=======================================")
# #iterating over list and tuples, week4
# def skip_elements(elements):
#     #return [ x for x in elements if elements.index(x) % 2 == 0 ]
#     return [elements[i] for i in range(len(elements)) if i % 2 == 0] 
# 
# print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
# print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']


def skip_elements(elements):
    #return [ x for x in elements if elements.index(x) % 2 == 0 ]
    #return [elements[i] for i in range(len(elements)) if i % 2 == 0]  
    new_list = []
    count = 0
    for index, value in enumerate(elements):
        if index % 2 == 0:
            new_list.append(value)
            count += 1
    return new_list
    

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']






















