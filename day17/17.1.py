# Day 17 - Recursion Examples


# 1. Factorial using Recursion
def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)


# 2. Sum of Natural Numbers using Recursion
def sum_natural(num):
    if num == 0:
        return 0
    return num + sum_natural(num - 1)


# 3. Fibonacci using Recursion
def fibonacci(num):
    if num <= 1:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


# 4. Power of a Number using Recursion
def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)


# 5. Reverse a String using Recursion
def reverse_string(text):
    if text == "":
        return ""
    return reverse_string(text[1:]) + text[0]


# Main Block
if __name__ == "__main__":

    print("1. Factorial")
    factorial_num = int(input("Enter a number: "))
    print("Factorial:", factorial(factorial_num))

    print("\n2. Sum of Natural Numbers")
    sum_num = int(input("Enter a number: "))
    print("Sum:", sum_natural(sum_num))

    print("\n3. Fibonacci")
    fibonacci_terms = int(input("Enter the number of terms: "))

    print("Fibonacci Series:", end=" ")
    for i in range(fibonacci_terms):
        print(fibonacci(i), end=" ")

    print("\n\n4. Power")
    power_base = int(input("Enter base: "))
    power_exponent = int(input("Enter exponent: "))
    print("Result:", power(power_base, power_exponent))

    print("\n5. Reverse String")
    input_text = input("Enter a string: ")
    print("Reversed String:", reverse_string(input_text))