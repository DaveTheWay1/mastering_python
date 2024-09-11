
# * Working with Strings
# Python also has strings for holding text, just like JavaScript:

my_string = "A double quoted string"
your_string = 'A single quoted string'
# You can also do some multi-line strings by using a triple quote (single or double):

multiline_string = '''This is my string that
                        goes on multiple lines
                          for whatever reason'''

# * Concatenating Strings
# One or more strings can be combined into a single string in the same way we do it in JS, by using the + operator:
little_string = "bad"
medium_string = "super"
long_string = medium_string + little_string
print(long_string)
# prints "superbad"

# * String Interpolation using f-Strings
# Something that Python has had much longer than JavaScript is a nice syntax for performing string interpolation 
# (evaluating Python expressions and embedding the result within strings).

# While we can always use the concatenation operators above, these get ugly when too many of them appear in a string.
# Instead, we can use a syntax similar to ES2015’s template literals.
# You just need to remember to add an f before the string:

state = "Hawaii"
year = 1959
message = f"{state} was the last state to join the U.S. in {year}."
# * When the f is placed directly before the opening quote (single, or double) of the string, 
# it makes a formatted string or, f-String, for short.
# Once we do this, we can put expressions into curly braces to “inject” the result of the expressions into the string.
# f-Strings are awesome, but they’ve only been available since version 3.6 (released in December of 2016).

# Prior to f-Strings, there were a couple of other options, one being # * the string format method:

template = "My name is {} and I like {}"
print( template.format("Jim", "tacos") )
# prints 'My name is Jim and I like tacos'

course = 'SEI'
print( course[0] )
# => Prints 'S'

# We can use negative indexes!
last_letter = course[-1]
print( last_letter )
# => Prints 'I'

# * Although we can access individual characters in a string, we cannot update the individual characters because stings are immutable (like JS):

s = 'Hello'
# I like Jello!
# s[0] = 'J'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object does not support item assignment

print(s.replace('H', "J"))
# output: Jello