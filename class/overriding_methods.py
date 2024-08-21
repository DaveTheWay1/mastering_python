class Dog():
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} says woof!")

    def __str__(self):
      return f'Dog named {self.name} is {self.age} years old'


cazador = Dog("Cazador", 7)
print(cazador)
# <__main__.Dog object at 0x100c29e80>
# * when this prints it is not useful. we can correct this by overriding
# the __str__ method
# * new output with overriding: 
# Dog named Cazador is 7 years old

print(cazador.name, cazador.age)
cazador.bark()