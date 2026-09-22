class Animal:

    @staticmethod
    def eat():
        print("Eating")


class Dog(Animal):

    @staticmethod
    def bark():
        print("Barking")


class BabyDog(Dog):

    @staticmethod
    def cry():
        print("Crying")


b = BabyDog()
b.cry()
b.bark()
b.eat()