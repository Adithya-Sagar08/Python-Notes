from abc import ABC, abstractmethod


class Bank(ABC):  # Inheritance

    @abstractmethod
    def Loan_interest(self):
        pass

    def Message(self):
        print("Every Bank comes with an App")


class SBI(Bank):  # Inheritance

    def Loan_interest(self):
        print("SBI Loan Interest is 10% ")


class HDFC(Bank):

    def Loan_interest(self):
        print("HDFC Loan Interest is 8%")


h = HDFC()
h.Loan_interest()
s = SBI()
s.Loan_interest()