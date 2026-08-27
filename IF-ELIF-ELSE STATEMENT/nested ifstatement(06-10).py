#6. User Authentication


username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":

    if password == "1234":
        print("Access granted.")

    else:
        print("Incorrect password.")

else:
    print("Invalid username.")



#7. Food Ordering


food = input("Enter food (Burger / Pizza): ")

if food == "Burger":

    fries = input("Do you want fries? ")

    if fries == "yes":
        print("Your order: Burger with Fries")
    else:
        print("Your order: Burger")

elif food == "Pizza":

    cheese = input("Do you want extra cheese? ")

    if cheese == "yes":
        print("Your order: Pizza with Extra Cheese")
    else:
        print("Your order: Pizza")

else:
    print("Invalid food choice")


#8. Positive/Negative/Zero and Even/Odd


num = int(input("Enter number: "))

if num > 0:
    print("Positive")

    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

elif num < 0:
    print("Negative")

else:
    print("Zero")


#9. Driving Eligibility


age = int(input("Enter age: "))
license = input("Do you have a license? ")

if age >= 18:

    if license == "yes":
        print("You are eligible to drive.")
    else:
        print("You are not eligible to drive.")

else:
    print("You are not eligible to drive.")


#10. Voting Eligibility


age = int(input("Enter age: "))
citizen = input("Are you a citizen? ")

if age >= 18:

    if citizen == "yes":
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")

else:
    print("You are not eligible to vote.")

