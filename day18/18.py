# ============================================================
# DAY 18 - FUNCTIONS, ITERATORS, GENERATORS & COMPREHENSIONS
# ============================================================

# 1. Basic Function
def greet():
    return "Good Morning"


print("--- Function ---")
print(greet())


# 2. Function to Calculate Squares
def square_func(value_list):
    square_result = []

    for value in value_list:
        square_result.append(value * value)

    return square_result


print("\n--- Function Square ---")
sample_numbers = [1, 2, 3, 4, 5]
print(*square_func(sample_numbers))


# 3. Iterator using iter() and next()
print("\n--- Iterator ---")
my_list = [1, 2, 3, 4]
list_iterator = iter(my_list)

print(next(list_iterator))
print(next(list_iterator))
print(next(list_iterator))
print(next(list_iterator))


# 4. Simple Generator
def my_gen():
    yield "First yield"
    yield "Second yield"


print("\n--- Simple Generator ---")
simple_generator = my_gen()

print(next(simple_generator))
print(next(simple_generator))


# 5. Generator Execution Flow
def my_gen_verbose():
    print("one")
    yield "First yield"

    print("two")
    yield "Second yield"

    print("three")


print("\n--- Generator Execution Order ---")
verbose_generator = my_gen_verbose()

print(next(verbose_generator))
print(next(verbose_generator))


# 6. Generator with for Loop
def numbers_gen():
    for current_number in range(1, 6):
        yield current_number


print("\n--- Generator Numbers ---")

for generated_number in numbers_gen():
    print(generated_number)


# 7. Generator for Squares
def square_gen(value_list):
    for current_value in value_list:
        yield current_value * current_value


print("\n--- Generator Squares ---")

for square_value in square_gen([1, 2, 3, 4, 5, 6]):
    print(square_value)


# 8. List Comprehensions
print("\n--- List Comprehensions ---")

# Numbers from 1 to 5
number_list = [value for value in range(1, 6)]
print("Numbers:", number_list)

# Squares from 1 to 5
square_list = [value * value for value in range(1, 6)]
print("Squares:", square_list)

# Even numbers from 1 to 10
even_list = [value for value in range(1, 11) if value % 2 == 0]
print("Even Numbers:", even_list)

# Uppercase names
name_list = ["shiva", "teju", "pranavi"]
uppercase_names = [name.upper() for name in name_list]
print("Uppercase Names:", uppercase_names)

# Prices greater than 2000
price_list = [8000, 2444, 5000, 8000, 1000]
high_price_list = [price for price in price_list if price > 2000]
print("Prices > 2000:", high_price_list)

# Index of zero-stock items
stock_list = [1, 3, 0, 9, 10, 0]
zero_stock_indexes = [
    index for index, stock_value in enumerate(stock_list)
    if stock_value == 0
]
print("Zero Stock Indexes:", zero_stock_indexes)


# 9. List Comprehension with Tuples
product_list = [
    ("laptop", 50000),
    ("mobile", 40000),
    ("tab", 30000)
]

selected_products = [
    product_name
    for product_name, product_price in product_list
    if product_price > 30000
]

print("Products > 30000:", selected_products)


# 10. List Comprehension with Dictionaries
product_info_list = [
    {"name": "laptop", "price": 50000, "stock": 2},
    {"name": "mobile", "price": 30000, "stock": 0},
    {"name": "tab", "price": 10000, "stock": 6}
]

available_products = [
    product["name"]
    for product in product_info_list
    if product["stock"] > 0
]

print("Available Products:", available_products)