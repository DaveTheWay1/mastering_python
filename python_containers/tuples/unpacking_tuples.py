
# * Unpacking Tuples
# Tuples (and other sequences such as lists & strings) 
# have a convenient feature, called unpacking, 
# for performing multiple variable assignments in a single line of code:

colors = ('red', 'green', 'blue')
r, g, b = colors
print(r, g, b)
# > red green blue

# * Comma separated variables on the left-side of the assignment operator 
# and a sequence of values on the right is what it takes.

# FYI, we were seeing unpacking in action within the for in loops above, for example:
student = {
  'name':'david',
  'title':'security officer',
  'security':'clearence: secret'
}

for key, val in student.items():
  print( f"{key} = {val}" )