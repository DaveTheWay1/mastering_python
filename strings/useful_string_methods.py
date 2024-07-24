"ace of spades".split(" ")
# => ['ace', 'of', 'spades']

# However, this won't work as desired
"abcd".split("")
# Instead, use the list() function like this:
list("abcd")
# => ['a', 'b', 'c', 'd']

# Warning: Raises error if substring not found
"tesla".index("s")
# => 2

# Like index, but returns -1 if substring not found
"tesla".find("x")
# => -1

"foo".upper()
# => "FOO"

"WHY???".lower()
# => "why???"

"Then I went to the store I like".replace("I", "you")
# => 'Then you went to the store you like'