
# * Python’s ** Parameter Specifier (**kwargs)
# First, the reason we name the parameter kwargs 
# is because it stands for keyword arguments.

# * A keyword argument is an argument with a name, and this is why 
# keyword arguments are also referred to as # * named arguments.
# * For example, assume the following function:
def divide(a, b):
  return f'{a} divided by {b} is {a / b}'
# Not that it’s recommended, but knowing how the 
# function is defined above, we could invoke the 
# function using keyword arguments where the 
# order of the arguments doesn’t matter:

print(divide(b=25, a=100)) # returns '100 divided by 25 is 4.0'

#  ! However, the above example is not how 
# keyword arguments are commonly used…

# * First, we use the ** specifier when 
# defining a parameter named **kwargs (named by convention).
# * By adding **kwargs at the end of the parameter 
# list, we can access any number of keyword arguments.
# * For example:
def dev_skills(dev_name, **kwargs):
#   kwargs will be a dictionary!
    dev = {'name': dev_name, 'skills': kwargs}
    return dev
print(dev_skills('Jackie', HTML=5, CSS=3, JavaScript=4, Python=2))
# {'name': 'Jackie', 'skills': {'HTML': 5, 'CSS': 3, 'JavaScript': 4, 'Python': 2}}
