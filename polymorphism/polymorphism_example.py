# POLYMORPHISM: Same method, different behavior
# Meaning:
# Polymorphism allows different objects to respond differently
# to the same method call.

class Bird:
    def fly(self):
        print("Bird can fly")


class Penguin(Bird):
    # Penguin provides a different behavior for the same method
    def fly(self):
        print("Penguin cannot fly")


# Creating objects
bird = Bird()
penguin = Penguin()

# Same method name, different outputs
bird.fly()
penguin.fly()
