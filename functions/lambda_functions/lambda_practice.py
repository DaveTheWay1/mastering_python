
# * lambda functions are a one line annonymous function 
add_1 = lambda x: x + 1
result = add_1(1)
print(result)
# output: 2


add_2 = lambda x, y: x + y
result_2 = add_2(1,3)
print(result_2)
# output: 4

# * lambda function with map
my_numbers = [1,2,3,4,5,6,7,8,9,10]
squares = list(map(lambda x: x**2, my_numbers))
print(squares)
# in this case, without wrapping the map within the list function
# it will instead say: <map object at 0x1028e9d50>
# however, with the list wrapping, the output is:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# * lambda function with map
my_nums = [1,2,3,4,5,6,7,8,9,10]
sqrs = filter(lambda x: x%2 == 0, my_nums)
print(sqrs)
# all that is true gets put into a list
# output: [2, 4, 6, 8, 10]
# without the list wrapping you would get: <filter object at 0x10275e020>