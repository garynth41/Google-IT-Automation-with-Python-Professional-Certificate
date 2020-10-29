'''
The validate_users function is used by the system to check if a list of users is valid or invalid. A valid user is one that is at least 3
characters long. For example, ['taylor', 'luisa', 'jamaal'] are all valid users. When calling it like in this example, something is not right.
Can you figure out what to fix?
'''

def validate_users(users):
    for user in ['purplecat']:
        if is_valid(user):
            print(user + " is valid")
        else:
            print(user + " is invalid")

validate_users("purplecat")

'''
Here is your output:
purplecat is valid

Nice job! You figured out that you needed to call the
function with a list instead of just a string!
'''
