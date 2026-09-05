# ============================================================
# DAY 1 - INTRODUCTION TO PROGRAMMING & PYTHON
# ============================================================

# 1. Print Hello World
print("Hello World")


# 2. Print Name, Age and City
student_name = "Adithya"
student_age = 24
student_city = "Hyderabad"

print("Name:", student_name)
print("Age:", student_age)
print("City:", student_city)


# 3. Store and Print Name
user_name = "Adithya"
print("Name:", user_name)


# 4. Product Name and Price
product_name = "Laptop"
product_price = 50000

print("Product:", product_name)
print("Price:", product_price)


# 5. Employee Name and Salary
employee_name = "Rahul"
employee_salary = 50000

print("Employee:", employee_name)
print("Salary:", employee_salary)


# 6. Calculate Sum of Two Numbers
number1 = 100
number2 = 200

sum_result = number1 + number2

print("Sum:", sum_result)


# 7. Calculate Total Bill
item_price = 500
item_quantity = 3

bill_total = item_price * item_quantity

print("Total Bill:", bill_total)


# 8. Procedural Programming
def login():
    print("1. Login")


def select_restaurant():
    print("2. Select Restaurant")


def select_food():
    print("3. Select Food")


def payment():
    print("4. Payment")


def confirm_order():
    print("5. Order Confirmed")


print("\nFood Ordering Process")
login()
select_restaurant()
select_food()
payment()
confirm_order()


# 9. OOP - Product Object
class Product:
    def __init__(self, product_name, product_price, product_rating):
        self.name = product_name
        self.price = product_price
        self.rating = product_rating


product1 = Product("Laptop", 50000, 4.5)

print("\nProduct Details")
print("Name:", product1.name)
print("Price:", product1.price)
print("Rating:", product1.rating)


# 10. OOP - Product Behaviors
class ProductOperations:

    @staticmethod
    def add_to_cart():
        print("Product added to cart")

    @staticmethod
    def buy_now():
        print("Product purchased")

    @staticmethod
    def add_review():
        print("Review added")


product_operations = ProductOperations()

print("\nProduct Operations")
product_operations.add_to_cart()
product_operations.buy_now()
product_operations.add_review()


# 11. Bill Using Functions
def calculate_bill(bill_price, bill_quantity):
    return bill_price * bill_quantity


bill_product_name = "Laptop"
bill_product_price = 50000
bill_product_quantity = 2

total_bill = calculate_bill(
    bill_product_price,
    bill_product_quantity
)

print("\nBill Details")
print("Product:", bill_product_name)
print("Price:", bill_product_price)
print("Quantity:", bill_product_quantity)
print("Total:", total_bill)