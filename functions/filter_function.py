
# * filter function

nums = [1,2,3,4,5,6,7,8,9,10]

round_up = list(filter(lambda num: num >= 5, nums))
print(round_up)
round_down = list(filter(lambda num: num <= 4, nums))
print(round_down)
