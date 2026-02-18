# Demonstrates basic class definition and object usage

class Student:
    name = "Simran"
    age = 20

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Creating an object of the class
s = Student()
s.display()
