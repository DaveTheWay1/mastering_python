
# * Accessing Items
# Accessing the individual items of a list is much like accessing elements in a JS array, 
# i.e., by using square bracket notation with an expression that evaluates to an integer:

colors = ['red', 'blue', 'white']

idx = 1
colors[idx + 1]
# > white

# * However, unlike in JS, we can use negative integers to index from the end of a list:
colors[-1]
# > white
# No need to write code like colors[len(colors) - 1] - yay!

num_order = [1,2,3,4,55,6,7,8,9,99,887]
num88 = num_order[num_order.index(887)]
print(num88)

blue = colors[colors.index('blue')]
print(blue)