# DAY - SET, DICTIONARY, BOOLEAN, NONE & TYPE CONVERSION


# 1. Set Creation and Duplicates
print("\n--- 1. Set ---")

numbers = {10, 20, 30, 10}
print("Set:", numbers)

numbers.add(40)
print("After add:", numbers)


# 2. Set from User Input
print("\n--- 2. Set Input ---")

fruits = set(input(
    "Enter fruits separated by spaces: "
).split())

print("Fruits:", fruits)


# 3. Dictionary Creation
print("\n--- 3. Dictionary ---")

student = {
    "name": "Raju",
    "age": 21,
    "city": "Hyderabad"
}

print("Student:", student)
print("Name:", student["name"])
print("Age:", student.get("age"))


# 4. Dictionary Add and Update
print("\n--- 4. Dictionary Update ---")

student["marks"] = 85
student["age"] = 22

print("Updated Student:", student)


# 5. Boolean Values
print("\n--- 5. Boolean ---")

is_logged_in = True
is_admin = False

print("Logged in:", is_logged_in)
print("Admin:", is_admin)
print("10 > 5:", 10 > 5)


# 6. Boolean with Integer
print("\n--- 6. Boolean with Integer ---")

print("True + 5:", True + 5)
print("False + 5:", False + 5)


# 7. None Value
print("\n--- 7. None ---")

payment_status = None

if payment_status is None:
    print("Payment status is not available")


# 8. Integer and Float Conversion
print("\n--- 8. Integer and Float ---")

number = 10

print("Integer:", number)
print("Float:", float(number))

price = 10.5
print("Float:", price)
print("Integer:", int(price))


# 9. Integer and String Conversion
print("\n--- 9. Integer and String ---")

number = 100
text = str(number)

print("Number:", number)
print("String:", text)


# 10. String to Number
print("\n--- 10. String to Number ---")

text = "25"
number = int(text)

decimal_text = "25.5"
decimal_number = float(decimal_text)

print("Integer:", number)
print("Float:", decimal_number)


# 11. Boolean Conversion
print("\n--- 11. Boolean Conversion ---")

print("bool(10):", bool(10))
print("bool(0):", bool(0))
print("int(True):", int(True))
print("int(False):", int(False))


# 12. List to Tuple
print("\n--- 12. List to Tuple ---")

numbers = [10, 20, 30]
result = tuple(numbers)

print("List:", numbers)
print("Tuple:", result)


# 13. Tuple to List
print("\n--- 13. Tuple to List ---")

numbers = (10, 20, 30)
result = list(numbers)

print("Tuple:", numbers)
print("List:", result)


# 14. List to Set
print("\n--- 14. List to Set ---")

numbers = [10, 20, 20, 30]
result = set(numbers)

print("List:", numbers)
print("Set:", result)


# 15. String to List, Tuple and Set
print("\n--- 15. String Conversions ---")

text = "Python"

print("List :", list(text))
print("Tuple:", tuple(text))
print("Set  :", set(text))


# 16. List to Dictionary
print("\n--- 16. List to Dictionary ---")

data = [
    ("name", "Raju"),
    ("age", 23),
    ("subject", "Python")
]

student = dict(data)

print("Dictionary:", student)