class Vehicle:

    @staticmethod
    def fuel_type():
        print("Uses petrol or diesel or gas")


class Car(Vehicle):

    @staticmethod
    def drive():
        print("Driving")


class Bike(Vehicle):

    @staticmethod
    def ride():
        print("Riding")


b = Bike()
c = Car()

c.drive()
b.ride()
b.fuel_type()