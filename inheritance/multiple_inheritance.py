# Demonstrates multiple inheritance in Python

class Father:
    # Method defined in Father class
    def show_father(self):
        print("This is the Father class")


class Mother:
    # Method defined in Mother class
    def show_mother(self):
        print("This is the Mother class")


class Child(Father, Mother):
    # Method defined in Child class
    def show_child(self):
        print("This is the Child class")


# Creating object of Child class
child_obj = Child()

# Calling methods from both parent classes
child_obj.show_father()
child_obj.show_mother()

# Calling Child's own method
child_obj.show_child()
