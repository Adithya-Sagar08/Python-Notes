class A:

    @staticmethod
    def m1():
        print("I am m1() in class-A")


class B:

    @staticmethod
    def m1():
        print("I am m1() in class-B")


class C(A, B):  # Follows C3 Linearization / MRO
    pass


c = C()
c.m1()

# Printing MRO explicitly
print(C.__mro__)
# Alternative explicit tuple syntax if your IDE linter continues to complain:
# print(C.mro())