
# * Adding an Item
# The equivalent to JS’s push() method is # * append():
colors = ["red", "white", "blue"]
colors.append('purple')
# ! However, unlike JS’s push() method, append() can only add one item 
# and does not return a value.

colors.extend(['orange', 'black'])
# or the += operator:

colors += ['orange', 'black']
# The + operator can be used to create a new list by combining others:

odds = [1, 3, 5]
evens = [2, 4, 6]
nums = odds + evens
print(nums)
# > [1, 3, 5, 2, 4, 6]

# * Inserting an Item
# To add an item anywhere within a list, use the insert() method:
print(colors)
# > ['red', 'green', 'brown', 'purple', 'orange', 'black']
colors.insert(1, 'yellow')
# > ['red', 'yellow', 'green', 'brown', 'purple', 'orange', 'black']