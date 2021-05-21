class Vehicle:
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
