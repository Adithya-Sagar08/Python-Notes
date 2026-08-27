#6. Multiple of 5

n = int(input("Enter a number: "))

if n % 5 == 0:
    print("Multiple of 5")
else:
    print("Not a multiple of 5")


#7. Divisible by 3 and 5

n = int(input("Enter a number: "))

if n % 3 == 0 and n % 5 == 0:
    print("Divisible by 3 and 5")
else:
    print("Not divisible by 3 and 5")


#8. Vowel or Consonant
ch = input("Enter a character: ")

if ch in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")


#9. Admin Check
name = input("Enter your name: ")

if name == "admin":
    print("Welcome, Admin!")


#10. Zero or Non-Zero
n = int(input("Enter a number: "))

if n == 0:
    print("Zero")
else:
    print("Non-Zero")