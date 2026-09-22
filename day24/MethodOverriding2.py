class Shop:

    def Calculatebill(self, a, b=0):
        total = a + b
        print(f"Total Bill(no discount): ${total}")


class SpecialCustomer(Shop):

    def Calculatebill(self, a, b=0):
        total = a + b
        total = total * 0.9  # considering 10 percent discount
        print(f"Total Bill(with discount): ${total}")


# This certainly stimulates method overloading concept
shop = Shop()
shop.Calculatebill(10, 90)  # NO DISCOUNT
spc = SpecialCustomer()
spc.Calculatebill(200, 100)  # WITH DISCOUNT