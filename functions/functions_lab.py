'''
# ? Exercise 1
- Write a function named sum_to with a parameter named n and returns the sum of the integers from 1 to n.

    For example:
    sum_to(6)  # returns 21
    sum_to(10) # returns 55
'''
# Your solution to Exercise 1 here:

def sum_to(n):
    sum = 0
    for num in range(1, n+1):
        sum += num
    return sum

print(sum_to(6))

'''
# ? Exercise 2
- Write a function named largest that takes a list of numbers as an argument
    and returns the largest number in that list.

    For example:
    largest([1, 2, 3, 4, 0])  # returns 4
    largest([10, -4, 2, 231, 91, 54])  # returns 231
'''
# Your solution to Exercise 2 here:

def largest(nums):
    largest_num = 0
    for num in nums:
        if num > largest_num:
            largest_num = num
    return largest_num

print(largest([5,3,6,8,3]))
# 8
print(largest([1, 2, 3, 4, 0]))
# 4
print(largest([10, -4, 2, 231, 91, 54]))
# 231

'''
# ? Exercise 3
- Write a function named occurrences that takes two string arguments as input
    and counts the number of occurrences of the second string inside of the first string.

For example:
    occurrences('fleep floop', 'e')   # returns 2
    occurrences('fleep floop', 'p')   # returns 2
    occurrences('fleep floop', 'ee')  # returns 1
    occurrences('fleep floop', 'fe')  # returns 0
'''
# Your solution to Exercise 3 here:

# print("")
def occurrences(string_one, string_two):
    count = 0
    string_two_length = len(list(string_two))
    for i in range(0, len(list(string_one)), string_two_length ):
        string_one_sliced = string_one[i:(i+len(list(string_two)))]
        if string_two == string_one_sliced:
            count += 1
    return count
print(occurrences('hello', 'h'))


# '''
# Exercise 4
# - Write a function named product that takes an arbitrary number of individual number args (not a list),
#     multiplies them all together, and returns the product.
#     (HINT: Review your notes on *args).

# For example:
#     product(-1, 4) # returns -4
#     product(2, 5, 5) # returns 50
#     product(4, 0.5, 5, 1) # returns 10.0
# '''
# Your solution to Exercise 4 here:

def product(*args):
    result = 1
    for num in args:
        result *= num
    return result
print(product(-1,-4, 3, 8))