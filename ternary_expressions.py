
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