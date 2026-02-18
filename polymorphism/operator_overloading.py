# POLYMORPHISM: Operator Overloading
# Meaning:
# Operator overloading allows the same operator (+, -, *, etc.)
# to behave differently for different objects.

class Number:
    def __init__(self, value):
        self.value = value

    # Here, the + operator is overloaded
    # When we use n1 + n2, this method is called internally
    def __add__(self, other):
        return self.value + other.value


# Creating objects
n1 = Number(10)
n2 = Number(20)

# Using + operator on objects
# Internally, Python calls n1.__add__(n2)
result = n1 + n2

print("Sum:", result)
