#1.Count Even Digits(no_of_even.py)Based on

n = int(input("enter a number:"))
s = str(n)
count = 0
for i in s:
    if int(i) % 2 == 0:
        count += 1
print(f"count of even digits in {n} is {count}")

#2.Reverse a Number(Reverse_num.py)Based on

n = int(input("enter a number: "))
temp = n
rev = 0
while n > 0:
    r = n % 10
    rev = rev * 10 + r
    n = n // 10
print(f"Reverse of {temp} is {rev}")

#3.Check Prime Number(Primeornot.py)

n = int(input("Enter number: "))

if n < 2:
    print("Not a prime number")
else:
    is_prime = True

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")


#4.Check Palindrome(Palindromeornot.py)

n = int(input())
temp = n
rev = 0
while n > 0:
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10
if temp == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")


#5.Find Factors and Check if Prime / Composite(factors.py)

n = int(input("Enter number: "))

factors = []

for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        factors.append(i)

        if i != n // i:
            factors.append(n // i)

factors.sort()

print("Factors:", *factors)

if len(factors) == 2:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is a composite number.")