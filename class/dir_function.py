
# * Python provides a dir() 
# * function that can be used to list an object’s 
# * members (attributes and methods):

nums = [1,2,3]
print(dir(nums))
# output:
['__add__', '__class__', '__class_getitem__', 
'__contains__', '__delattr__', '__delitem__', 
'__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__getitem__', 
'__gt__', '__hash__', '__iadd__', '__imul__', 
'__init__', '__init_subclass__', '__iter__', 
'__le__', '__len__', '__lt__', '__mul__', '__ne__', 
'__new__', '__reduce__', '__reduce_ex__', '__repr__', 
'__reversed__', '__rmul__', '__setattr__', '__setitem__', 
'__sizeof__', '__str__', '__subclasshook__', 'append', 
'clear', 'copy', 'count', 'extend', 'index', 'insert', 
'pop', 'remove', 'reverse', 'sort']

# Some of the members like append & pop might look familiar.

# The other methods that start and end with double-underscores, 
# are called magic (or dunder) methods. They are internal 
# methods most commonly used to overload operators. 