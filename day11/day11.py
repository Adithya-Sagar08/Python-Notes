# ============================================================
# DAY 11 - ELIF, NESTED-IF & FOR LOOP
# ============================================================


# ============================================================
# 1. ELIF STATEMENT
# ============================================================

print("--- ELIF Statement ---")

marks = 75

if marks >= 90:
    print("Grade: A+")
elif marks >= 75:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")


# ============================================================
# 2. ELIF WITH USER INPUT
# ============================================================

print("\n--- ELIF with User Input ---")

temperature = int(input("Enter temperature: "))

if temperature >= 35:
    print("It is very hot.")
elif temperature >= 25:
    print("The weather is warm.")
elif temperature >= 15:
    print("The weather is cool.")
else:
    print("It is cold.")


# ============================================================
# 3. NESTED IF
# ============================================================

print("\n--- Nested IF ---")

age = 21
has_id = True

if age >= 18:
    print("Eligible by age.")

    if has_id:
        print("ID verified. Entry allowed.")
    else:
        print("ID is required.")
else:
    print("Not eligible by age.")


# ============================================================
# 4. NESTED IF WITH USER INPUT
# ============================================================

print("\n--- Nested IF with User Input ---")

user_age = int(input("Enter your age: "))

if user_age >= 18:
    citizenship = input("Are you a citizen? (yes/no): ")

    if citizenship.lower() == "yes":
        print("Eligible to vote.")
    else:
        print("Citizenship is required.")
else:
    print("You are not eligible to vote.")


# ============================================================
# 5. FOR LOOP
# ============================================================

print("\n--- FOR Loop ---")

for number in range(1, 6):
    print(number)


# ============================================================
# 6. FOR LOOP WITH LIST
# ============================================================

print("\n--- FOR Loop with List ---")

languages = ["Python", "Java", "C++", "SQL"]

for language in languages:
    print(language)


# ============================================================
# 7. FOR LOOP WITH CONDITION
# ============================================================

print("\n--- FOR Loop with IF ---")

for number in range(1, 11):
    if number % 2 == 0:
        print(number, "is Even")


# ============================================================
# 8. NESTED FOR LOOP
# ============================================================

print("\n--- Nested FOR Loop ---")

for row in range(1, 4):
    for column in range(1, 4):
        print("*", end=" ")
    print()


# ============================================================
# 9. FOR LOOP WITH DICTIONARY
# ============================================================

print("\n--- FOR Loop with Dictionary ---")

student = {
    "name": "Shiva",
    "age": 21,
    "course": "Python"
}

for key, value in student.items():
    print(key, ":", value)