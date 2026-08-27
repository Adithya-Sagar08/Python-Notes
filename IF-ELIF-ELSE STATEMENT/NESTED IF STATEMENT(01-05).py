# 1. Compare x and y

x = int(input("Enter x: "))
y = int(input("Enter y: "))

if x > y:
    print("x is greater than y")

    if x > 15:
        print("x is also greater than 15")
    else:
        print("x is not greater than 15")

else:
    print("x is not greater than y")

#2. Grade and Pass/Fail


grade = int(input("Enter grade: "))

if grade >= 90:
    print("Letter grade: A")

elif grade >= 80:
    print("Letter grade: B")

elif grade >= 70:
    print("Letter grade: C")

else:
    print("Letter grade: D")

    if grade < 70:
        print("You failed.")


#3. Credit Card Eligibility


age = int(input("Enter age: "))
income = float(input("Enter income: "))

if age >= 18:

    if income >= 30000:
        print("You are eligible for a credit card.")

    else:
        print("Your income is too low for a credit card.")

else:
    print("You are underage.")

# 4. Even/Odd and Greater Than 10


num = int(input("Enter number: "))

if num % 2 == 0:
    print(num, "is even")

    if num > 10:
        print(num, "is greater than 10")

    else:
        print(num, "is not greater than 10")

else:
    print(num, "is odd")


#5. Theme Park Ticket Price

age = int(input("Enter age: "))
height = float(input("Enter height in feet: "))

if age < 12:

    if height < 4:
        print("Ticket price: $10")

    else:
        print("Ticket price: $15")

else:

    if height < 4:
        print("Ticket price: $15")

    else:
        print("Ticket price: $20")

