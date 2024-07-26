
# * Accessing Items
# Although tuples can’t be modified like lists, 
# we retrieve their items in the same way using square brackets:
colors = ('red', 'green', 'blue')
green = colors[1]
print(green)
# > green

# * Sequences (lists, tuples & strings) also have an index() 
# method that returns the index of the first match:

colors = ('red', 'green', 'blue')
blue_idx = colors.index('blue')
print(blue_idx)
# > 2