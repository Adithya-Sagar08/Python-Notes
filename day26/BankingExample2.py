class BankAccount:

    def __init__(self, name, acc_no, balance):
        self.name = name
        self.__acc_no = acc_no
        self.__balance = balance

    # Usage of Getters and Setters to achieve Encapsulation
    # Validating the Account Number
    def __is_validAccno(self, acc_no):  # private method
        return self.__acc_no == acc_no

    # Showing the balance
    def Showbalance(self, acc_no):
        if self.__is_validAccno(acc_no):
            return f"Your Balance is {self.__balance}"
        else:
            return f"Invalid Account Number: {acc_no}"

    # Deposit the Amount in the Account
    def DepositAmount(self, amount, acc_no):
        if self.__is_validAccno(acc_no):
            if amount > 0:
                self.__balance += amount
                return f"Amount {amount} is Deposited successfully"
            else:
                return f"Invalid Amount {amount} entered"
        else:
            return f"Invalid Account Number: {acc_no}"

    # Withdraw the Amount in the Account
    def WithdrawAmount(self, amount, acc_no):
        if self.__is_validAccno(acc_no):
            if amount > 0 and amount <= self.__balance:
                self.__balance -= amount
                return f"Amount {amount} is Withdrawn successfully"
            else:
                return (
                    f"Invalid Amount {amount} entered or insufficient balance"
                )
        else:
            return f"Invalid Account Number: {acc_no}"


b = BankAccount("Shiva", 1234, 10000)
print(b.Showbalance(1234))
print(b.DepositAmount(25000, 1234))
print(b.Showbalance(1234))
print(b.WithdrawAmount(2000, 1234))
print(b.Showbalance(1234))