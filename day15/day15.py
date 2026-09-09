# 1. Without arguments & without return value
def greet():
    print("Welcome to Python Functions")

greet()


# 2. Without arguments & with return value
def get_name():
    return "Adithya Sagar"

print("Name:", get_name())


# 3. With arguments & with return value
def add(a, b):
    return a + b

result = add(10, 20)
print("Addition:", result)


# 4. With arguments & without return value
def display_sum(a, b):
    print("Sum:", a + b)

display_sum(15, 25)


# 5. Default arguments
def student(name, age=21, city="Hyderabad"):
    print(name, age, city)

student("Ravi")
student("Rahul", 25)
student("naveen", 30, "Bangalore")


# 6. *args - Variable positional arguments
def total(*numbers):
    print("Numbers:", numbers)
    print("Total:", sum(numbers))

total(10, 20, 30, 40)


# 7. **kwargs - Variable keyword arguments
def details(**data):
    for key, value in data.items():
        print(key, ":", value)

details(name="Shiva", age=21, city="Hyderabad")


# 8. Positional-only arguments
def multiply(a, b, /):
    return a * b

print("Multiplication:", multiply(5, 4))


# 9. Keyword-only arguments
def employee(*, name, salary):
    print("Name:", name)
    print("Salary:", salary)

employee(name="Adithya", salary=30000)