class Student:
    college = "CG"

    def __init__(self):
        self.name = "Ramu"
        self.age = 20
        self.marks = 89

    # Instance Method
    def Talk(self):
        print("My name is:", self.name)
        print("My age is:", self.age)
        print("My marks are:", self.marks)
        self.marks = 90
        print("My marks afterwards are:", self.marks)

    # Class Method ----> @class_method
    @classmethod
    def Show(cls):
        print(
            "My college inside the class method(using classname) is:",
            Student.college,
        )
        print("My college inside the class method(using cls) is:", cls.college)
        # print("My marks in classmethod",self.marks) #cannot access an instance variable inside a class method

    # Static Method ----> @static_method
    @staticmethod
    def Display():
        x = 10
        print("I am a static method, I am a helper function")


s = Student()
s.Talk()
s.Show()