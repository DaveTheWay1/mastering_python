
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