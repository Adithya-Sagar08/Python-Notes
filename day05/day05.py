# DAY - OPERATORS

# 1. Arithmetic Operators
print("\n--- 1. Arithmetic Operators ---")

a = 17
b = 5

print("Addition       :", a + b)
print("Subtraction    :", a - b)
print("Multiplication :", a * b)
print("Division       :", a / b)
print("Floor Division :", a // b)
print("Modulus        :", a % b)
print("Power          :", a ** b)


# 2. Arithmetic Operators with Input
print("\n--- 2. Arithmetic with Input ---")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition       :", a + b)
print("Subtraction    :", a - b)
print("Multiplication :", a * b)

if b != 0:
    print("Division       :", a / b)
    print("Floor Division :", a // b)
    print("Modulus        :", a % b)
else:
    print("Division       : Cannot divide by zero")


# 3. Assignment Operators
print("\n--- 3. Assignment Operators ---")

number = 10

number += 5
print("After += 5:", number)

number -= 3
print("After -= 3:", number)

number *= 2
print("After *= 2:", number)

number //= 4
print("After //= 4:", number)

number %= 3
print("After %= 3:", number)

number **= 2
print("After **= 2:", number)


# 4. Comparison Operators
print("\n--- 4. Comparison Operators ---")

a = 10
b = 5

print("a == b:", a == b)
print("a != b:", a != b)
print("a > b :", a > b)
print("a < b :", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)


# 5. Comparison with Input
print("\n--- 5. Comparison with Input ---")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("a == b:", a == b)
print("a != b:", a != b)
print("a > b :", a > b)
print("a < b :", a < b)


# 6. Logical Operators
print("\n--- 6. Logical Operators ---")

marks = int(input("Enter marks: "))
age = int(input("Enter age: "))

print("AND:", marks >= 60 and age >= 18)
print("OR :", marks >= 60 or age >= 18)
print("NOT:", not (marks >= 60))


# 7. Bitwise Operators
print("\n--- 7. Bitwise Operators ---")

a = 10
b = 15

print("AND :", a & b)
print("OR  :", a | b)
print("XOR :", a ^ b)
print("NOT :", ~a)
print("Left Shift :", a << 1)
print("Right Shift:", a >> 1)


# 8. Bitwise Operators with Input
print("\n--- 8. Bitwise with Input ---")

a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

print("a & b:", a & b)
print("a | b:", a | b)
print("a ^ b:", a ^ b)


# 9. Membership Operators
print("\n--- 9. Membership Operators ---")

fruits = ["Apple", "Mango", "Orange"]

print("Apple in fruits:", "Apple" in fruits)
print("Grapes not in fruits:", "Grapes" not in fruits)

name = "Python"
print("'P' in name:", "P" in name)


# 10. Membership with Input
print("\n--- 10. Membership with Input ---")

fruit = input("Enter fruit name: ")

print("Available:", fruit in fruits)
print("Not Available:", fruit not in fruits)


# 11. Identity Operators
print("\n--- 11. Identity Operators ---")

list_a = [10, 20, 30]
list_b = list_a
list_c = [10, 20, 30]

print("list_a is list_b:", list_a is list_b)
print("list_a is not list_c:", list_a is not list_c)
print("list_a == list_c:", list_a == list_c)


# 12. Identity with None
print("\n--- 12. Identity with None ---")

result = None

print("result is None:", result is None)
print("result is not None:", result is not None)


# 13. Ternary Operator
print("\n--- 13. Ternary Operator ---")

number = int(input("Enter a number: "))

result = "Even" if number % 2 == 0 else "Odd"

print("Result:", result)


# 14. Ternary - Pass or Fail
print("\n--- 14. Pass or Fail ---")

marks = int(input("Enter marks: "))

result = "Pass" if marks >= 35 else "Fail"

print("Result:", result)


# 15. Operator Precedence
print("\n--- 15. Operator Precedence ---")

print("10 + 5 * 2 =", 10 + 5 * 2)
print("(10 + 5) * 2 =", (10 + 5) * 2)


# 16. Real-Time Example
print("\n--- 16. Eligibility Example ---")

marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance percentage: "))

eligible = marks >= 60 and attendance >= 75

print("Eligible for admission:", eligible)