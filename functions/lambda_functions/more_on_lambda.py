
# ? Why use Lambda functions?
# The power of lambda is better shown when 
# you use them as an anonymous function inside 
# another function.

# Say you have a function definition that takes 
# one argument, and that argument will be multiplied 
# with an unknown number:

def myfunction(n):
    return lambda a : a * n

# Use that function definition to make a 
# function that always doubles the number 
# you send in:

doubler = myfunction(2)
# * in the above, we are setting n equal to 2
print(doubler(5))
# * in the above, we are setting a equal to 5
# output:
# 10


# Or, use the same function definition to make a 
# function that always triples the number you 
# send in:

mytripler = myfunction(3)
print(mytripler(11))
# output:
# 33

# Or, use the same function definition to make both 
# functions, in the same program:

mydoubler = myfunction(2)
mytripler = myfunction(3)

print(mydoubler(11))
print(mytripler(11))

# * simply put:
# Due to the way closures work, when we first call
# my function, lambda memorizes what has been passed in. 
# from there, it returns the lambda function as a whole
# and stores it in the variable mydoubler and that is why
# you can call mydoubler like a function and passing in an arg.