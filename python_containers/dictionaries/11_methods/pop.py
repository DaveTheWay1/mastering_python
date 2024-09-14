
# * pop()
# allows us to remove a specified key by passing it in

users = {
    0:'Mario',
    1:'Luigi',
    2:'James'
}

users.pop(2)
print(users)
# output
# {0: 'Mario', 1: 'Luigi'}

# * you can even store the popped into a variable
popped_key = users.pop(1)
print(popped_key)
# output:
# Luigi

# ! if you pop something that does not exist you will get a key error