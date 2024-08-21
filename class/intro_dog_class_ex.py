class Dog():
    def __init__(self, name, age=0):
        # * self parameter in class init method is only that; a parameter.
        # - this is because, for exmaple, cazador.bark(),,, after creating
        # an object of that class and labing it cazador.. it becomes the first thing
        # passed in which is why/how it simply takes in the space of self. 
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} says woof!")

cazador = Dog("Cazador", 7)
print(cazador)
# <__main__.Dog object at 0x100c29e80>
print(cazador.name, cazador.age)
# output: Cazador 7
cazador.bark()
# output:
# Cazador says woof!