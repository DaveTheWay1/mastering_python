class Car():
  def __init__(self, make, model):
    self.make = make
    self.model = model
    self.running = False

  def start(self):
    self.running = True
    print(f"The {self.make} {self.model} has started.")
    
  def stop(self):
    self.running = False
    print(f"The {self.make} {self.model} has come to a stop.")

  def __str__(self):
    return f"My {self.make} nice. it's a 2.0; not a reguluh"

my_car = Car("honda", "accord")
print(my_car)
my_car.start()
my_car.stop()

# output:
# My honda nice. it's a 2.0; not a reguluh
# True
# False