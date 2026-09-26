# Here is an example for a valid abstract class and an abstract method with its implementation
# inside the child class

from abc import ABC, abstractmethod


class Fruits(ABC):  # Inheritance

    @abstractmethod
    def Taste(self):
        pass

    def M1(self):
        print("I am M1() method")


class Child(Fruits):  # Inheritance

    def Taste(self):
        print("Delicious")


c = Child()
c.Taste()
c.M1()