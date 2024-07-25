
# * Removing an Item
# Yup, there’s a pop() method, but it’s more flexible 
# in Python because you can specify the index of the item to remove and return:
colors = ['red', 'yellow', 'green', 'brown', 'purple', 'orange', 'black']
print(colors)
# > ['red', 'yellow', 'green', 'brown', 'purple', 'orange', 'black']
green = colors.pop(2)
print(colors)
# > ['red', 'yellow', 'brown', 'purple', 'orange', 'black']


# * If you don’t care about the value returned by pop(), 
# you can also use the del operator to delete an item:
print(colors)
# > ['red', 'yellow', 'brown', 'purple', 'orange', 'black']
del colors[1]
print(colors)
# > ['red', 'brown', 'purple', 'orange', 'black']

# * Also there’s a remove() method that removes the first item 
# that matches what you pass in:

print(colors)
# > ['red', 'brown', 'purple', 'orange', 'black']
colors.remove('orange')
print(colors)
# > ['red', 'brown', 'purple', 'black']
# ! No value is returned by the remove() method.

# * !! Clearing an Entire List
# The clear() method does just what you’d think:
print(colors)
# > ['red', 'brown', 'purple', 'black']
colors.clear()
print(colors)
# > []