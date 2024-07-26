
# * Tuples
# Tuples in Python are very similar to Python lists.
# Tuples have a class (type) of tuple.

# You may come across tuple’s being “classified” based on 
# how many items they contain, e.g., a 2-tuple would contain 
# two items such as (some_key, some_value).

# * Basic Syntax
# * Tuples can be defined in a few different ways. Most basically, they are defined like this:
colors = ('red', 'green', 'blue')
print(colors)
# > ('red', 'green', 'blue')
print( len(colors) )
# > 3
# * The parentheses are actually optional. The following would work as well:
colors = 'red', 'green', 'blue'
# However, using parenthesis seems to be the convention.

# * If you need to create a 1-tuple (a tuple with one item), 
# be aware that a comma is necessary:

# * Will not create a tuple
hello_tuple = ('Hello')
print( type(hello_tuple) )
# >  <class 'str'>

hello_tuple = ('Hello',)
# or just the following (no parens required)
hello_tuple = 'Hello',
print( type(hello_tuple) )
# > <class 'tuple'>


# * Differences Between Tuples & Lists
# The main difference between tuples and lists is that tuples are immutable.
# Since tuples can’t be changed after they are created, 
# they are great for protecting data that you don’t want to be changed.

# Tuples internally are “lighter weight” than lists and Python iterates over 
# tuples faster than lists.
# Because they are immutable, tuples can even be used as keys for dictionaries.

# Generally, you’ll find that tuples are used to contain heterogeneous (different) 
# data types and lists for homogeneous (similar) data types.