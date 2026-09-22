class Parent:

    def __init__(self):
        print("I am constructor in parent class")


class Child(Parent):

    def __init__(self):
        super().__init__()
        print("I am constructor in child class")


c = Child()