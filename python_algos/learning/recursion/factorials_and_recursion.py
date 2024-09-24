
# * Factorials

# * Review:
# The FACTORIAL of the number 5 is 120.

# ? HOW 
# 5 x 4 x 3 x 2 x 1 = 120
# factorials take all numbers all the way down
# to number 1. it also takes positives only.

# * below is a function that will do just that.

def iterative_factorial(n):
    fact = 1
    # remember in range - 
    # the first arg is that start
    # the second is the end
    # the third is the count by; if none we count by 1

    # in this case, because we are doing factorials, we
    # start at 2 because if we start at one its unnecessary
    # bc 1x1 would be one and time 2 by that one would be 2 
    # when we could just start at 2

    # we have it as plus 1 because, when using range,
    # it foes u
    for i in range(2, n + 1):
        fact *= i
        print(fact)
    # when the cycling is finished, we simply return the fact object
    return fact

# output:
print(iterative_factorial(5))
# for loop output:
# 2
# 6
# 24
# 120

# return output:
# 120

# * Recursion 
# * the idea in which a function calls itself over and over
# applying the above using recursion.

print(" ")

def recur_factorial(n):
    # we do this because if n = 1, we dont need
    # to do a ton of math. simply, return n if n 
    # is 1 in the case of factorials
    if n == 1:
        return n
    else:
        # ? what goes on here?
        # it creates a pocketed space where it will
        # continuously call recur_factorial function 
        # until n does equal 1.
        temp = recur_factorial(n-1)
        print(f"temp before: {temp}")
        temp = temp * n
        print(f"temp after: {temp}")
    return temp
print(recur_factorial(5))
# looping output:
# temp before: 1
# temp after: 2
# temp before: 2
# temp after: 6
# temp before: 6
# temp after: 24
# temp before: 24
# temp after: 120

# reutnr output:         
# 120   

# * this overall works because all the others that are still waiting to 
# finish can finally finish. 

# ? what is happening ?
# in other words, the loop continues until n = 1. 
# once n finally equals 1, it goes back up to complete 
# all instances it didnt complete to get n to equal to 1.
# 2 can finish, and then 3, and then 4, and then 5