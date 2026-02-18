# Demonstrates use of constructor (__init__) in Python

class Person:
    # This is the CONSTRUCTOR
    # It is automatically called when an object of the class is created
    def __init__(self, name, age):
        # Initializing instance variables using constructor
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Creating object of Person class
# This line calls the constructor automatically
p1 = Person("Simran", 20)

# Calling method using the object
p1.display()
