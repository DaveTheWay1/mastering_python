
# * Slicing (Copying) Sequences
# Slicing in Python is used to create “slices” (copies) of sequences.

# * Python has a cool “slice” operator that uses this syntax:
# a_sequence[m:n]

# * Just like with indexing, slicing uses square brackets, but adds a colon:
short_name = 'Alexandria'[0:4]
print(short_name)
# > Alex
# ! Note that the slice includes up to, but not including the index to the right of the colon.

# * If the first index is omitted, a default starting index of 0 is used:
colors = ('red', 'green', 'blue')
print( colors[:2] )
# > ('red', 'green')

# * If the up to index is omitted, the slice copies the sequence all the way to the end:
colors = ['red', 'green', 'blue']
print( colors[1:] )
# > ['green', 'blue']

# * Assuming the following code:
fruit = ('apples', 'bananas', 'oranges')
fruits = fruit[:]
# ? ❓ What would the value of fruits be?
# ('apples', 'bananas', 'oranges')

# * Slice Assignment in Lists
# Amazingly, we can use the slice operator to insert and/or 
# remove items in a list 

# * For example, assume this list:
chars = ['a', 'b', 'x', 'y', 'd']
                  # 2,   3 .. this works bc it is the starting point(2) and end point(4) which goes up to but not included
# We could replace the 'x' and 'y' characters with 'c' like this:
chars = ['a', 'b', 'x', 'y', 'd']
chars[2:4] = 'c'
print(chars)
# > ['a', 'b', 'c', 'd']