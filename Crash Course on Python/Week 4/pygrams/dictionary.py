'''
The "toc" dictionary represents the table of contents for a book. Fill in the blanks to do the following: 1) Add an entry for
Epilogue on page 39. 2) Change the page number for Chapter 3 to 24. 3) Display the new dictionary contents. 4) Display True if
there is Chapter 5, False if there isn't.
'''

toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
#Epilogue starts on page 39
toc["Epilogue"] = 39

# Chapter 3 now starts on page 24
toc["Chapter 3"] = 24

# What are the current contents of the dictionary?
print(toc)

# Is there a Chapter 5?
print("Chapter 5" in toc)



'''
1.
The email_list function receives a dictionary, which contains domain names as keys, and a list of users as values. Fill in the
blanks to generate a list that contains complete email addresses (e.g. diana.prince@gmail.com).
'''
def email_list(domains):
    emails = []
    for user, d in domains.items():
      for u in d:
        emails.append(u+ "@" + user)
    return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))



'''
2.
The groups_per_user function receives a dictionary, which contains group names with the list of users. Users can belong to
multiple groups. Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values.
'''
def groups_per_user(group_dictionary):
    user_groups = {}
    for group,users in group_dictionary.items():
        for user in users:
          user_groups.setdefault(user, []).append(group)
    return(user_groups)
print(groups_per_user({"local": ["admin", "userA"],
        "public":  ["admin", "userB"],
        "administrator": ["admin"] }))
























