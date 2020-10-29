'''
In math, the factorial of a number is defined as the product of an integer and all the integers below it. For example, the factorial of four
(4!) is equal to 1*2*3*4=24. Fill in the blanks to make the factorial function return the right number.
'''
def factorial(n):
    result = 1
    
    for i in range(1, 1+n):
      result = result*i
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120

'''
Here is your output:
24
120
Well done, you! The pieces of code you're tackling keep getting more complex, but you're doing a great job!
'''
