#1. Celsius ↔ Fahrenheit

choice = input("Enter conversion (C to F / F to C): ")
temperature = float(input("Enter temperature: "))

if choice == "C to F":
    fahrenheit = (temperature * 9 / 5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)

elif choice == "F to C":
    celsius = (temperature - 32) * 5 / 9
    print("Temperature in Celsius:", celsius)

else:
    print("Invalid conversion")


#2. Simple Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print("Result:", num1 + num2)

elif operation == "-":
    print("Result:", num1 - num2)

elif operation == "*":
    print("Result:", num1 * num2)

elif operation == "/":
    print("Result:", num1 / num2)

else:
    print("Invalid operation")


#3. Guess the Number Game

import random

number = random.randint(1, 10)

guess = int(input("Guess the number: "))

if guess == number:
    print("Congratulations! You guessed the number.")

else:
    print("Wrong guess. Try again.")
    print("The number was:", number)



#4. Password Strength
password = input("Enter password: ")

if len(password) >= 8 and any(char.isdigit() for char in password):
    print("Strong password")

else:
    print("Weak password")



#5. Discount Based on Purchase Amount

amount = float(input("Enter purchase amount: "))

if amount >= 5000:
    discount = 20
    final_price = amount - (amount * discount / 100)

elif amount >= 1000:
    discount = 10
    final_price = amount - (amount * discount / 100)

else:
    discount = 0
    final_price = amount

print("Discount:", discount, "%")
print("Final price:", final_price)

