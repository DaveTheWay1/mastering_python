# Exercises


# Exercise 1
# Create a list named students containing some student names (strings).
# Print out the second student’s name.
# Print out the last student’s name.

student = ["David", "Gisselle", "Cazador", "Mow Mow", "Nova"]
print(f"Second Student: {student[1]}")


# Exercise 2
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Use a for loop to print out the string “[food goes here] is a good food”.

foods = "Pizza", "Pho", "Peanut Butter", "Churus", "Wet Food"
print(type(foods))

num = 0
for food in foods: 
    print(f"{student[num]} says {food} is a good food")
    num += 1


# Exercise 3
# Using a for loop, print just the last two food strings from foods.

num_of_foods = len(foods)
last_two_foods = num_of_foods - 2
for food in foods[last_two_foods:]:
    print(food)

# Exercise 4
# Create a dictionary named home_town containing the keys of city, state and population.
# Print a string with this format:
# “I was born in city, state - population of population”

home_town = {
    'city': 'union city',
    'state': 'CA',
    'population': 13000
}

print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")


# Exercise 5
# Iterate over the key: value pairs in home_town and print a string for each item, for example:
# “city = Arcadia”
# “state = California”
# “population = 58000”

for key,val in home_town.items():
    print(f"{key} = {val}")


# Exercise 6
# Create an empty list named cohort.
# Using a for loop to iterate over the students list.
# Hint: Use the enumerate function to provide both the index & student

# Within the for loop, add a dictionary to the cohort list that combines the student’s name 
# and the food in the foods list at the same index. Each dictionary will have this shape:
#   {
#     'student': 'Tina',
#     'fav_food': 'Cheeseburger'
#   }
# Iterate over the cohort list, printing out each item (it’s not necessary to format the dictionaries).

cohort = []

for idx, student in enumerate(student):
    cohort.append({'student': student, 'fav_food': foods[idx]})

print(cohort)

# Exercise 7
# Using the list of students and a list comprehension, assign to a variable named awesome_students a new list containing strings similar to this:
# ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
# Iterate over the awesome_students list, printing out each string.

awesome_students = [f"{student} is awesome!" for student in student]
print(awesome_students)

# Exercise 8
# Use a for loop to iterate over a list comprehension that filters the foods tuple to only include food strings that contains the letter a.
# Within the for loop, print each food string.

foods_containing_a = [food for food in foods if "a" in food]
print(foods_containing_a)
foods_containing_a = [food for food in foods if food.find("a") != -1]
# in the above, when find is used, it returns an index if succesful. if not, it returns and -1.
# it is part of how find works. usually, returning 0 would be false and -1 would be true but n
# ot the case here due to how find is built to work.
print(foods_containing_a)