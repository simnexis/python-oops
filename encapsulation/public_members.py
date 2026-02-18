# Demonstrates public data members and methods

class Employee:
    def __init__(self, name):
        # Public variable
        self.name = name

    # Public method
    def display(self):
        print("Employee Name:", self.name)


# Creating object
emp = Employee("Simran")

# Accessing public variable directly
print(emp.name)

# Calling public method
emp.display()
