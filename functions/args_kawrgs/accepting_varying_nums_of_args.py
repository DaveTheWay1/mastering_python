
# * Accepting a varying number of arguments

# * Python’s * Parameter Specifier (*args)
# Using the * (“star”) specifier in a parameter list 
# allows us to pass in a varying number of positional arguments into a function:

def fn(*args):
  print( type(args) )
  for arg in args:
    print(arg)

# fn(1, 2, 'SEI')
''' Output:
<class 'tuple'>
1
2
SEI
'''

def test(*args):
  print(f'''
            name: {args[0]},
            age: {args[1]},
            occupation: {args[2]}
        ''')

name = input('name:')
age = int(input('age:'))
occupation = input('occupation:')

test(name, age, occupation)

# * Always use the *args parameter after any required positional parameters. For example:

def dev_skills(dev_name, *args):
  dev = {'name': dev_name, 'skills': []}
  # args will be a tuple
  for skill in args:
    dev['skills'].append(skill)
  return dev

print(dev_skills('Alex', 'HTML', 'CSS', 'JavaScript', 'Python'))
# -> {'name': 'Alex', 'skills': ['HTML', 'CSS', 'JavaScript', 'Python']}


# * Or, why not use the list() function to convert the args tuple into a list…

def dev_skills(dev_name, *args):
  dev = {'name': dev_name, 'skills': list(args)}
  return dev

print(dev_skills('Alex', 'HTML', 'CSS', 'JavaScript', 'Python'))