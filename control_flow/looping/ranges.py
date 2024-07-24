
# * Python Ranges

# * Purpose of Ranges:
# Python ranges are a sequence type like lists and tuples.

# The range type represents an immutable sequence of integers 
# and is commonly used for looping a specific number of times in for loops.

# * Ranges have a class (type) of range.

# * Ranges - Basic Syntax
# Ranges can only be created by invoking the range() class:

for num in range(5):
  print(num)
# > 0
# > 1
# > 2
# > 3
# > 4
# * Notice that by default, the sequence starts at 0 and goes up to, but does not including the integer passed in.


# * Ranges can also generate sequences with a start and a step:
for even in range(2, 10, 2):
  print(even)
# > 2
# > 4
# > 6
# > 8
# When not passed in, the start value defaults to 0 and the step defaults to 1.

# * Ranges can also be used to create lists and tuples:

nums = list(range(10))
print(nums)
# > [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
odds = tuple(range(1, 10, 2))
print(odds)
# > (1, 3, 5, 7, 9)

# * Ranges - Negative Step
# If the step is a negative integer, the sequence counts down:
for num in range(5, 0, -1):
  print(num)
# > 5
# > 4
# > 3
# > 2
# > 1