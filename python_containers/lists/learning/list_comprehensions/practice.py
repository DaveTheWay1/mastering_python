nums = [1,2,3,4,5,6,7,8,9]
numbers = [num ** 5 for num in nums]
print(numbers)


grater_than_4 = [num * 4 for num in nums if num > 4]
print(grater_than_4)

gisselle = [char for char in "gisselle" if char == "s"]
print(gisselle)