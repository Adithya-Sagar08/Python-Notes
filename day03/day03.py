
print("----- 1. SINGLE LINE COMMENTS -----")

# This is a single-line comment.
# Comments are ignored by the Python interpreter.
# They are used to explain the program.

print("Welcome to Python")

print("----- 2. MULTI LINE COMMENTS -----")

"""
This is a multi-line text block.

It contains multiple lines.
Triple quotes are commonly used
for documentation or multi-line text.
"""

print("Python Programming")

print()


# ============================================================
# 3. SWAPPING VARIABLES
# ============================================================

print("----- 3. SWAPPING VARIABLES -----")

# Taking input from the user
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

print("\nBefore Swapping:")
print("a =", a)
print("b =", b)

# Pythonic swapping
# The values of a and b are exchanged.
a, b = b, a

print("\nAfter Swapping:")
print("a =", a)
print("b =", b)

print()


print("----- 4. NUMERIC DATATYPES -----")

# -------------------- INTEGER --------------------

age = 23

print("Integer value    :", age)
print("Integer datatype :", type(age).__name__)


# -------------------- FLOAT --------------------

percentage = 95.5

print("\nFloat value      :", percentage)
print("Float datatype   :", type(percentage).__name__)


# -------------------- COMPLEX --------------------

z = 4 + 5j

print("\nComplex value    :", z)
print("Complex datatype :", type(z).__name__)

print("Real part        :", z.real)
print("Imaginary part   :", z.imag)

print()

print("----- 5. STRINGS -----")

# Taking string input from the user
name = input("Enter your name: ")
city = input("Enter your city: ")

print("\nString Values:")
print("Name :", name)
print("City :", city)

# Accessing the first character
print("\nFirst character of name:", name[0])

# Checking datatype
print("Name datatype:", type(name).__name__)

print()


print("----- 6. LISTS -----")

numbers = [10, 20, 30]

print("Original list:")
print(numbers)

# Accessing elements using index
print("\nFirst element :", numbers[0])
print("Second element:", numbers[1])

# Adding a new element
numbers.append(40)

print("\nList after adding 40:")
print(numbers)

print("List datatype:", type(numbers).__name__)

print()


print("----- 7. TUPLES -----")

colors = ("Red", "Blue", "Green")

print("Tuple:")
print(colors)

# Accessing elements using index
print("\nFirst color :", colors[0])
print("Second color:", colors[1])

print("\nTuple datatype:", type(colors).__name__)

print()

print("----- SINGLE ITEM TUPLE -----")

student = ("Raju",)

print("Student tuple:")
print(student)

print("Datatype:", type(student).__name__)

print()

print("----- 8. RANGE -----")


# -------------------- ONE ARGUMENT --------------------

print("range(5):")
print(list(range(5)))


# -------------------- TWO ARGUMENTS --------------------

print("\nrange(2, 8):")
print(list(range(2, 8)))


# -------------------- THREE ARGUMENTS --------------------

print("\nrange(0, 10, 2):")
print(list(range(0, 10, 2)))

print()


print("----- 9. DATA TYPE CHECKING -----")

name = "Raju"
age = 23
marks = 97.5

print("Name :", name)
print("Datatype of name :", type(name).__name__)

print("\nAge :", age)
print("Datatype of age  :", type(age).__name__)

print("\nMarks :", marks)
print("Datatype of marks:", type(marks).__name__)


