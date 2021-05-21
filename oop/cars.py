class Car:
    top_speed = 100
    warnings = []

    # dunder functions = double under functions
    # auto executes when we call the class as a function, like when we create a new instance
    # we define instance attributes with __init__

    def __init__(self, starting_top_speed=100):
        self.top_speed = starting_top_speed
        self.__warnings = []

    def __repr__(self):
        print('Printing...')
        return 'Top Speed: {}, Warnings: {}'.format(self.top_speed, len(self.warnings))

    def add_warning(self, warning_text):
      if len(warning_text) > 0:
        self.__warnings.append(warning_text)

    def get_warnings(self):
      return self.__warnings


    # self is not a reserved keyword
    # you could use a different name
    # but the convention is to go
    # with SELF
    def drive(self):
        print('I am driving but certainly not faster than {}'.format(self.top_speed))


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
