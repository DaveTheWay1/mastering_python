
# * Inheritance
# Using inheritance, a subclass automatically inherits all of the attributes and methods of its superclass.
# The subclass can then define additional attributes and/or methods to make a more specialized class than the superclass.

# * Example to break down the above:
# The superclass can be of a class called Insect. The subclass would be, for example, bumblee or grassphoper;
# a specified kind of insect. The subclass automaticalls inherits all the attributes and methods of the superclass
# as they are all insects, therefore, would have the same attributes and methods that make an insect an insect

class Dog():
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} says woof!")

    def __str__(self):
        return f'Dog named {self.name} is {self.age} years old'
    

# Pass in superclass as argument
class ShowDog(Dog):
  # Add additional parameters AFTER those in the superclass
  def __init__(self, name, age=0, total_earnings=0):
    # Always call the superclass's __init__ first
    Dog.__init__(self, name, age)
    # Now add any new attributes
    self.total_earnings = total_earnings
  
  # Add additional methods
  def add_prize_money(self, amount):
    self.total_earnings += amount
    print(f'{self.name}\'s new total earnings are {self.total_earnings}')

cazador = ShowDog("Cazador", 2, 3)



cazador.bark()
# output:
# Cazador says woof!

print(cazador.total_earnings)
# output: 3

cazador.add_prize_money(500)
# output: Cazador's new total earnings are 503