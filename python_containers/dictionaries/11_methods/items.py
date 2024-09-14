
# * items()

users = {
    0:'Mario',
    1:'Luigi',
    2:'James'
}

print(users.items())
# returns an iterable
# dict_items([(0, 'Mario'), (1, 'Luigi'), (2, 'James')])

for k, v in users.items():
    print(k,v)