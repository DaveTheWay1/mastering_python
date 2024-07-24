
# * Integer Numbers (<class 'int'>)
#  Unlike in JavaScript, Python distinguishes between integers (whole numbers) and floats (numbers with decimals).
# When we don’t follow a number literal with a decimal point, an integer is assumed:
some_int = 25
type(some_int)
# <class 'int'>


# * In JavaScript, we could use Math.floor() to truncate the 
# decimal portion of a number. In Python, we can convert non-integer 
# numbers into integers using the int() function:

a_float = 1.7
an_int = int(a_float)
# >>> an_int
1