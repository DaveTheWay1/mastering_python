
# * popitem()
# a lot like pop except it only pops the last item

users = {
    0:'Mario',
    1:'Luigi',
    2:'James'
}

last_item = users.popitem()
print(users)
# output:
# {0: 'Mario', 1: 'Luigi'}

# * just like pop you can also store the popped item
print(last_item)
# (2, 'James')
