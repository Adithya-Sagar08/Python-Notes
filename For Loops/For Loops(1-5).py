 # 1. Print numbers from 1 to 5 using a for loop
for i in range(1, 6):
    print(i)


# 2. Calculate the sum of numbers from 1 to 10

sum = 0

for i in range(1, 11):
    sum = sum + i

print("Sum =", sum)

#3. Print even numbers from 1 to 10

for i in range(1, 11):
    if i % 2 == 0:
        print(i)


#4. Calculate factorial of a number

n = int(input())

fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial =", fact)

#5. Print elements of a list

numbers = [10, 20, 30, 40, 50]

for i in numbers:
    print(i)