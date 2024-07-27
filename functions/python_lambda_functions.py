
# * Python has lambda functions instead of arrow functions
# Python lambda functions are very much like Arrow Functions in JavaScript:
# They implicitly return a single expression’s value.
# They are expressions so they are commonly used as “inline” arguments.
# They can be assigned to a variable.

# * However, unlike arrow functions, they cannot have any code block 
#   - just a single expression that has its result implicitly returned.

# For example:

# * JavaScript
# const nums = [1, 3, 2, 6, 5];
# let odds = nums.filter(num => num % 2);

# * Python
nums = [1, 3, 2, 6, 5]
odds = list( filter(lambda num: num % 2, nums) )
print(odds)

# Lambda functions are nifty when using Python functions 
# such as map() and filter() - just like how arrow functions are nifty 
# when using array iterator methods.

