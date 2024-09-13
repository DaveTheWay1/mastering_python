
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

# ? print(student.name), why doesnt this work?
# * because it does not evaluate to a key.
# you would get the error: AttributeError: 'dict' object has no attribute 'name'

# * to further explain: an attribute are variables, methods, and etc. NOT keys of a dictionary.
# so what we dont use square brackets, it assumes to look for an attribute and not a dictionary key.
