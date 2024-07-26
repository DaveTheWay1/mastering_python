
# * Dictionaries - Iterating Items
# for...in loops are used to iterate over the items in a dictionary.


# * THE ANTI PATTERN WAY: However, accessing the value of an item as follows is considered to be 
# a Python anti-pattern:

# student = {'name': 'Tina', 'course': 'SEI'}

# for key in student:
#   print( f"{key} = {student[key]}" )

# * THE PREFERRED WAY: The preferred approach is to use the items() method to obtain 
# a dictionary view object.

student = {'name': 'Tina', 'course': 'SEI'}
print(student.items()) 

# returns a wrapped list of (key, value) tuples:

student.items()
# > dict_items([('name', 'Tina'), ('course', 'SEI')])
# Now we can use a for...in loop to iterate over the view object:

for key, val in student.items():
  print( f"{key} = {val}" )\
# name = Tina
# course = SEI

# The for statement “unpacks” the tuples by assigning 
# its values to multiple variables like with key, val above.

stats = {
  'name':'david ramirez-vazquez',
  'age': 24,
  'occupation':'security officer',
  'security_clearence':True,
  'clearence_level':'secret',
  'adobe_digital_academy_scholar':True
}

print(stats)

for key,value in stats.items():
  if key == 'security_clearence' and value == True:
    print(f"{key}: {value} - clearnece level: {stats['clearence_level']}")
  elif(key == 'clearence_level'):
    continue
  else:
    print(f"{key}: {value}")