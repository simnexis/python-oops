# ABSTRACTION: Abstract Class
# Meaning:
# Abstraction hides implementation details and shows only what is necessary.
# An abstract class cannot be used to create objects directly.
# It forces child classes to implement certain methods.

from abc import ABC, abstractmethod

class Shape(ABC):
    # Abstract method (no implementation here)
    @abstractmethod
    def area(self):
        pass


class Square(Shape):
    # Child class provides implementation of abstract method
    def area(self):
        print("Area of square = side × side")


# Creating object of child class
square = Square()
square.area()
