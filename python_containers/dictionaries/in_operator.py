
# * The in Operator

# * Another way to avoid the KeyError is to use the in operator to 
# check if the dictionary includes a certain key:
student = {
  'name':'David'
}

if 'course' in student:
  print( f"{student['name']} is enrolled in {student['course']}")
else:
  print( f"{student['name']} is not enrolled in a course")
# The in operator always returns a boolean (True or False).

