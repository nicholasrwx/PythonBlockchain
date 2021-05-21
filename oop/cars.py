class Car:
  top_speed = 100
  warnings = []

  #self is not a reserved keyword
  #you could use a different name
  #but the convention is to go
  #with SELF


  def drive(self):
    print('I am driving but certainly not faster than {}'.format(self.top_speed))

#create a new instance
car1 = Car()
#call a class method
car1.drive()

#Car.top_speed = 200
Car.warnings.append('New Warning')

car2 = Car()
car2.drive()
print(car2.warnings)

car3 = Car()
car3.drive()
print(car2.warnings)

