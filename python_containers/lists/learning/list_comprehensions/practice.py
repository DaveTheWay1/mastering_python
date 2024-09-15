nums = [1,2,3,4,5,6,7,8,9]
numbers = [num ** 5 for num in nums]
print(numbers)

grater_than_4 = [num * 4 for num in nums if num > 4]
print(grater_than_4)

gisselle = [char for char in "gisselle" if char == "s"]
print(gisselle)

print("my test")
[print(num * 3) for num in range(10) if num % 2 == 0]
# 0
# 6
# 12
# 18
# 24

print(" ")

[ print(nums[num]) for num in range(len(nums)) if nums[num] != 6]
# output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# ? whats going on?
# in short, how this works is we put a for and  if check and instead of having  
# what we want to happen to those conditionals that turn out true in the front
# ! however, it has to be a imple conditional statement. otherwise they don't really work.

[ print(nums[num]) for num in range(len(nums)) if nums[num] != 6 or nums[num] != 3]
# output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9