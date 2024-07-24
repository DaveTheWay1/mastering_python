
# * Comparison Operators

# * < 
#   less than
# * > 
#   greater than
# * <= 
#   less than or equal
# * >= 
#   greater than or equal
# * == 
#   equal to
# * != 
#   not equal to

# * Note that in Python, there’s only one equality operator. The == in Python is the same as === in JavaScript.

# * Examples:
8 > 8
# => False — 8 is not greater than 8.

8 >= 8
# => True — This checks if 8 is greater than or equal to 8, and they are equal.

8 < 8
# => False — 8 is not less than 8.

7 == 7
# => True — 7 is equal to 7.

7 == "7"
# => False — One is a number and the other is a string.

7 != 7
# => False — This checks if they aren't equal. Because does 7 equal 7, it's `False`.

6 != 7
# => True — 6 is not equal to 7.


# * Logical Operators
# in Python except Python uses English words instead of symbols:
# * or
# If the first operand is truthy, return it, otherwise return the second operand.
# * and
# If the first operand is falsy, return it, otherwise return the second operand.

# * Examples:
True or False
# => True

False or True
# => True

'hello' or 0
# => 'hello'

0 or 'hello'
# => 'hello'

True and False
# => False

False and True
# => False

'hello' and 0
# => 0

0 and 'hello'
# => 0

'hello' and 'tacos'
# => 'tacos'


# * not
# “Flips” the truthiness/falsyness of its operand, and returns True or False

not True
# => False

not 123
# => False

not []
# => True