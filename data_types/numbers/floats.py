
# * Floating-point Numbers (<class 'float'>)
#  Numbers with a decimal point are stored in variables as floating-point numbers, usually just called a float.

# Certain built-in features need to be imported
import math
pi = math.pi
# pi
# 3.141592653589793
print(type(pi))
# <class 'float'>
some_float = 25.
print(type(some_float))
# <class 'float'>

result = int(pi)
print(result)

float = 3.9
round = int(float)
print(f"float: {float}")
print(f"round: {round}")

# * in summary, when converting a float to an int
# * it will always round down.