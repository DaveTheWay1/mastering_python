
# * Assigning Items
# We also use square brackets to target an item of a list for assignment:
colors = ["red", "white", "blue"]
colors[-1] = 'brown'
print(colors)
# > ['red', 'white', 'brown']

# ! Unlike with JS arrays, assigning to a non-existing index results in an error:
colors[10] = 'yellow'
# > IndexError: list assignment index out of range