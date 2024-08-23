class Dog():
  # class attribute
  next_id = 1

  # updated __init__
  def __init__(self, name, age=0):
    self.name = name
    self.age = age
    self.id = Dog.next_id
    Dog.next_id += 1

  def bark(self):
    print(f'{self.name} says woof!')

  # updated __str__
  def __str__(self):
    return f'Dog ({self.id}) named {self.name} is {self.age} years old'
  
  @classmethod
  def get_total_dogs(cls):
    # cls represents the Dog class
    return cls.next_id - 1
    # the minus 1 exists here bc of line 10 since after creating the last dog
    # we immediately increase the id so that it is ready for the next dog's id.
    # therefore, the minus 1 is important here bc it assures the accurate amount
    # of dogs

cazador = Dog("Cazador", 7)
chocolate = Dog("Chocolate", 18)

# class methods are called on the class, not an instance
print(Dog.get_total_dogs())
# output: 2

print(cazador.get_total_dogs())
# output: 2
# ! although this was called on the instance, class methods are to be called by the class for NEATNESS and 
# ! GOOD python practice.

# * The @classmethod decorator
# * The naming convention of the first parameter is to use cls instead of self