class Dog():
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} says woof!")

    def __str__(self):
        return f'Dog named {self.name} is {self.age} years old'
    
    def __repr__(self):
        return f"Dog(name={self.name!r}, age={self.age!r})"


cazador = Dog("Cazador", 7)
print(cazador)
# <__main__.Dog object at 0x100c29e80>
# * when this prints it is not useful. we can correct this by overriding
# the __str__ method
# * new output with overriding: 
# Dog named Cazador is 7 years old

# *** IN SUMMARY OF STR METHOD
# * before str there is and __repr__() which is what gives us the "non useful" return.
# * through str, we successfully are able to translate that with ease. 
# ! however, it is important to note that repr could essentially have done the same, 
# ! however it'd look slightly different
# def __repr__(self):
#         return f"Dog(name={self.name!r}, age={self.age!r})"
print("repr")
print(repr(cazador))
# output:
# Dog(name='Cazador', age=7)

# ! while both str and repr can be written to return the same results
# it is best to keep them separate and use them as their intended.
# * str is for readability for the users while repr is for developers to 
# receive and unambiguous return and further debug

# * for better understanding, str is to be usedto return normal strings that 
# contain details of an object as you desire 
# * repr on the other hand is to clearly identify what is what like in the example
# rather than to return a normal string

print(cazador.name, cazador.age)
cazador.bark()