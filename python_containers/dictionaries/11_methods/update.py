
# * update()

users = {
    0:'Mario',
    1:'Luigi',
    2:'James'
}

users.update({2:'Bob', 3:'James\'s sister'})

print(users)
# output:
# {0: 'Mario', 1: 'Luigi', 2: 'Bob', 3: "James's sister"}

# ! HOWEVER update is the old syntax

print(users | {10:'Spam', 11:'Eggs'})
# {0: 'Mario', 1: 'Luigi', 2: 'Bob', 3: "James's sister", 10: 'Spam', 11: 'Eggs'}

users |= {2:'David', 3:'Mow'}
print(users)
# output:
# {0: 'Mario', 1: 'Luigi', 2: 'David', 3: 'Mow'}