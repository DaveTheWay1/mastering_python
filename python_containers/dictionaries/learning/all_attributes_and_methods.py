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

# Help on dict object:

# class dict(object)
# dict() -> new empty dictionary
#  |  dict(mapping) -> new dictionary initialized from a mapping object's
#  |      (key, value) pairs
#  |  dict(iterable) -> new dictionary initialized as if via:
#  |      d = {}
#  |      for k, v in iterable:
#  |          d[k] = v
#  |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
#  |      in the keyword argument list.  For example:  dict(one=1, two=2)
#  |  
#  |  Methods defined here:
#  |  
#  |  __contains__(self, key, /)
#  |      True if the dictionary has the specified key, else False.
#  |  
#  |  __delitem__(self, key, /)
#  |      Delete self[key].
#  |  
#  |  __eq__(self, value, /)
#  |      Return self==value.
#  |  
#  |  __ge__(self, value, /)
#  |      Return self>=value.
#  |  
#  |  __getattribute__(self, name, /)
#  |      Return getattr(self, name).
#  |  
#  |  __getitem__(...)
#  |      x.__getitem__(y) <==> x[y]
#  |  
#  |  __gt__(self, value, /)
#  |      Return self>value.
#  |  
#  |  __init__(self, /, *args, **kwargs)
#  |      Initialize self.  See help(type(self)) for accurate signature.
#  |  
#  |  __ior__(self, value, /)
#  |      Return self|=value.
#  |  
#  |  __iter__(self, /)
#  |      Implement iter(self).
#  |  
#  |  __le__(self, value, /)
#  |      Return self<=value.
#  |  
#  |  __len__(self, /)
#  |      Return len(self).
#  |  
#  |  __lt__(self, value, /)
#  |      Return self<value.
#  |  
#  |  __ne__(self, value, /)
#  |      Return self!=value.
#  |  
#  |  __or__(self, value, /)
#  |      Return self|value.
#  |  
#  |  __repr__(self, /)
#  |      Return repr(self).
#  |  
#  |  __reversed__(self, /)
# __ror__(self, value, /)
#  |      Return value|self.
#  |  
#  |  __setitem__(self, key, value, /)
#  |      Set self[key] to value.
#  |  
#  |  __sizeof__(...)
#  |      D.__sizeof__() -> size of D in memory, in bytes
#  |  
#  |  clear(...)
#  |      D.clear() -> None.  Remove all items from D.
#  |  
#  |  copy(...)
#  |      D.copy() -> a shallow copy of D
#  |  
#  |  get(self, key, default=None, /)
#  |      Return the value for key if key is in the dictionary, else default.
#  |  
#  |  items(...)
#  |      D.items() -> a set-like object providing a view on D's items
#  |  
#  |  keys(...)
#  |      D.keys() -> a set-like object providing a view on D's keys
#  |  
#  |  pop(...)
#  |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
#  |      
#  |      If key is not found, default is returned if given, otherwise KeyError is raised
#  |  
#  |  popitem(self, /)
#  |      Remove and return a (key, value) pair as a 2-tuple.
#  |      
#  |      Pairs are returned in LIFO (last-in, first-out) order.
#  |      Raises KeyError if the dict is empty.
#  |  
#  |  setdefault(self, key, default=None, /)
#  |      Insert key with a value of default if key is not in the dictionary.
#  |      
#  |      Return the value for key if key is in the dictionary, else default.
#  |  
#  |  update(...)
#  |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
#  |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
#  |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
#  |      In either case, this is followed by: for k in F:  D[k] = F[k]
#  |  
#  |  values(...)
#  |      D.values() -> an object providing a view on D's values
#  |  ----------------------------------------------------------------------
#  |  Class methods defined here:
#  |  
#  |  __class_getitem__(...) from builtins.type
#  |      See PEP 585
#  |  
#  |  fromkeys(iterable, value=None, /) from builtins.type
#  |      Create a new dictionary with keys from iterable and values set to value.
#  |  
#  |  ----------------------------------------------------------------------
#  |  Static methods defined here:
#  |  
#  |  __new__(*args, **kwargs) from builtins.type
#  |      Create and return a new object.  See help(type) for accurate signature.
#  |  
#  |  ----------------------------------------------------------------------
#  |  Data and other attributes defined here:
#  |  
#  |  __hash__ = None


# print(all(space is not None for space in spaces.values()))
# the all is an efficient way to check the value of all spaces is one thing or another. it returns true or false. it will stop
# at the first one that presents a false.