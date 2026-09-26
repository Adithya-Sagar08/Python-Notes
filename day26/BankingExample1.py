class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance  # Encapsulated

    def Showbalance(self):
        print(f"Your Balance: {self.__balance}")

    def Deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Amount {amount} is deposited successfully"
        else:
            return f"Invalid Amount {amount} entered"

    def Withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Amount {amount} is withdrawn succesfully"
        else:
            return f"Invalid Amount entered or Insufficient Balance"


b = BankAccount("Raju", 100000)
b.Showbalance()
print(b.Deposit(10000))
b.Showbalance()
print(b.Withdraw(12000))
b.Showbalance()