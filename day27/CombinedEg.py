from abc import ABC, abstractmethod


class Vehicle(ABC):  # This is used to hide the implementation details

    @abstractmethod
    def Start_engine(self):
        pass

    @abstractmethod
    def Stop_engine(self):
        pass


class Bike(Vehicle):  # This child class implements the abstract methods

    def Start_engine(self):
        print("Starts with kick or self")

    def Stop_engine(self):
        print("Stops by turning it off with key")


b = Bike()
b.Start_engine()
b.Stop_engine()