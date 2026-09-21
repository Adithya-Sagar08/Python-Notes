# No Parameterised Constructor


class Employee:

    def __init__(self):
        self.name = "Sai"
        self.e_id = "emp123"
        self.salary = 100000
        print("My Name is:", self.name)


e1 = Employee()