# Demonstrates multilevel inheritance in Python

class Grandparent:
    # Method defined in Grandparent class
    def show_grandparent(self):
        print("This is the Grandparent class")


class Parent(Grandparent):
    # Method defined in Parent class
    def show_parent(self):
        print("This is the Parent class")


class Child(Parent):
    # Method defined in Child class
    def show_child(self):
        print("This is the Child class")


# Creating object of Child class
child_obj = Child()

# Calling methods from all levels
child_obj.show_grandparent()
child_obj.show_parent()
child_obj.show_child()
