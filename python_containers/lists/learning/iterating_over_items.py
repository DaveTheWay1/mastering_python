
# * The for...in loop is used to iterate over the items in a list:
colors = ['red', 'green', 'blue']
for color in colors:
  print(color)
# > red
# > green
# > blue

# * If we need to access the index of the item while iterating over a list, 
# we use the # * built-in enumerate() function to provide the index 
# and the value to a for...in loop:

for idx, color in enumerate(colors):
  print(idx, color)
# > 0 red
# > 1 green
# > 2 blue