from vehicle import Vehicle 

class Car(Vehicle):
    # top_speed = 100
    # warnings = []

    def brag(self):
      print('Look how cool my car is!') 



# create a new instance
car1 = Car()
# call a class method
car1.drive()

#Car.top_speed = 200
car1.add_warning('New warning')
car1.__warnings.append([])
# displays instance methods in a dict format
# without it, you would just get a memory location
print(car1)

car2 = Car(200)
car2.drive()
print(car2.get_warnings)

car3 = Car(250)
car3.drive()
print(car2.get_warnings)
