# * Combining Required Positional, Optional Positional (*args) & Keyword (**kwargs) Arguments
# You can use all three types of parameters in the same 
# function, but they have to be defined in the following order:

def arg_demo(pos1, pos2, *args, **kwargs):
    print(f'Positional params: {pos1}, {pos2}')
    print('*args:')
    for arg in args:
      print(' ', arg)
      print('**kwargs:')
    for keyword, value in kwargs.items():
      print(f'  {keyword}: {value}')

# arg_demo('A', 'B', 1, 2, 3, color='purple', shape='circle')
# Output:
# Positional params: A, B
# *args:
#   1
#   2
#   3
# **kwargs:
#   color: purple
#   shape: circle