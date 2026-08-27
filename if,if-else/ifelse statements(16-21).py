# 16. Polygon Type

sides = int(input("Enter number of sides: "))

if sides == 3:
    print("Triangle")
elif sides == 4:
    print("Quadrilateral")
elif sides == 5:
    print("Pentagon")
else:
    print("Unknown shape")


#17. Bus Fare

age = int(input("Enter your age: "))

if age < 5:
    print("Free")
elif age <= 18:
    print("Half Ticket")
else:
    print("Full Ticket")


#18. Student Grade Calculator

average = float(input("Enter average marks: "))

if average > 90:
    print("Excellent")
elif average >= 70:
    print("Good")
else:
    print("Needs Improvement")


#19. Uppercase, Lowercase, or Not a Letter

ch = input("Enter a character: ")

if ch >= 'A' and ch <= 'Z':
    print("Uppercase")
else:
    if ch >= 'a' and ch <= 'z':
        print("Lowercase")
    else:
        print("Not a letter")


#20. Multiple of 5 + Even/Odd

n = int(input("Enter a number: "))

if n % 5 == 0:
    if n % 2 == 0:
        print(n, "is a multiple of 5 and it is even")
    else:
        print(n, "is a multiple of 5 and it is odd")
else:
    print("its not multiple of 5")

# Multiple of 5 and Positive/Negative

n = int(input("Enter a number: "))

if n % 5 == 0:
    print(n, "is a multiple of 5")
else:
    if n > 0:
        print(n, "is not a multiple of 5 and it is positive")
    else:
        print(n, "is not a multiple of 5 and it is negative")
