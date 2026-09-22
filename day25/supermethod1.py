class Employee:

    def __init__(self, name):
        self.name = name

    def show(self):
        print("Employee Name is:", self.name)


class Manager(Employee):

    def __init__(self, name, dept):
        super().__init__(name)
        self.dept = dept

    def show(self) -> None:
        super().show()
        print("My Dept name is:", self.dept)


m = Manager("Adithya", "Computer Science")
m.show()