spaces = {
    'a1': None , 'b1': None, 'c1': None,
    'a2': None , 'b2': None, 'c2': None,
    'a3': None , 'b3': None, 'c3': None
    }

# * to see all arrtibutes and methods of a dictionary:
print(dir(spaces))
[
    '__class__', 
    '__class_getitem__', 
    '__contains__', 
    '__delattr__', 
    '__delitem__', 
    '__dir__', 
    '__doc__', 
    '__eq__', 
    '__format__', 
    '__ge__', 
    '__getattribute__',
    '__getitem__', 
    '__getstate__', 
    '__gt__', 
    '__hash__',
    '__init__', 
    '__init_subclass__', 
    '__ior__', 
    '__iter__',
    '__le__', 
    '__len__', 
    '__lt__', 
    '__ne__', 
    '__new__',
    '__or__', 
    '__reduce__', 
    '__reduce_ex__', 
    '__repr__', 
    '__reversed__', 
    '__ror__', 
    '__setattr__', 
    '__setitem__', 
    '__sizeof__', 
    '__str__', 
    '__subclasshook__', 
    'clear', 
    'copy', 
    'fromkeys', 
    'get', 
    'items', 
    'keys', 
    'pop', 
    'popitem', 
    'setdefault', 
    'update', 
    'values'
]

# * For an in depth description of all attributes and methods.. you can use the help() function:
# print(help(spaces)) # ! WARNING: using the help will cause you to have to terminate your terminal

print(all(space is not None for space in spaces.values()))
# the all is an efficient way to check the value of all spaces is one thing or another. it returns true or false. it will stop
# at the first one that presents a false.