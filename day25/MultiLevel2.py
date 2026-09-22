class Employee:

    @staticmethod
    def work():
        print("Working")


class Developer(Employee):

    @staticmethod
    def develop():
        print("Write the Code")


class Intern(Developer):

    @staticmethod
    def learn():
        print("Learning")


i = Intern()
i.learn()
i.develop()
i.work()