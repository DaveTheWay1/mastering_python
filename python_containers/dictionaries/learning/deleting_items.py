student = {
  'name':'David'
}
student['age'] = 21

# * Deleting Items
# The del statement is used to delete an item from a dictionary:

del student['age']
# Verify that item was deleted
print('age' in student)
# > False


# ! 👀 A del statement does not return a value

student['security'] = True
print(student)

del student['security']
print(student)