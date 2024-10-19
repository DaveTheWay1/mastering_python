
# * Python, however, does not have a dedicated ternary operator.
# Instead, Python uses a modified syntax of if...else which results in a ternary expression 
# instead of a control flow construct.
# The Python ternary expression equivalent to the JS example above is:

# JAVASCRIPT 
# Using the ternary operator/expression
# let beverage = age >= 21 ? 'Beer' : 'Milk';

# PYTHON
age = 24
beverage = 'Beer' if age >= 21 else 'Milk'

print("Do you have a bottle opener? Please answer with a yes or no response.")
do_you = input()
response = 'Beer me' if do_you.lower() == 'yes' else 'Mmm, come onnn maneee'
print(response)


# ? can a ternary operator in python have an if else? 
# ! a ternary operator in Python cannot directly contain another 
# if-else statement within it.
# * Why? The purpose of a ternary operator:
# The ternary operator is meant to be a concise way to express a 
# simple conditional expression in a single line.

# ! if an if else is needed, use a regular if statement and not a ternary