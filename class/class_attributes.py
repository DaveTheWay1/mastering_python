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

cazador = Dog("Cazador", 7)
chocolate = Dog("Chocolate", 18)

print(cazador.id)
# output: 1
print(cazador.name)
# output: Cazador

print(cazador)
# Dog (1) named Cazador is 7 years old
print(chocolate)
# Dog (2) named Chocolate is 18 years old