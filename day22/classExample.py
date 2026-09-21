class Student:
    # constructor
    def __init__(self):
        print("I am no parameterised constructor")
        print("address of self:", id(self))


# object creation
s1 = Student()
print("address of s1:", id(s1))
s2 = Student()
print("address of s2:", id(s2))