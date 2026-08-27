#  1. Take an integer input from the user and print whether it is positive or negative.

n = int(input("Enter a number: "))

if n > 0:
    print("Positive")
else:
    print("Negative")

# 2.  Take an input number from the user and check whether it is even or odd.

n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")

#3.  Ask the user for their age. If the age is 18 or more, print (You are eligible to vote.)

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")

#4. Pass or Fail
marks = int(input("Enter marks: "))

if marks >= 35:
    print("Pass")
else:
    print("Fail")

#5. Greater of Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a)
else:
    print(b)