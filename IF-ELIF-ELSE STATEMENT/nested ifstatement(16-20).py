#16. Delivery Charges

distance = float(input("Enter distance: "))
amount = float(input("Enter order amount: "))

if distance <= 5:

    if amount >= 500:
        charge = 0
    else:
        charge = 20

else:

    if amount >= 500:
        charge = 30
    else:
        charge = 50

print("Delivery charge: $", charge)


#17. Employee Performance and Bonus


score = int(input("Enter performance score: "))
years = int(input("Enter years of service: "))

if score >= 90:

    print("Performance: Excellent")

    if years >= 5:
        bonus = 20000
    else:
        bonus = 15000

elif score >= 70:

    print("Performance: Good")

    if years >= 5:
        bonus = 12000
    else:
        bonus = 10000

else:

    print("Performance: Average")

    if years >= 5:
        bonus = 7000
    else:
        bonus = 5000

print("Bonus:", bonus)


#18. Library Late Fee


days = int(input("Enter overdue days: "))
book_type = input("Enter book type: ")

if book_type == "regular":

    if days <= 7:
        fee = days * 1
    else:
        fee = days * 2

elif book_type == "reference":

    if days <= 7:
        fee = days * 2
    else:
        fee = days * 4

else:
    fee = 0
    print("Invalid book type")

print("Late fee: $", fee)


#19. Scholarship Eligibility


gpa = float(input("Enter GPA: "))
activities = int(input("Enter number of activities: "))

if gpa > 3.5:

    if activities >= 3:
        print("Scholarship awarded")
    else:
        print("Scholarship not awarded")

else:
    print("Scholarship not awarded")


#20. Clothing Recommendation


temperature = float(input("Enter temperature: "))
raining = input("Is it raining? ")

if temperature < 20:

    if raining == "yes":
        print("Wear a jacket and carry an umbrella.")
    else:
        print("Wear a jacket.")

else:

    if raining == "yes":
        print("Wear light clothes and carry an umbrella.")
    else:
        print("Wear light clothes.")

