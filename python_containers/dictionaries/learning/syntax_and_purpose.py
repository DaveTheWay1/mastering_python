
# * Dictionaries

# * Purpose:
# Dictionaries are to Python as objects are to JS.
# A dictionary provides a container for key: value pairs.

# * In Python, we commonly refer to key: value pairs as items vs. properties as in JS.
# * Dictionaries have a class (type) of dict.

# * BASIC SYNTAX
# A dictionary is created literally using curly braces:

student = {
  'name': 'Maria',
  'course': 'SEI',
  'current_week': 7
} 

# ! Dictionaries are mutable:

# * The values assigned to a key can be changed
# * Additional items can be added
# * Existing items can be deleted


# * Any immutable type can be used as a key, including 
# numbers and tuples (which we’ll cover in a bit), for example:

option = 3

d = {
  option: 'three'
}

# The above dictionary, d, has 1 item with a key of 3 that holds the value of 'three'. 
# Note that the value of the option variable is “copied” as the key - thus no “link” 
# to the option variable is created.

# 👀 Only since version 3.6 does Python track the insertion order of items in a 
# dictionary - so beware if you’re relying on the order items are iterated upon.