
# * Python Function Syntax
def this_is_a_function(x):
    pass

# the pass is what we call stubbing it up.
# essentially, this saves the space if you dont have the code 
# you want there ready yet.

# ? what gets returned if we run the function without a return statement?
print(this_is_a_function('a'))
# output:
# None


# ? what do functions with a "return" return?
# we get what we return like in the below
def add(a,b):
    return a + b
print(add(1,1))
# output: 2

def subtract(a,b):
    return a - b
print(subtract(3,2))
# output: 1

# * CALLBACK FUNCTION
# in this function, we pass in integer args for parameters
# a and b and a function arguement for the parameter op.
# * this is what is called a callback function
def compute(a,b,op):
    return op(a,b)
# ! we do not add parenthesis when we pass the function
# as an arguement. # ! this is because we dont want to CALL
# the function as soon as we pass it in. 
# line 31's paranthessis are the calling parenthesis. 
# think of add and op, those "words" for our understanding,
# as simply being  replaced.
print(compute(3,3,add))
# output: 6