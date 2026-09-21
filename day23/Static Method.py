class Student:
    college = "CodeGnan"

    def __init__(self):
        self.name = "Ramu"
        self.age = 23
        self.marks = 90

    # Static Method ----> @static_method
    @staticmethod
    def Display():
        print("I am Static Method, I am a helper Function")


s = Student()
Student.Display()  # First way to call the static method
s.Display()  # Second way to call the static method