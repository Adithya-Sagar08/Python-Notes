
import re

text = "Hello Python! Contact me at adithya@gmail.com or call 9876543210."

# 1. re.match() - checks at the beginning
result = re.match(r"Hello", text)
print("Match:", result.group() if result else "No match")

# 2. re.search() - finds the first occurrence
result = re.search(r"Python", text)
print("Search:", result.group() if result else "No match")

# 3. re.findall() - finds all matching patterns
numbers = re.findall(r"\d+", text)
print("Numbers:", numbers)

# 4. re.finditer() - returns match objects
for match in re.finditer(r"\w+", text):
    print("Word:", match.group())

# 5. re.sub() - replaces matching text
updated_text = re.sub(r"Python", "Java", text)
print("Replaced:", updated_text)

# 6. re.split() - splits text using a pattern
words = re.split(r"\s+", text)
print("Split:", words)

# 7. Character classes and quantifiers
sample = "cat bat rat mat"
print("Words ending with at:", re.findall(r"\w+at", sample))

# 8. Email pattern validation (basic example)
email = "adithya@gmail.com"
pattern = r"^[\w.-]+@[\w.-]+\.[A-Za-z]{2,}$"

if re.fullmatch(pattern, email):
    print("Valid email format")
else:
    print("Invalid email format")

# 9. Phone number validation (10 digits)
phone = "9876543210"

if re.fullmatch(r"\d{10}", phone):
    print("Valid 10-digit phone format")
else:
    print("Invalid phone format")
