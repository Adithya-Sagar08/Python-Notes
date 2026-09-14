import json
import platform as p
import random
import sys
from itertools import combinations, permutations

# ==============================================================================
# 1. CUSTOM FUNCTIONS & EXECUTION CONTEXT
# ==============================================================================
def greet():
    return "Welcome to Python Modules"


def msg():
    return "Modules are fun..."


print("Function call:", greet())
print("Function call:", msg())
print("Current module name:", __name__)


# ==============================================================================
# 2. ARITHMETIC OPERATIONS & INPUT HANDLING
# ==============================================================================
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b if b != 0 else "provide a valid input"


print("Static Add (1 + 3):", add(1, 3))
print("Static Subtract (20 - 10):", subtract(20, 10))

# Interactive calculator demo
num_a = int(input("Enter the first number: "))
num_b = int(input("Enter the second number: "))

print("Addition is:", add(num_a, num_b))
print("Subtraction is:", subtract(num_a, num_b))
print("Multiplication is:", mul(num_a, num_b))
print("Division is:", div(num_a, num_b))


# ==============================================================================
# 3. RANDOM MODULE
# ==============================================================================
colors = ["red", "green", "blue"]

print("Random float (0.0 to 1.0):", random.random())
print("Random integer (1 to 10):", random.randint(1, 10))
print("Random choice from list:", random.choice(colors))
print("Random uniform float (1.0 to 10.0):", random.uniform(1, 10))


# ==============================================================================
# 4. ITERTOOLS MODULE
# ==============================================================================
numbers_list = [1, 2, 3, 4, 4, 4, 3, 3, 3, 2, 2]
print("Count of '3' in list:", numbers_list.count(3))

perm_list = list(permutations("abc", 2))
comb_list = list(combinations("abc", 2))

print("Permutations of 'abc':", perm_list)
print("Combinations of 'abc':", comb_list)


# ==============================================================================
# 5. PLATFORM MODULE
# ==============================================================================
print("System OS:", p.system())
print("OS Version:", p.version())
print("OS Release:", p.release())
print("Architecture Machine:", p.machine())
print("Bit Architecture:", p.architecture())
print("Processor:", p.processor())
print("Full Platform:", p.platform())
print("Python Version:", p.python_version())
print("Python Implementation:", p.python_implementation())
print("Uname Info:", dict(p.uname()._asdict()))
print("Node Name:", p.node())


# ==============================================================================
# 6. JSON MODULE
# ==============================================================================
data_dict = {"name": "ramu", "age": 23}
print("Original type:", type(data_dict).__name__)

json_str = json.dumps(data_dict)
print("JSON String:", json_str)
print("Converted type:", type(json_str).__name__)


# ==============================================================================
# 7. SYS MODULE
# ==============================================================================
sys.setrecursionlimit(100000)
print("Updated recursion limit:", sys.getrecursionlimit())

sample_list = [1, 3, 4, 3]
print("Memory size of list (bytes):", sys.getsizeof(sample_list))