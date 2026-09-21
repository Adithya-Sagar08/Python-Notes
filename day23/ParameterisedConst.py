# Parameterised Constructor
class Employee:

    def __init__(self, name, e_id, salary):
        self.name = name
        self.e_id = e_id
        self.salary = salary

    def Display(self):
        print("My name is:", self.name)
        print("My Id is:", self.e_id)
        print("My salary is:", self.salary)


e1 = Employee(name="shiva", e_id="emp234", salary=50000)
e1.Display()
print()
e2 = Employee(name="varun", e_id="emp244", salary=50000)
e2.Display()