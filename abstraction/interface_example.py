# ABSTRACTION: Interface-like behavior in Python
# Meaning:
# Python does not have interfaces like Java,
# but abstract classes can be used to achieve interface behavior.
# An interface defines what methods a class must have.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    # Method that every child class must implement
    @abstractmethod
    def start(self):
        pass


class Bike(Vehicle):
    # Bike provides its own implementation of start()
    def start(self):
        print("Bike starts using kick")


# Creating object of Bike class
bike = Bike()
bike.start()
