class User:

    @staticmethod
    def login():
        print("Everyone need to login...")


class Manager(User):

    @staticmethod
    def manage_users():
        print("Manager manages the users")


m = Manager()
m.login()
m.manage_users()