class Student:

    def __init__(self):
        self.name = 'shiva'  # public member declaration
        self.age = 23
        self._marks = 90  # protected member declaration
        self.__color = "white"  # private member declaration

    def Display(self):
        print(f"My name is {self.name}")
        print(f"My marks inside parent class are: {self._marks}")
        print(f"My color is: {self.__color}")


class Child(Student):

    def Show(self):
        print(
            f"My marks inside child class are: {self._marks}"
        )  # protected can be used in the
        # main class and the subclass

        # print(f"My color is {self.__color}")  It cannot be accessed inside the child class
        # since it is a private member


s = Student()
s.Display()
print(
    s.name
)  # public member can be accessed inside and outside the class
c = Child()
c.Show()

# Manggling mechanism can be used to access a private member outside the class
# but it breaks the encapsulation rule
print(
    "Through Manggling accessing color(not recommended):",
    s._Student__color,
)