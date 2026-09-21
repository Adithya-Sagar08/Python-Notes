class Student:
    # constructor
    def __init__(self):
        self.name = "Ramu"  # instance variable
        self.age = 20  # instance variable
        print("My name is:", self.name)
        print("My age is:", self.age)


# object creation
s1 = Student()
print("my name outside the class is:", s1.name)
print("my age outside the class is:", s1.age)