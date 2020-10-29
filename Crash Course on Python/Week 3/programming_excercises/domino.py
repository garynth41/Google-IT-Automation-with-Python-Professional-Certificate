for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()
print("==============================")    

teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)
            
 
# The validate_users function is used by the system to check if a list of users is valid or invalid. A valid user
# is one that is at least 3 characters long. For example, ['taylor', 'luisa', 'jamaal'] are all valid users. When calling
# it like in this example, something is not right. Can you figure out what to fix? 
 
#  
# print("==============================") 
# def validate_users(users):
#   for user in ['purplecat']:
#     if is_valid(user):
#       print(user + " is valid")
#     else:
#       print(user + " is invalid")
# 
# validate_users("purplecat")
#             