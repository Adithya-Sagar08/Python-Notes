class Person:

    @staticmethod
    def work():
        print("A Person Works in an MNC")


class Employee(Person):

    @staticmethod
    def manage():
        print("A Employee Manages activities in an MNC")


class Developer(Employee):

    @staticmethod
    def develop():
        print("A Developer develops code")


class Trainer(Developer):

    @staticmethod
    def train():
        print("A Trainer trains the freshers and trainees")


t = Trainer()
t.train()
t.develop()

d = Developer()
d.manage()
d.work()