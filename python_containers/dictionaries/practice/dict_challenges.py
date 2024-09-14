
# * Exercise 1: Convert two lists into a dictionary
# Below are the two lists. Write a Python program to 
# convert them into a dictionary in a way that item from 
# list1 is the key and item from list2 is the value

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

list_to_dict = {

}

# our solution
# ? how can we loop through 2 lists at once?
# * through using zip like in the below
for k,v in zip(keys,values):
    list_to_dict[k] = v
print(list_to_dict)

# given solution:
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]


res_dict = dict(zip(keys, values))
print(res_dict)
# zip immediately takes two iterables like the above and turns them into tuples
# by applying dict like so - it behaves like a converter of the result turning them all into a dict

# another given solution:
# empty dictionary
res_dict = dict()

for i in range(len(keys)):
    res_dict.update({keys[i]: values[i]})
print(res_dict)

# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

# ? Exercise 2: Merge two Python dictionaries into one

dict1 = {'Ten':10, 'Twenty':20, 'Thirty':30}
dict2 = {'Thirty':30, 'Fourty':40, 'Fifty':50}

# printing here will return none:
dict1.update(dict2)

# however printing like so in the below will display your result
print(dict1)
# output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# ? Exercise 3: Print the value of key ‘history’ from the below dict

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print(sampleDict['class']['student']['marks']["history"])