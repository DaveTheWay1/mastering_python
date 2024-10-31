class Dog():
    def __init__(self, name, age=0):
    # * Python automatically calls the __init__ magic method when a new dog is created.
    # __init__ is short for “initialize” because the method is used to initialize 
    # the properties of the new object.
        # * self parameter in class init method is only that; a parameter.
        # - this is because, for exmaple, cazador.bark(),,, after creating
        # an object of that class and labing it cazador.. it becomes the first thing
        # passed in which is why/how it simply takes in the space of self. 
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} says woof!")

    def dogs_age(self):
        print(f"{self.name} is {self.age} years old")

cazador = Dog("Cazador", 7)
print(cazador)
# <__main__.Dog object at 0x100c29e80> the last few numbers and letters that follow is a memory location.
print(cazador.name, cazador.age)
# output: Cazador 7
cazador.bark()
# output:
# Cazador says woof!

cazador.dogs_age()
# output:
# Cazador is 7 years old