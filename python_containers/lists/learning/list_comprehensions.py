
# * Purpose
# List comprehensions are a powerful feature in Python.
# They provide a concise way to create and work with lists.
# They will seem confusing as first, but they certainly are a favorite of Pythonistas 
# and you will probably come across them when googling.


# * Numerical Example
# Say we needed to square all of the numbers in a list and put 
# them into a new list, we might use a for loop like this:
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# I want 'n * n' for each 'n' in nums 
squares = []
for n in nums:
  squares.append(n * n)
print(squares)
# > [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# * A list comprehension can reduce this code:
squares = []
for n in nums:
  squares.append(n * n)
# To this:
squares = [n * n for n in nums]

# 👀 Again, a list comprehension always returns a new list.

# * Basic Syntax
# Here’s the basic syntax of a list comprehension:
# * [<expression> for <item> in <list>]
# This reads as: I want <expression> for each <item> in <list>
# As you can see, a list comprehension is basically a modified 
# for...in loop within square brackets that returns a new list.

# * Filtering the Items
# We just saw how list comprehensions are a nice way to map a list, 
# but they can be used for filtering too.

# * Again, let’s start with a non-comprehension approach by 
# using a for...in loop to map and filter nums:
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# I want 'n * n' for each 'n' in nums  if 'n * n' is even
even_squares = []
for n in nums:
  square = n * n 
  if square % 2 == 0:
    even_squares.append(square)
print(even_squares)
# > [4, 16, 36, 64, 100]

# * Again list comprehensions reduce the above from:
even_squares = []
for n in nums:
  square = n * n 
  if square % 2 == 0:
    even_squares.append(square)

# * To this one-liner:
even_squares = [n * n for n in nums if (n * n) % 2 == 0]
# Talk about less is more!