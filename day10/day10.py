# ============================================================
# DAY 10 - DICTIONARY, IF & IF-ELSE
# ============================================================


# ============================================================
# 1. DICTIONARY CREATION & ACCESSING
# ============================================================

student = {
    "name": "Shiva",
    "age": 21,
    "city": "Hyderabad",
    "course": "Python"
}

print("--- Dictionary ---")
print("Student:", student)
print("Name:", student["name"])
print("Age:", student["age"])


# ============================================================
# 2. ADDING & UPDATING DICTIONARY VALUES
# ============================================================

print("\n--- Add & Update ---")

student["email"] = "shiva@gmail.com"
student["age"] = 22

print("Updated Dictionary:", student)


# ============================================================
# 3. DICTIONARY METHODS
# ============================================================

print("\n--- Dictionary Methods ---")

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

print("City:", student.get("city"))

student.pop("email")
print("After pop:", student)


# ============================================================
# 4. ITERATING THROUGH A DICTIONARY
# ============================================================

print("\n--- Dictionary Iteration ---")

for key, value in student.items():
    print(key, ":", value)


# ============================================================
# 5. IF STATEMENT
# ============================================================

print("\n--- If Statement ---")

age = 21

if age >= 18:
    print("You are eligible to vote.")


# ============================================================
# 6. IF STATEMENT WITH DICTIONARY
# ============================================================

print("\n--- If with Dictionary ---")

marks = {
    "Python": 85,
    "Java": 70,
    "SQL": 90
}

if marks["Python"] >= 50:
    print("Passed in Python")


# ============================================================
# 7. IF-ELSE STATEMENT
# ============================================================

print("\n--- If-Else ---")

number = 10

if number % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")


# ============================================================
# 8. IF-ELSE WITH USER INPUT
# ============================================================

print("\n--- User Input ---")

user_number = int(input("Enter a number: "))

if user_number > 0:
    print("Positive Number")
else:
    print("Zero or Negative Number")


# ============================================================
# 9. IF-ELSE WITH DICTIONARY
# ============================================================

print("\n--- Dictionary + If-Else ---")

product = {
    "name": "Laptop",
    "price": 50000,
    "stock": 5
}

if product["stock"] > 0:
    print(product["name"], "is Available")
else:
    print(product["name"], "is Out of Stock")