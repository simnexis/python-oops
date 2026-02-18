# Demonstrates protected data members

class Company:
    def __init__(self):
        # Protected variable (single underscore)
        self._company_name = "TechCorp"


class Employee(Company):
    def display(self):
        # Accessing protected variable inside child class
        print("Company Name:", self._company_name)


# Creating object of child class
emp = Employee()
emp.display()
