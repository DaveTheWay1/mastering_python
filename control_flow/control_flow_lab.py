
# ? exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':

# letter = input('Please enter a letter from the alphabet (a-z or A_Z):')
# vowels = ["a","e","i","o","u"]

# # verifying a single letter was entered
# if len(letter) > 1:
#     # if not a single letter; have the prompt be entered again.
#     # letter = input('Please enter a letter from the alphabet (a-z or A_Z):')
#     while len(letter) > 1: 
#         letter = input('Please enter a letter from the alphabet (a-z or A_Z):')

# if letter.isalpha():
#     if letter in vowels:
#         print(f"{letter} is a vowel")
#     else:
#         print(f"{letter} is a consonant")
# else: 
#     print(f"{letter} is not a letter")

# ? exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

# response_container = ""
# while response_container != "quit":
#     response_container = input("Please enter a word or phase:").lower()
#     print(response_container)
#     find_space = response_container.find(" ")
#     if find_space != -1:
#         space_index = response_container.index(" ")
#         response_container = list(response_container)
#         response_container.pop(space_index)
#         response_container = "".join(response_container)
#     if response_container != "quit":
#         char_count = len(response_container)
#         print(char_count)







# ? exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age like this:
#      Input a dog's age: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hints:
# Use the int() function to convert the string returned from input() into an integer
# Start with an if that checks if the age is less than 3


# nums = ["0","1","2","3","4","5","6","7","8","9"]
# dog_age = input("Input a dog's age: ")
# r_dog_age = 0

# def dog_age_is_num(dog_age):
#     dog_age = list(dog_age)
#     for char in dog_age:
#         if char in nums:
#             continue
#         else:
#             return False
#     dog_age = "".join(dog_age)
#     return int(dog_age)

# if len(dog_age) >= 3:
#     while len(dog_age) >= 3:
#         dog_age = input("Please enter a valid dog's age: ")

# dog_age = dog_age_is_num(dog_age) 

# print(f"dog age in human years: {dog_age}")

# for age in range(1, dog_age+1):
#     if age == 1 or age == 2:
#         r_dog_age += 10
#     else: 
#         r_dog_age += 7
# dog_age = r_dog_age

# print(f"dog age in dog years: {dog_age}")

# ? exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equilateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - exactly two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

# print(("Enter the length of three side of a triangle: "))
# a = input("a:")
# b = input("b:")
# c = input("c:")

# if a == b and a == c:
#     print("equilateral - all three sides are equal in length")
# elif a != b and a != c and c != b:
#     print("scalene - all three sides are unequal in length")
# elif a == b or c == b or c == a:
#     print("isosceles - exactly two sides are the same length")




# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hints:
# The next number is found by adding the two numbers before it
# Use a while loop with a looping variable, or look into Python ranges, e.g.:
#   for n in range(50):


for n in range(50):
    if n < 2:
        print(f"term: {n} / number: {n}")
    elif(n == 2):
        number = n-1
        previos_number = 1
        print(f"term: {n} / number: {number}")
    else:
        previos_number = number
        
        print(f"term: {n} / number: {number}")








# exercise-06 What's the Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
#   if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.