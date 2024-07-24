
# * Getting and Setting Values
# We always use square bracket notation to get and set an item’s value:
student = {
  'name':'David'
}
name = student['name']
print(name)
student['name'] = 'Tina'
print(student['name'])
student['age'] = 24
print(student['age'])
print(student)