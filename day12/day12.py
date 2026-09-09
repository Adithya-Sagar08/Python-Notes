#1. while-else.py — OTP Verification
correct_otp = "2432"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    entered_otp = input("Enter OTP: ")

    if entered_otp == correct_otp:
        print("OTP Verified Successfully!")
        break
    else:
        print("Incorrect OTP. Try again.")
        attempts += 1
else:
    print("OTP expired. Request a new one.")


#2. continue_statement.py — Skip a Number
l = [1, 2, 3, 4, 5]

for i in range(len(l)):
    if l[i] == 3:
        continue

    print(l[i])


#3. for-else.py — Search for an ID
ids = [101, 102, 103, 104]
key = 108

for i in range(len(ids)):
    if ids[i] == key:
        print("Key found")
        break
else:
    print("Key not found")

print("End of the program")

#4. break statement

numbers = [10, 20, 30, 40, 50]
target = 30

for n in numbers:
    if n == target:
        print("Target found:", n)
        break
    print("Current number:", n)
