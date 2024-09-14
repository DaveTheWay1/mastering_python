
# * setdefault()

users = {
    0:'Mario',
    1:'Luigi',
    2:'James'
}
print(users.setdefault(0,'???'))
print(users.setdefault(3,'!!!'))
# output
# Mario
# . !!!

# * if it does it exist it will return the value of what already exists
# if it doesnt exist it will return what we created as the  default

# ! HOWEVER
# the difference between get and setdefault is that # * IT WILL apply to our dictionary
print(users)
# output:
# {0: 'Mario', 1: 'Luigi', 2: 'James', 3: '!!!'}