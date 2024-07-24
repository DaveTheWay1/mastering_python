# * The get() Method
# ❓ What happens when we access a property that does not exist in a JS object?
# undefined is returned

# One option to avoid this error is to use # * the get() method:

student = {
  'name':'David'
}

skills = student['skills']
# > KeyError: 'skills'
print( student.get('skills') )
# > None
# Provide a default value if key not in dictionary
print( student.get('skills', {'HTML': 5, 'JAVASCRIPT': 4}) )
# > {'HTML': 5, 'JAVASCRIPT': 4}