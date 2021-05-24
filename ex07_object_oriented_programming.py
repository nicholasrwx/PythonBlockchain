
class Food:

    name = 'Vegetarian Lasagna'
    kind = 'Pasta'

    def __init__(self):
        self.name = 'Vegetarian Lasagna'
        self.kind = 'Pasta'

    # Instance Method -> can be accessed from an instance of class, can access variables.
    def describe(self):
        return print("I am having {} and the recipe is called {}".format(self.kind, self.name))

    # Static Method -> can be accessed from an instance of a class, has to be passed variables
    @staticmethod
    def describe2(arg1, arg2):
        return print("I am having {} and the recipe is called {}".format(arg1, arg2))

    # Class Method -> has to be accessed
    @classmethod
    def describe3(cls):
        return print("I am having {} and the recipe is called {}".format(cls.kind, cls.name))

    def get_describe(self):
        return self.describe3()


class Meat(Food):

    #gets initialized vars from the super class, and assigns them to the sub class
    def __init__(self):
      super().__init__()

    def __repr__(self):
        return '{}, {}'.format(self.name, self.kind)

    def cook(self):
        return


class Fruit(Food):
    
    #gets initialized vars from the super class, and assigns them to the sub class
    def __init__(self):
      super().__init__()

    def __str__(self):
        return '{}, {}'.format(self.name, self.kind)

    def clean(self):
        return


# Instantiate the Food, Meat, and Fruit class
food = Food()
meat = Meat()
fruit = Fruit()

# Instance Method
food.describe()

# Static Method (pass vars from somewhere)
food.describe2(food.kind, food.name)

# Class Method (using a getter to access a class method)
food.get_describe()


# Print the Food class from the Meat and Fruit class 
print("MEAT CLASS", meat)
print("FRUIT CLASS", fruit)


# ✓ 1) Create a Food class with a “name” and a “kind” attribute as well as a “describe() ”
# method (which prints “name” and “kind” in a sentence).
# ✓ 2) Try turning describe() from an instance method into a class and a static method.
# ✓ 3) Create a  “Meat” and a “Fruit” class – both should inherit from “Food”.
# Add a “cook() ” method to “Meat” and “clean() ” to “Fruit”.
# ✓ 4) Overwrite a “dunder” method to be able to print your “Food” class.