class Animal:

    @staticmethod
    def sound():
        print("Animal makes sound")


class Dog(Animal):

    @staticmethod
    def bark():
        print("Dog barks")


d = Dog()
d.sound()
d.bark()