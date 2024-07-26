def space():
  print(" ")

# ? Exercise 1
# Create a list named students containing some student names (strings).
# Print out the second student’s name.
# Print out the last student’s name.
students = ['david', 'gisselle', 'cazador', 'mow', 'nova']
space()
print(f"second student: {students[1]}, last student: {students[-1]}")
# second student: gisselle, last student: nova


# ? Exercise 2
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Use a for loop to print out the string “[food goes here] is a good food”.
foods = ('burritos', 'pasta', 'human food','wet food', 'dry food')
space()
for food in foods:
  print(f"{food} is a good food")

# burritos is a good food
# pasta is a good food
# human food is a good food
# wet food is a good food
# dry food is a good food


# ? Exercise 3
# Using a for loop, print just the last two food strings from foods.
# Hint: Use the slice operator to select the last two foods
space()
print(foods[-2:])
# ('wet food', 'dry food')

# ? Exercise 4
# Create a dictionary named home_town containing the keys of city, state and population.
# Print a string with this format:
# “I was born in city, state - population of population”

born = {'state':'California','west bay': 'Palo Alto/Redwood City'}
raised = {'state':'Calfornia', 'east bay': 'Union City'}
current = {'state': 'California', 'east bay':'Fremont'}

home_town = {
  'born':born,
  'raised':raised,
  'current':current
}

def sentence(key, items):
  space()
  state, bay = items
  print(f"I was {key} in the {state[0]} of {state[1]}, in the {bay[0]} of the bay area, in the {bay[1]} area.")
  print(f"{key} = {state[1]}, {bay[1]}")
  space()


for key, val in home_town.items():
    sentence(key, val.items())

# ? Exercise 5
# Iterate over the key: value pairs in home_town and print a string for each item, for example:
# “city = Arcadia”
# “state = California”
# “population = 58000”

# * line 55

# I was born in the state of California, in the west bay of the bay area, in the Palo Alto/Redwood City area.
# born = California, Palo Alto/Redwood City

# I was raised in the state of Calfornia, in the east bay of the bay area, in the Union City area.
# raised = Calfornia, Union City

# I was current in the state of California, in the east bay of the bay area, in the Fremont area.
# current = California, Fremont

# ? Exercise 6
# Create an empty list named cohort.
# Using a for loop to iterate over the students list.
# Hint: Use the enumerate function to provide both the index & student
# Within the for loop, add a dictionary to the cohort list that combines 
# the student’s name and the food in the foods list at the same index. 
# Each dictionary will have this shape:
#   {
#     'student': 'Tina',
#     'fav_food': 'Cheeseburger'
#   }
# Iterate over the cohort list, printing out each item (it’s not necessary to format the dictionaries).

# cohort = ['cazador', 'mow', 'nova', 'tuki', 'luna', 'sol']
cohort = []

students = ['david', 'gisselle', 'cazador', 'mow', 'nova']
foods = ('burritos', 'pasta', 'human food','wet food', 'dry food')
for idx, precious in enumerate(students):
  cohort.append({'student':precious, 'fav_food':foods[idx]})

print(cohort)
# [{'student': 'david', 'fav_food': 'burritos'}, {'student': 'gisselle', 'fav_food': 'pasta'}, {'student': 'cazador', 'fav_food': 'human food'}, {'student': 'mow', 'fav_food': 'wet food'}, {'student': 'nova', 'fav_food': 'dry food'}]

for student in cohort:
  name, food = student.items()
  print(f"{name[1]} - {food[1]}")
# david - burritos
# gisselle - pasta
# cazador - human food
# mow - wet food
# nova - dry food


# ? Exercise 7
# Using the list of students and a list comprehension, assign to a variable named awesome_students a new list containing strings similar to this:
# ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
# Iterate over the awesome_students list, printing out each string.

awesome_students = [f"{name} is awesome!" for name in students]
print(awesome_students)
# ['david is awesome!', 'gisselle is awesome!', 'cazador is awesome!', 'mow is awesome!', 'nova is awesome!']


# ? Exercise 8
# Use a for loop to iterate over a list comprehension that filters the foods tuple to only include food strings that contains the letter a.
# Within the for loop, print each food string.

I_have_an_a_in_my_food = [food for food in foods if 'a' in food]
print(I_have_an_a_in_my_food)
# ['pasta', 'human food']