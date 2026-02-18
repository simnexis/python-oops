# POLYMORPHISM: Method Overriding
# Meaning:
# Method overriding occurs when a child class provides its own implementation
# of a method that already exists in the parent class.
# The child class method replaces (overrides) the parent class method.

class Animal:
    # Parent class method
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    # Child class overrides the parent class method
    def sound(self):
        print("Dog barks")


# Creating object of Dog class
dog = Dog()

# Even though sound() exists in Animal,
# the Dog class version is executed
dog.sound()
