class Student:
    college = "Codegnan"  # Class Variable

    # constructor
    def __init__(self):
        print("I am no parameterised constructor")
        print("My college name inside the class is:", Student.college)


# object creation
s1 = Student()
print("My college name outside the class is:", Student.college)
print("My college name outside the class is:", s1.college)