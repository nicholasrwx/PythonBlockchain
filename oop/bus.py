from vehicle import Vehicle

class Bus(Vehicle):
  
    # dunder functions = double under functions
    # auto executes when we call the class as a function, like when we create a new instance
    # we define instance attributes with __init__

    def __init__(self, starting_top_speed=100):
        super().__init__(starting_top_speed)
        self.passengers = []

    def add_group(self, passengers):
      self.passengers.extend(passengers)

bus1 = Bus(150)
bus1.add_warning('Test')
bus1.add_group(['Max', 'Manuel', 'Anna'])

print(bus1.passengers)

bus1.drive()



