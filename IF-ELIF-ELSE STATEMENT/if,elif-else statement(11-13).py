#11. Number of Days in a Month

month = int(input("Enter month number: "))

if month == 2:
    print("Number of days: 28")

elif month == 4 or month == 6 or month == 9 or month == 11:
    print("Number of days: 30")

elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("Number of days: 31")

else:
    print("Invalid month")



#12. BMI Category

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height * height)

print("BMI:", round(bmi, 2))

if bmi < 18.5:
    print("Category: Underweight")

elif bmi < 25:
    print("Category: Normal weight")

elif bmi < 30:
    print("Category: Overweight")

else:
    print("Category: Obese")


#13. Letter Grade to GPA


grade = input("Enter grade: ")

if grade == "A":
    print("GPA: 4.0")

elif grade == "B":
    print("GPA: 3.0")

elif grade == "C":
    print("GPA: 2.0")

elif grade == "D":
    print("GPA: 1.0")

elif grade == "F":
    print("GPA: 0.0")

else:
    print("Invalid grade")


