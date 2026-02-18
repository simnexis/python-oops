# Demonstrates single inheritance in Python

class Parent:
    # This method is defined in the Parent class
    def show(self):
        print("This is the Parent class")


class Child(Parent):
    # This method is defined in the Child class
    def display(self):
        print("This is the Child class")


# Creating object of Child class
child_obj = Child()

# Calling method inherited from Parent class
child_obj.show()

# Calling method of Child class
child_obj.display()
