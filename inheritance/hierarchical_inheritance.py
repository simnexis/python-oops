# Demonstrates hierarchical inheritance in Python

class Parent:
    # Method defined in Parent class
    def show_parent(self):
        print("This is the Parent class")


class ChildOne(Parent):
    # Method defined in ChildOne class
    def show_child_one(self):
        print("This is Child One")


class ChildTwo(Parent):
    # Method defined in ChildTwo class
    def show_child_two(self):
        print("This is Child Two")


# Creating objects of both child classes
child1 = ChildOne()
child2 = ChildTwo()

# Calling Parent method using ChildOne object
child1.show_parent()
child1.show_child_one()

# Calling Parent method using ChildTwo object
child2.show_parent()
child2.show_child_two()
