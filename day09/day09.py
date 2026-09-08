# ============================================================
# DAY 9 - TUPLES & SETS
# ============================================================


# ============================================================
# 1. TUPLE CREATION & ACCESSING
# ============================================================

student = ("Shiva", 21, "Hyderabad", "Python")

print("--- Tuple ---")
print("Tuple:", student)
print("First Element:", student[0])
print("Last Element:", student[-1])


# ============================================================
# 2. TUPLE SLICING & ITERATION
# ============================================================

print("\n--- Tuple Slicing ---")
print("Slice:", student[1:3])

print("Tuple Elements:")
for item in student:
    print(item)


# ============================================================
# 3. TUPLE PACKING & UNPACKING
# ============================================================

print("\n--- Tuple Packing & Unpacking ---")

packed_tuple = "Shiva", 21, "Hyderabad"
print("Packed Tuple:", packed_tuple)

name, age, city = packed_tuple

print("Name:", name)
print("Age:", age)
print("City:", city)


# ============================================================
# 4. TUPLE METHODS
# ============================================================

print("\n--- Tuple Methods ---")

numbers = (10, 20, 30, 20, 40, 20)

print("Tuple:", numbers)
print("Count of 20:", numbers.count(20))
print("Index of 30:", numbers.index(30))


# ============================================================
# 5. NESTED TUPLE
# ============================================================

print("\n--- Nested Tuple ---")

students = (
    ("Shiva", 21),
    ("Varun", 22),
    ("Pranavi", 20)
)

print("Students:", students)
print("First Student:", students[0])
print("First Student Name:", students[0][0])


# ============================================================
# 6. SET CREATION & DUPLICATE REMOVAL
# ============================================================

print("\n--- Set ---")

values = {10, 20, 30, 20, 40, 10}

print("Set:", values)

# Duplicate values are automatically removed.


# ============================================================
# 7. ADDING & REMOVING ELEMENTS
# ============================================================

print("\n--- Set Add & Remove ---")

numbers_set = {10, 20, 30}

numbers_set.add(40)
print("After add:", numbers_set)

numbers_set.remove(20)
print("After remove:", numbers_set)

numbers_set.discard(100)
print("After discard:", numbers_set)


# ============================================================
# 8. SET OPERATIONS
# ============================================================

print("\n--- Set Operations ---")

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print("Set A:", set_a)
print("Set B:", set_b)

print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference A-B:", set_a - set_b)
print("Difference B-A:", set_b - set_a)
print("Symmetric Difference:", set_a ^ set_b)


# ============================================================
# 9. SET MEMBERSHIP & ITERATION
# ============================================================

print("\n--- Set Membership & Iteration ---")

languages = {"Python", "Java", "C++"}

print("Python" in languages)
print("JavaScript" in languages)

for language in languages:
    print(language)