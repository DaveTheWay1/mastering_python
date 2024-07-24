
# * THE for STATEMENT
# Python’s for statement is not designed like the one you first used in JavaScript:

# Python for loop always iterates over the items in a sequence
names = ["Tom", "Deborah", "Murray", "Axel"]
for name in names:
  print(name)

# * THE while LOOP
# Python also has a while loop construct that will continue to iterate while a given condition is truthy

# Let’s look at the syntax:

condition = True
while condition:
  print("still true")
  # do some stuff
  # continue to do stuff

# *while loops are the go to when the number of times you will need to iterate is unknown.

# ! 👀 Beware of infinite loops! When using while loops, 
# it’s important to ensure that the condition will become falsy 
# as some point so that the loop exits