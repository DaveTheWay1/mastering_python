
# fromkeys()

people = ['Mario', 'Luigi', 'James']
users = dict.fromkeys(people)
print(users)

# output:
# {'Mario': None, 'Luigi': None, 'James': None}
# * using from keys like in the above sets all values as none

# ! HOWEVER,
# you can set a default
# ex:

users = dict.fromkeys(people, 'Unknown')
print(users)
# {'Mario': 'Unknown', 'Luigi': 'Unknown', 'James': 'Unknown'}