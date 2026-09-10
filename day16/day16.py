"""
DAY 16/100: Scopes & Functional Programming
Course: Python Full Stack Development at Codegnan
"""

from functools import reduce


# ==================================================
# 1. LOCAL SCOPE
# ==================================================
print("\n--- 1. Local Scope ---")


def student():
    student_name = "Shiva"
    print("Inside function:", student_name)


student()


# ==================================================
# 2. GLOBAL SCOPE
# ==================================================
print("\n--- 2. Global Scope ---")

company_name = "Codegnan"


def display_company():
    print("Inside function:", company_name)


display_company()
print("Outside function:", company_name)


# ==================================================
# 3. LOCAL VARIABLE
# ==================================================
print("\n--- 3. Local Variable ---")

global_number = 10


def update_number():
    local_number = 100
    print("Inside function:", local_number)


update_number()
print("Outside function:", global_number)


# ==================================================
# 4. GLOBAL KEYWORD
# ==================================================
print("\n--- 4. Global Keyword ---")

global_value = 10


def update_global_value():
    global global_value
    global_value = 100
    print("Inside function:", global_value)


print("Before function:", global_value)
update_global_value()
print("After function:", global_value)


# ==================================================
# 5. ENCLOSING SCOPE & NONLOCAL
# ==================================================
print("\n--- 5. Enclosing Scope & Nonlocal ---")


def outer_function():
    outer_value = 10

    def inner_function():
        nonlocal outer_value
        outer_value = 100
        print("Inside inner function:", outer_value)

    print("Before inner function:", outer_value)
    inner_function()
    print("After inner function:", outer_value)


outer_function()


# ==================================================
# 6. LEGB RULE
# ==================================================
print("\n--- 6. LEGB Rule ---")

global_message = "Global"


def outer_scope():
    enclosing_message = "Enclosing"

    def inner_scope():
        local_message = "Local"
        print("Local:", local_message)
        print("Enclosing:", enclosing_message)
        print("Global:", global_message)
        print("Built-in:", len("Python"))

    inner_scope()


outer_scope()

print("\nLEGB Order:")
print("L - Local")
print("E - Enclosing")
print("G - Global")
print("B - Built-in")


# ==================================================
# 7. MUTABLE OBJECT
# ==================================================
print("\n--- 7. Mutable Object ---")


def add_item(shopping_cart):
    shopping_cart.append("Laptop")


shopping_cart = ["Mobile", "Watch"]

print("Before function:", shopping_cart)
add_item(shopping_cart)
print("After function:", shopping_cart)


# ==================================================
# 8. IMMUTABLE OBJECT
# ==================================================
print("\n--- 8. Immutable Object ---")


def change_number(original_number):
    new_number = 100
    print("Inside function:", new_number)


original_value = 50

print("Before function:", original_value)
change_number(original_value)
print("After function:", original_value)


# ==================================================
# 9. LAMBDA FUNCTION
# ==================================================
print("\n--- 9. Lambda Function ---")

square_number = lambda number: number * number

print("Square of 5:", square_number(5))
print("Square of 10:", square_number(10))


# ==================================================
# 10. MAP FUNCTION
# ==================================================
print("\n--- 10. map() Function ---")

number_list = [1, 2, 3, 4, 5]

square_list = list(
    map(lambda number: number * number, number_list)
)

print("Numbers:", number_list)
print("Squares:", square_list)


names_list = ["shiva", "ravi", "sneha"]

uppercase_names = list(
    map(lambda person_name: person_name.upper(), names_list)
)

print("Original names:", names_list)
print("Uppercase names:", uppercase_names)


# ==================================================
# 11. FILTER FUNCTION
# ==================================================
print("\n--- 11. filter() Function ---")

number_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_values = list(
    filter(lambda number: number % 2 == 0, number_values)
)

odd_values = list(
    filter(lambda number: number % 2 != 0, number_values)
)

print("Numbers:", number_values)
print("Even numbers:", even_values)
print("Odd numbers:", odd_values)


# ==================================================
# 12. FILTER WITH CONDITION
# ==================================================
print("\n--- 12. Filter Prices ---")

price_list = [500, 1200, 800, 2500, 600]

high_price_list = list(
    filter(lambda price: price > 1000, price_list)
)

print("Prices:", price_list)
print("Prices above 1000:", high_price_list)


# ==================================================
# 13. REDUCE FUNCTION
# ==================================================
print("\n--- 13. reduce() Function ---")

sum_numbers = [1, 2, 3, 4, 5]

total_sum = reduce(
    lambda first_number, second_number:
    first_number + second_number,
    sum_numbers
)

print("Numbers:", sum_numbers)
print("Total:", total_sum)


# ==================================================
# 14. REDUCE - PRODUCT
# ==================================================
print("\n--- 14. Reduce Product ---")

product_numbers = [1, 2, 3, 4]

total_product = reduce(
    lambda first_number, second_number:
    first_number * second_number,
    product_numbers
)

print("Numbers:", product_numbers)
print("Product:", total_product)


# ==================================================
# 15. REDUCE - MAXIMUM
# ==================================================
print("\n--- 15. Reduce Maximum ---")

maximum_numbers = [10, 25, 8, 40, 15]

maximum_value = reduce(
    lambda first_number, second_number:
    first_number if first_number > second_number
    else second_number,
    maximum_numbers
)

print("Numbers:", maximum_numbers)
print("Maximum number:", maximum_value)