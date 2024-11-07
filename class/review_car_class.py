class Car():
    def __init__(self, make, model, running = False):
        self.make = make
        self.model = model
        self.running = running

    def start(self):
        self.running = True
        print("running...")
        return "running..."
    
    def stop(self):
        self.running = False
        print("stopped...")

    def __str__(self):
        return(f"{self.make} {self.model} is {'running..' if self.running == True else 'stopped...' }")
    
    def __repr__(self):
        return f"Car(make={self.make!r}, model={self.model}, running={self.running})"
my_car = Car("honda", "accord")

print(my_car.make, my_car.model, my_car.running)
my_car.start()
print(my_car.running)
print(my_car)
print(repr(my_car))

# ? Why does print(my_car) call __str__?
# * When you use print() on an object, Python internally calls the __str__ method, if 
# it's defined. This is because print() is meant to output a user-friendly string 
# representation of the object. If __str__ isn't defined, Python falls back to __repr__.

# ? Why do you need to explicitly call repr()?
# The __repr__ method is not called automatically with print(). 
# You need to use repr() explicitly, like this:
print(repr(my_car))