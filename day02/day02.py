# DAY 2 - PYTHON BASICS

# 1. Print Statement
print("\n--- 1. Print ---")
print("Hello, Python!")


# 2. Variables and Literals
print("\n--- 2. Variables and Literals ---")

name = "Adithya"
age = 24
percentage = 85.5
passed = True

print("Name:", name)
print("Age:", age)
print("Percentage:", percentage)
print("Passed:", passed)


# 3. Identifiers and Keywords
print("\n--- 3. Identifiers ---")

student_name = "Adithya"
total_marks = 450

print("Student:", student_name)
print("Marks:", total_marks)


# 4. Arithmetic Operators
print("\n--- 4. Arithmetic Operators ---")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)


# 5. Comparison and Logical Operators
print("\n--- 5. Comparison and Logical Operators ---")

print("a == b:", a == b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a != b:", a != b)
print("a > 0 and b > 0:", a > 0 and b > 0)


# 6. Multiple Assignment
print("\n--- 6. Multiple Assignment ---")

x, y, z = 10, 20, 30

print("x:", x)
print("y:", y)
print("z:", z)


# 7. Reassignment
print("\n--- 7. Reassignment ---")

number = 10
print("Before:", number)

number = 100
print("After:", number)


# 8. Swapping Variables
print("\n--- 8. Swapping ---")

a, b = b, a

print("After swapping:")
print("a:", a)
print("b:", b)


# 9. Mutable Object
print("\n--- 9. Mutable Object ---")

numbers = [10, 20]

print("Before:", numbers)

numbers.append(30)

print("After:", numbers)


# 10. Immutable Object
print("\n--- 10. Immutable Object ---")

text = "Python"

print("Before:", text)

text = text + " Programming"

print("After:", text)


# 11. Delete Variable
print("\n--- 11. Delete Variable ---")

value = 10
print("Before deleting:", value)

del value

print("Variable deleted successfully.")


# 12. Practical Example
print("\n--- 12. Practical Example ---")

student_name = input("Enter student name: ")
marks = int(input("Enter marks: "))

result = marks >= 35

print("Student:", student_name)
print("Marks:", marks)
print("Passed:", result)