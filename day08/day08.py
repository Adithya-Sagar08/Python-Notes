
# 1. CREATE STRING
print("\n--- 1. Create String ---")

name = "Python"

print("String:", name)


# 2. CONCATENATION
print("\n--- 2. Concatenation ---")

first = "Hello"
second = "World"

print(first + " " + second)


# 3. REPETITION
print("\n--- 3. Repetition ---")

print("Python " * 3)


# 4. INDEXING
print("\n--- 4. Indexing ---")

text = "Python"

print("First:", text[0])
print("Last:", text[-1])


# 5. SLICING
print("\n--- 5. Slicing ---")

text = "Python"

print("Slice:", text[0:3])
print("First Four:", text[:4])
print("From Index 2:", text[2:])


# 6. MEMBERSHIP
print("\n--- 6. Membership ---")

text = "Python"

print("'Py' in text:", "Py" in text)
print("'Java' not in text:", "Java" not in text)


# 7. BUILT-IN FUNCTIONS
print("\n--- 7. Built-in Functions ---")

text = "Python"

print("Length:", len(text))
print("Maximum:", max(text))
print("Minimum:", min(text))
print("Sorted:", sorted(text))


# 8. CASE METHODS
print("\n--- 8. Case Methods ---")

text = "hello python"

print("Upper:", text.upper())
print("Lower:", text.lower())
print("Capitalize:", text.capitalize())
print("Title:", text.title())
print("Swapcase:", text.swapcase())


# 9. ALIGNMENT METHODS
print("\n--- 9. Alignment Methods ---")

text = "Python"

print("Center:", text.center(10, "*"))
print("Left:", text.ljust(10, "-"))
print("Right:", text.rjust(10, "-"))
print("Zero Fill:", "42".zfill(5))


# 10. SEARCH METHODS
print("\n--- 10. Search Methods ---")

text = "hello"

print("find:", text.find("l"))
print("rfind:", text.rfind("l"))
print("index:", text.index("e"))
print("rindex:", text.rindex("l"))
print("count:", text.count("l"))


# 11. STRING TESTING
print("\n--- 11. String Testing ---")

text = "Python123"

print("Starts with Py:", text.startswith("Py"))
print("Ends with 123:", text.endswith("123"))
print("Is Alphanumeric:", text.isalnum())
print("Is Lower:", text.islower())
print("Is Upper:", text.isupper())


# 12. REPLACE
print("\n--- 12. replace() ---")

text = "I like Java"

print(text.replace("Java", "Python"))


# 13. SPLIT
print("\n--- 13. split() ---")

text = "Python Java C++"

print(text.split())


# 14. JOIN
print("\n--- 14. join() ---")

words = ["Python", "is", "easy"]

print(" ".join(words))


# 15. PARTITION
print("\n--- 15. partition() ---")

text = "apple-pie"

print(text.partition("-"))


# 16. STRIP
print("\n--- 16. strip() ---")

text = "   Python   "

print("Original:", text)
print("Stripped:", text.strip())


# 17. LSTRIP AND RSTRIP
print("\n--- 17. lstrip() and rstrip() ---")

text = "---Python---"

print("Left:", text.lstrip("-"))
print("Right:", text.rstrip("-"))


# 18. ORD AND CHR
print("\n--- 18. ord() and chr() ---")

print("ASCII of A:", ord("A"))
print("Character of 97:", chr(97))


# 19. USER INPUT
print("\n--- 19. User Input ---")

text = input("Enter a string: ")

print("String:", text)
print("Length:", len(text))
print("Upper:", text.upper())
print("Lower:", text.lower())
print("Title:", text.title())


# 20. STRING CHECK
print("\n--- 20. String Checking ---")

text = input("Enter a string to check: ")

print("Is Alphabet:", text.isalpha())
print("Is Alphanumeric:", text.isalnum())
print("Is Digit:", text.isdigit())
print("Starts with A:", text.startswith("A"))
print("Ends with z:", text.endswith("z"))
