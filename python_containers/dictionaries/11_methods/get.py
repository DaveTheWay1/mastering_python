
# * get()

users = {
    0:'Mario',
    1:'Luigi',
    2:'James'
}

print(users.get(1))
# if it does exist
# output:Luigi

print(users.get(999))
# if it does not exist
# output:None

print(users.get(999, {000:'bravedave1'}))
# however, if it does not exist but we set a default
# {0: 'bravedave1'}
# !anything couldve been inserted. included the string 'Missing!' if you 
# wanted to declare that it is not found

print(users)
# yet, it does not add it
# output:
# {0: 'Mario', 1: 'Luigi', 2: 'James'}