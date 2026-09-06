# DAY - INPUT, OUTPUT & FORMATTING

# 1. String Input
print("\n--- 1. String Input ---")
name = input("Enter your name: ")
print("Name:", name)


# 2. Integer Input
print("\n--- 2. Integer Input ---")
age = int(input("Enter your age: "))
print("Age:", age)


# 3. Float Input
print("\n--- 3. Float Input ---")
salary = float(input("Enter your salary: "))
print("Salary:", salary)


# 4. Multiple Inputs
print("\n--- 4. Multiple Inputs ---")
first_name, last_name = input(
    "Enter first name and last name: "
).split()

print("First Name:", first_name)
print("Last Name:", last_name)


# 5. Integer List Input
print("\n--- 5. Integer List Input ---")
numbers = list(map(int, input(
    "Enter numbers separated by spaces: "
).split()))

print("Numbers:", numbers)


# 6. Comma-Separated Input
print("\n--- 6. Comma-Separated Input ---")
fruits = [fruit.strip() for fruit in input(
    "Enter fruits separated by commas: "
).split(",")]

print("Fruits:", fruits)


# 7. Tuple Input
print("\n--- 7. Tuple Input ---")
values = tuple(map(int, input(
    "Enter numbers separated by spaces: "
).split()))

print("Tuple:", values)


# 8. Set Input
print("\n--- 8. Set Input ---")
unique_numbers = set(map(int, input(
    "Enter numbers separated by spaces: "
).split()))

print("Unique Numbers:", unique_numbers)


# 9. Dictionary Input
print("\n--- 9. Dictionary Input ---")
student_name = input("Enter student name: ")
student_age = int(input("Enter student age: "))
student_city = input("Enter student city: ")

student = {
    "name": student_name,
    "age": student_age,
    "city": student_city
}

print("Student:", student)


# 10. Type Conversion
print("\n--- 10. Type Conversion ---")
value = input("Enter a number: ")
number = int(value)

print("Value:", number)
print("Type:", type(number).__name__)


# 11. Basic Output
print("\n--- 11. Basic Output ---")
print("Hello, Python!")
print("Name:", "Adithya", "Age:", 25)


# 12. sep Parameter
print("\n--- 12. sep Parameter ---")
print("2026", "08", "13", sep="-")


# 13. end Parameter
print("\n--- 13. end Parameter ---")
print("Hello", end=" ")
print("Python")


# 14. Escape Characters
print("\n--- 14. Escape Characters ---")
print("Line 1\nLine 2")
print("Name:\tAdithya")


# 15. % Formatting
print("\n--- 15. % Formatting ---")
student_name = "Adithya"
student_age = 25

print("Name: %s | Age: %d" % (student_name, student_age))


# 16. str.format()
print("\n--- 16. str.format() ---")
print("Name: {} | Age: {}".format(student_name, student_age))


# 17. f-string
print("\n--- 17. f-string ---")
print(f"Name: {student_name} | Age: {student_age}")


# 18. Decimal Formatting
print("\n--- 18. Decimal Formatting ---")
price = 1250.5678
print(f"Price: {price:.2f}")


# 19. Percentage Formatting
print("\n--- 19. Percentage Formatting ---")
percentage = 0.875
print(f"Percentage: {percentage:.2%}")


# 20. Alignment
print("\n--- 20. Alignment ---")
print(f"{'Name':<15}{'Age':>5}{'Score':>10}")
print(f"{student_name:<15}{student_age:>5}{92.50:>10.2f}")


# 21. Formatted Table
print("\n--- 21. Formatted Table ---")
print(f"{'Name':<15}{'Age':>5}{'Score':>10}")
print("-" * 30)
print(f"{'Adithya':<15}{25:>5}{92.50:>10.2f}")
print(f"{'Rahul':<15}{24:>5}{88.75:>10.2f}")


# 22. Billing Example
print("\n--- 22. Billing Example ---")
product = input("Enter product name: ")
quantity = int(input("Enter quantity: "))
unit_price = float(input("Enter price per item: "))

total = quantity * unit_price

print("\n--- BILL ---")
print(f"Product  : {product}")
print(f"Quantity : {quantity}")
print(f"Price    : {unit_price:.2f}")
print(f"Total    : {total:.2f}")