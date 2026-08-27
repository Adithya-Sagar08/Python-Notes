# 11. Greatest of Three Number
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("Greatest number is:", a)
elif b > a and b > c:
    print("Greatest number is:", b)
else:
    print("Greatest number is:", c)

# 12. Three-Digit Number
n = int(input("Enter a number: "))

if n >= 100 and n <= 999:
    print("Its three digit number")
elif n <= -100 and n >= -999:
    print("Its three digit number")
else:
    print("Not a three digit number")

# 13. Temperature
temperature = int(input("Enter temperature: "))

if temperature > 30:
    print("It's hot")
elif temperature >= 15:
    print("Pleasant")
else:
    print("Cold")


# 14. Positive, Negative, or Zero
n = int(input("Enter a number: "))

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

#15. Student Grade
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
else:
    print("F")