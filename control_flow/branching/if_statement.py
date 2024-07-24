
# * Branching with the if Statement
# We can use an if statement to branch to one of several code paths depending upon the result of conditional expression(s).

# * SINGLE PATH IF STATEMENT

floor = "sticky"
walls = "clean"
if floor == "sticky":   
# don't forget the colon
  print("Clean the floor! It's sticky!")
  # more lines of code in this code
  # block need to be indented as well
if walls == "sticky":
  print("Clean the walls! They're sticky!")

# * DUAL PATH if..else STATEMENT:
condition = []
if condition:
  print(f'if result:{condition}')
  # do something
else:
  print(f'else result:{condition}')
    # do something else
    # do something else


# * Multi-path if..elif..else statement:
condition1 = 0
condition2 = {}
condition3 = False
condition4 = ""

if condition1:
  print(f"if results: {condition1}")
  # do something
  # do something
elif condition2:
  print(f"first elif result: {condition2}")
  # do something else
  # do something else
  # do something else
elif condition3 and condition4:
  print(f"second elif result: {condition3}, {condition4}")
  # do another thing entirely
  # do another thing entirely
else:
  print("else results")
  # else do this stuff