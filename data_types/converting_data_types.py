
# * With few exceptions, variables must be the same type to perform an operation on them.
# Luckily, doing math operations between integers and floats is allowed, but not much else.
# When the time comes to convert one data type into another, Python provides us with 
# several global functions or predefined classes to do so:

str(item)        # Converts item to a string
int(item, base)  # Converts the provided item to an integer with the provided base
float(item)      # Converts the item to a floating-point number
hex(int)         # Converts an integer to a hexadecimal STRING
oct(int)         # Converts an integer to an octal STRING
tuple(item)      # Converts item to a tuple
list(item)       # Converts item to a list
dict(item)       # Converts item to a dictionary