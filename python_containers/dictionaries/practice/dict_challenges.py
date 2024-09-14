
# * Exercise 1: Convert two lists into a dictionary
# Below are the two lists. Write a Python program to 
# convert them into a dictionary in a way that item from 
# list1 is the key and item from list2 is the value

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

list_to_dict = {

}
# ? how can we loop through 2 lists at once?
# * through using zip like in the below
for k,v in zip(keys,values):
    list_to_dict[k] = v
print(list_to_dict)