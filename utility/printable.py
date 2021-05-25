class Printable:
    #repr is a built-in function, that displays a printable version of the object
    #so when we go to print a class, it recognizes repr if it is in the class
    # and what is returned from repr automatically takes precedence for outputting 
    # the class. This basically lets you DEFINE HOW you want the PRINTABLE version to look.
     
    def __repr__(self):
      return str(self.__dict__)
