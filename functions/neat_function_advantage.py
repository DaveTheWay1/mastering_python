
# * For example, here’s how you could dynamically “select” which function 
# to call using a dictionary instead of a potentially 
# huge if...elif...else statement:

def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

math_operations = {
  '+': add,
  '-': subtract
}

selected_operation = '+'

math_operations[selected_operation](2, 4)
# > 6