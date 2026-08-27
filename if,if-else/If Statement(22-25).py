#22. Check Whether a Number is Positive

n = int(input("Enter a number: "))

if n > 0:
    print("Positive Number")


#23. Check Whether a String is Empty

s = input("Enter a string: ")

if s == "":
    print("String is Empty")



#24. Positive, Negative, or Zero Using Only if

n = int(input("Enter a number: "))

if n > 0:
    print("Positive")

if n < 0:
    print("Negative")

if n == 0:
    print("Zero")

# 25.Multiple of Both 3 and 5

n = int(input("Enter a number: "))

if n % 3 == 0 and n % 5 == 0:
    print("Multiple of 3 and 5")