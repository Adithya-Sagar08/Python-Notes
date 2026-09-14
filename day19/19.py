# ==========================================
# DAY 19 - PYTHON MODULES
# User-Defined & Built-in Modules
# ==========================================


# ==========================================
# 1. USER-DEFINED MODULE CONCEPT
# ==========================================

def greet():
    return "Welcome to Python Modules"


def msg():
    return "Modules are fun..."


print("----- User-Defined Module -----")

print("Function call:", greet())
print("Function call:", greet())
print("Function call:", msg())


# ==========================================
# 2. CALCULATOR MODULE CONCEPT
# ==========================================

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    if y != 0:
        return x / y
    return "Provide a valid input"


print("\n----- Calculator Module -----")

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

print("Addition is:", add(first_number, second_number))
print("Subtraction is:", subtract(first_number, second_number))
print("Multiplication is:", mul(first_number, second_number))
print("Division is:", div(first_number, second_number))


# ==========================================
# 3. BUILT-IN random MODULE
# ==========================================

import random

print("\n----- random Module -----")

print("Random number:", random.random())

print("Random integer:", random.randint(1, 10))

colors = ["red", "green", "blue"]

print("Random color:", random.choice(colors))

print("Random float:", random.uniform(1, 10))


# ==========================================
# 4. BUILT-IN itertools MODULE
# ==========================================

from itertools import count, permutations, combinations

print("\n----- itertools Module -----")

numbers = [1, 2, 3, 4, 4, 4, 3, 3, 3, 2, 2]

print("Count of 3:", numbers.count(3))

permutation_result = permutations("abc", 2)
print("Permutations:", list(permutation_result))

combination_result = combinations("abc", 2)
print("Combinations:", list(combination_result))

print("First 5 values using count():")

counter = count(1)

for _ in range(5):
    print(next(counter))


# ==========================================
# 5. BUILT-IN json MODULE
# ==========================================

import json

print("\n----- json Module -----")

student = {
    "name": "Ramu",
    "age": 23
}

print("Dictionary:", student)
print("Type before conversion:", type(student).__name__)

json_string = json.dumps(student)

print("JSON String:", json_string)
print("Type after conversion:", type(json_string).__name__)


# ==========================================
# 6. BUILT-IN sys MODULE
# ==========================================

import sys

print("\n----- sys Module -----")

print("Current recursion limit:",
      sys.getrecursionlimit())

sys.setrecursionlimit(100000)

print("New recursion limit:",
      sys.getrecursionlimit())

my_list = [1, 3, 4, 3]

print("List:", my_list)

print("Size of list:",
      sys.getsizeof(my_list))


# ==========================================
# 7. __name__ CONCEPT
# ==========================================

print("\n----- __name__ Concept -----")

print("Current module name:", __name__)

if __name__ == "__main__":
    print("This program is running directly.")