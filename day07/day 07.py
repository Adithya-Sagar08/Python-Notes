
# 1. CREATE LIST
print("\n--- 1. Create List ---")

numbers = [10, 20, 30, 40, 50]
print("List:", numbers)


# 2. MIXED LIST
print("\n--- 2. Mixed List ---")

data = [10, "Python", 5.5, True]
print("List:", data)


# 3. CONCATENATION
print("\n--- 3. Concatenation ---")

a = [1, 2, 3]
b = [4, 5, 6]

print("Result:", a + b)


# 4. REPETITION
print("\n--- 4. Repetition ---")

print([1, 2] * 3)


# 5. INDEXING
print("\n--- 5. Indexing ---")

numbers = [10, 20, 30, 40]

print("First:", numbers[0])
print("Last:", numbers[-1])


# 6. SLICING
print("\n--- 6. Slicing ---")

numbers = [10, 20, 30, 40, 50]

print("Slice:", numbers[1:4])
print("Reverse:", numbers[::-1])


# 7. MEMBERSHIP
print("\n--- 7. Membership ---")

numbers = [10, 20, 30]

print("20 in list:", 20 in numbers)
print("50 not in list:", 50 not in numbers)


# 8. BUILT-IN FUNCTIONS
print("\n--- 8. Built-in Functions ---")

numbers = [10, 20, 30, 40, 50]

print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))
print("Sorted:", sorted(numbers))


# 9. APPEND
print("\n--- 9. append() ---")

numbers = [10, 20, 30]
numbers.append(40)

print(numbers)


# 10. EXTEND
print("\n--- 10. extend() ---")

numbers = [10, 20]
numbers.extend([30, 40])

print(numbers)


# 11. INSERT
print("\n--- 11. insert() ---")

numbers = [10, 20, 40]
numbers.insert(2, 30)

print(numbers)


# 12. REMOVE
print("\n--- 12. remove() ---")

numbers = [10, 20, 30, 20]
numbers.remove(20)

print(numbers)


# 13. POP
print("\n--- 13. pop() ---")

numbers = [10, 20, 30]
removed = numbers.pop()

print("Removed:", removed)
print("List:", numbers)


# 14. CLEAR
print("\n--- 14. clear() ---")

numbers = [10, 20, 30]
numbers.clear()

print(numbers)


# 15. INDEX AND COUNT
print("\n--- 15. index() and count() ---")

numbers = [10, 20, 10, 30, 10]

print("Index of 20:", numbers.index(20))
print("Count of 10:", numbers.count(10))


# 16. SORT
print("\n--- 16. sort() ---")

numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)


# 17. REVERSE
print("\n--- 17. reverse() ---")

numbers = [10, 20, 30, 40]

numbers.reverse()

print(numbers)


# 18. COPY
print("\n--- 18. copy() ---")

numbers = [10, 20, 30]

new_numbers = numbers.copy()

print("Original:", numbers)
print("Copy:", new_numbers)


# 19. NESTED LIST
print("\n--- 19. Nested List ---")

data = [[1, 2], [3, 4]]

print("Nested List:", data)
print("Element:", data[1][1])


# 20. USER INPUT
print("\n--- 20. User Input ---")

user_input = input("Enter numbers separated by spaces: ")

numbers = list(map(int, user_input.split()))

print("List:", numbers)
print("Sum:", sum(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sorted:", sorted(numbers))

