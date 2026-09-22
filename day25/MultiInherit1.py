class Father:

    @staticmethod
    def work():
        print("Father works")


class Mother:

    @staticmethod
    def makes():
        print("Mother makes food")


class Child(Father, Mother):

    @staticmethod
    def play():
        print("Child plays")


c = Child()
c.makes()
c.work()
c.play()