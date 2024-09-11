
# * SPLIT METHOD
print("using split on a sentence found within a string")
print("ace of spades".split(" "))
# output: ['ace', 'of', 'spades']
sentence = "ace of spades"
print(sentence.split())
# output: ['ace', 'of', 'spades']
print(" the above lists all words in a sentence by using split. ")
print(" ")

# ? how would we split all the letters in a word?
# print("abcd".split(""))
# ! but that wouldnt work. we'd get an error: ValueError: empty separator
# Instead, use the list() function like this:
print(list("abcd"))
# output: ['a', 'b', 'c', 'd']
# * the above demonstrates how to list all letters in a single worded string
print(" ")

# * INDEX METHOD
# Warning: Raises error if substring not found
# "tesla".index("s")
# => 2

print("david it is".index("is"))
# output:9 
# if it is a word, it will find the index of where that word first starts
# ! this will only locate the index of the first instance, not all instances.
print("david it is".index("s"))
# output: 10

# print("david it is".index("x"))
# output:
# ! ValueError: substring not found
print(" ")

# Like index, but returns -1 if substring not found
# "tesla".find("x")
# => -1
print("david it is".find("is"))
# output: 9
print("david it is".find("x"))
# output: -1

# * the difference here is that UNLIKE index method, find method will prevent an error and give you -1 instead of the error
# if the searched value is not found

# "foo".upper()
# => "FOO"

# "WHY???".lower()
# => "why???"

# "Then I went to the store I like".replace("I", "you")
# => 'Then you went to the store you like'