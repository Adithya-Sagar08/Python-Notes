#1.Basic Star Patterns(Printing_Star_Patterns.py)

n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))
for i in range(n):
    for j in range(m):
        print("*", end=" ")
    print()

#Right - Angled
#Triangle:
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

#2.Diamond StarPattern(Printing_Star_Patterns2.py)

n = int(input("Enter a number: "))

# Upper half
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

# Lower half
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)
#3.Number Patterns(Printing_Number_Patterns.py)

n = int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()

#Floyd's Triangle (Sequential Numbers):

n = int(input("Enter a number: "))
k = 1
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(k, end=" ")
        k += 1
    print()
#4.Alphabet Patterns(Printing_Alpha_Patterns.py)

n = int(input("Enter a number: "))
k = 0
for i in range(n):
    for j in range(n):
        print(chr(65 + k), end=" ")
        k += 1
    print()
#Repeating Alphabet Triangle:

n = int(input("Enter a number: "))
for i in range(n):
    for j in range(i + 1):
        print(chr(65 + i), end=" ")
    print()