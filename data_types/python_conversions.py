
# ** Python Conversions

# * int(): Converts a value to an integer.
x = int("10")  
# x = 10
y = int(3.14) 
# y = 3

# * float(): Converts a value to a floating-point number.
x = float("3.14")  
# x = 3.14
y = float(10)     
# y = 10.0

# * str(): Converts a value to a string.
x = str(10)     
# x = "10"
y = str(3.14)   
# y = "3.14"

# * bool(): Converts a value to a boolean.
x = bool(1)      
# x = True
y = bool(0)      
# y = False
z = bool("False")
# z = True (any non-empty string is True)

# ** Conversions for Collections

# * list(): Converts an iterable (like a tuple, set, or string) to a list.

x = list("hello")  
# x = ['h', 'e', 'l', 'l', 'o']

# * tuple(): Converts an iterable to a tuple.
x = tuple([1, 2, 3])  
# x = (1, 2, 3)

# * set(): Converts an iterable to a set.
x = set([1, 2, 2, 3])  
# x = {1, 2, 3}

# * dict(): Converts a sequence of key-value pairs to a dictionary.
x = dict([('a', 1), ('b', 2)])  
# x = {'a': 1, 'b': 2}