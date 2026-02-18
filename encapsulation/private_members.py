# Demonstrates private data members

class BankAccount:
    def __init__(self, balance):
        # Private variable (double underscore)
        self.__balance = balance

    def show_balance(self):
        # Accessing private variable inside the class
        print("Balance:", self.__balance)


# Creating object
account = BankAccount(5000)

# Calling public method to access private data
account.show_balance()

# Direct access like account.__balance is NOT allowed
