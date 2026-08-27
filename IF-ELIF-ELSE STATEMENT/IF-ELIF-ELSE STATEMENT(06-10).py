# 6. ATM Machine

balance = 10000

choice = input("Enter choice (balance / withdraw): ")

if choice == "balance":
    print("Your balance is:", balance)

elif choice == "withdraw":
    amount = int(input("Enter amount: "))

    if amount <= balance:
        balance = balance - amount
        print("Withdrawal successful")
        print("Remaining balance:", balance)

    else:
        print("Insufficient balance")

else:
    print("Invalid choice")


# 7. Greeting Based on Time

hour = int(input("Enter hour: "))

if hour >= 5 and hour < 12:
    print("Good Morning")

elif 12 <= hour < 17:
    print("Good Afternoon")

elif hour >= 17 and hour < 21:
    print("Good Evening")

elif hour >= 21 or hour < 5:
    print("Good Night")

else:
    print("Invalid hour")

# 8. Discount Coupon Code

price = float(input("Enter price: "))
coupon = input("Enter coupon code: ")

if coupon == "SAVE20":
    discount = 20
    final_price = price - (price * discount / 100)
    print("Discount:", discount, "%")
    print("Final price:", final_price)

elif coupon == "SAVE10":
    discount = 10
    final_price = price - (price * discount / 100)
    print("Discount:", discount, "%")
    print("Final price:", final_price)

else:
    print("Invalid coupon code")
    print("Final price:", price)


#9. Grade Based on Score

score = int(input("Enter score: "))

if score < 0 or score > 100:
    print("Invalid score")

elif score >= 90:
    print("Grade: A")

elif score >= 80:
    print("Grade: B")

elif score >= 70:
    print("Grade: C")

elif score >= 60:
    print("Grade: D")

else:
    print("Grade: F")


#10. Calculator Using Operation Choice

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

