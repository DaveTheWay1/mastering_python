# * The get() Method
# ❓ What happens when we access a property that does not exist in a JS object?
# undefined is returned

# One option to avoid this error is to use # * the get() method:

student = {
  'name':'David',
  'keyword':'123543'
}

# skills = student['skills']
# > KeyError: 'skills'
print( student.get('skills') )
# > None
# Provide a default value if key not in dictionary
print( student.get('skills', {'HTML': 5, 'JAVASCRIPT': 4}) )
# > {'HTML': 5, 'JAVASCRIPT': 4}


print( student.get('name'))

# * what the below does is get the value of keyword. if something is keyword already exist and it has a value,
# then it will return that value. if nothing is found then normally it would
# return us None. HOWEVER, bc we provided the dictionary after the key we are looking for(keyword), then
# we are setting that as the default if nothing is found instead.
print( student.get('keyword', {'passcode':374, 'keypad':1187}))