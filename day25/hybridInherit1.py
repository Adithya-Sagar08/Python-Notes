class A:

    @staticmethod
    def m1():
        print("M1() in class A")


class B(A):

    @staticmethod
    def m2():
        print("M2() in class B")


class C(A):

    @staticmethod
    def m3():
        print("M3() in class C")  # Up to here: Hierarchical Inheritance


class D(B, C):  # Diamond Inheritance (Multiple + Hierarchical)

    @staticmethod
    def m4():
        print("M4() in class D")


d = D()
d.m1()
d.m2()
d.m3()
d.m4()