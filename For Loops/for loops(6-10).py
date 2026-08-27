#6. Find maximum value in a list


numbers = [10, 25, 7, 45, 18]

maximum = numbers[0]

for i in numbers:
    if i > maximum:
        maximum = i

print("Maximum =", maximum)


#7. Print characters in a string


text = input("Enter a string: ")

for i in text:
    print("Character =", i)


#8. Count vowels in a string


text = input("Enter a string: ")

count = 0

for i in text:
    if i in "aeiouAEIOU":
        count = count + 1

print("Number of vowels =", count)


#9. Iterate over dictionary and print key-value pairs

student = {
    "name": "Adithya",
    "age": 25,
    "city": "Hyderabad"
}

for key, value in student.items():
    print(key, "=", value)


#10. Print a pattern using nested for loops


n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()