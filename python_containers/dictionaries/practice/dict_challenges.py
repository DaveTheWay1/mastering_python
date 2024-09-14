
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

dict1.update(dict2)
print(dict1)

# output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

Home » Python Exercises » Python Dictionary Exercise with Solutions
Python Dictionary Exercise with Solutions
Updated on: May 6, 2023 | 56 Comments

This Python dictionary exercise aims to help Python developers to learn and practice dictionary operations. All questions are tested on Python 3.

Python dictionary is a mutable object, and it contains the data in the form of key-value pairs. Each key is separated from its value by a colon (:).

Dictionary is the most widely used data structure, and it is necessary to understand its methods and operations.

Also Read:

Python Dictionary
Python Dictionary Quiz

This Python dictionary exercise includes the following: –

It contains 10 dictionary questions and solutions provided for each question.
Practice different dictionary assignments, programs, and challenges.
It covers questions on the following topics:

Dictionary operations and manipulations
Dictionary functions
Dictionary comprehension
When you complete each question, you get more familiar with the Python dictionary. Let us know if you have any alternative solutions. It will help other developers.

Use Online Code Editor to solve exercise questions.
Read the complete guide to Python dictionaries to solve this exercise

Table of contents
Exercise 1: Convert two lists into a dictionary
Exercise 2: Merge two Python dictionaries into one
Exercise 3: Print the value of key ‘history’ from the below dict
Exercise 4: Initialize dictionary with default values
Exercise 5: Create a dictionary by extracting the keys from a given dictionary
Exercise 6: Delete a list of keys from a dictionary
Exercise 7: Check if a value exists in a dictionary
Exercise 8: Rename key of a dictionary
Exercise 9: Get the key of a minimum value from the following dictionary
Exercise 10: Change value of a key in a nested dictionary

Exercise 1: Convert two lists into a dictionary
Below are the two lists. Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
Expected output:

{'Ten': 10, 'Twenty': 20, 'Thirty': 30}
Show Hint
Show Solution
Solution 1: The zip() function and a dict() constructor

Use the zip(keys, values) to aggregate two lists.
Wrap the result of a zip() function into a dict() constructor.
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

res_dict = dict(zip(keys, values))
print(res_dict)
 Run
Solution 2: Using a loop and update() method of a dictionary

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# empty dictionary
res_dict = dict()

for i in range(len(keys)):
    res_dict.update({keys[i]: values[i]})
print(res_dict)
 Run
Exercise 2: Merge two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
Expected output:

{'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}