'''
# ? Exercise 1
- Write a function named sum_to with a parameter named n and returns the sum of the integers from 1 to n.

    For example:
	sum_to(6)  # returns 21
	sum_to(10) # returns 55
'''
# Your solution to Exercise 1 here:

# * regular function
def sum_to(n):
    return 1 + n
print(sum_to(3))

# * lambda function
sum_to = lambda n: 1+n
print(sum_to(1))

'''
Exercise 2
- Write a function named largest that takes a list of numbers as an argument
    and returns the largest number in that list.

    For example:
    largest([1, 2, 3, 4, 0])  # returns 4
    largest([10, -4, 2, 231, 91, 54])  # returns 231
'''
# Your solution to Exercise 2 here:

def largest(*args):
    L = 0
    for arg in args:
        if arg > L:
            L = arg
            print(L)
    return L
print(largest(3,2,4,1,2,6,2,3,4))

'''
Exercise 3
- Write a function named occurrences that takes two string arguments as input
    and counts the number of occurrences of the second string inside of the first string.

For example:
    occurrences('fleep floop', 'e')   # returns 2
    occurrences('fleep floop', 'p')   # returns 2
    occurrences('fleep floop', 'ee')  # returns 1
    occurrences('fleep floop', 'fe')  # returns 0
'''
# Your solution to Exercise 3 here:



'''
Exercise 4
- Write a function named product that takes an arbitrary number of individual number args (not a list),
    multiplies them all together, and returns the product.
    (HINT: Review your notes on *args).

For example:
    product(-1, 4) # returns -4
    product(2, 5, 5) # returns 50
    product(4, 0.5, 5, 1) # returns 10.0
'''
# Your solution to Exercise 4 here: