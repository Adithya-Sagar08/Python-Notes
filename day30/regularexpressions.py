# ------------------------------------------
# 1. Syntax Error Example (SyntaxError.py)
# ------------------------------------------
# Fixed missing colon after condition
a = 14
if a > 5:
    print("Hello")
else:
    print("Goodbye")


# ------------------------------------------
# 2. Logical Error Example (LogicalError.py)
# ------------------------------------------
# Fixed logic: Changed multiplication (*) to addition (+)
a = 10
b = 20
print("Addition of two numbers:", a + b)


# ------------------------------------------
# 3. Basic Exception Handling (ExceptionEg1.py)
# ------------------------------------------
a = 10
b = 2
print("Execution Started")
print(a + b)
print(a - b)
print(a * b)

try:
    print(a / 0)
except ZeroDivisionError:
    print("You can't divide a number by zero")

print("Execution Stopped")


# ------------------------------------------
# 4. Try-Except Flow (ExceptionEg2.py)
# ------------------------------------------
try:
    n = 10
    b = 2
    print("Execution Started")
    print(a + b)
    print(a - b)
    print(a / 0)
    print(a * b)
except ZeroDivisionError as e:
    print("Please don't divide by Zero")

print("Execution Stopped")


# ------------------------------------------
# 5. Handling Input Errors (ExceptionEg3.py)
# ------------------------------------------
try:
    print("Execution Started")
    a = int(input("Enter a number: "))
    print("hey")
except ValueError as e:
    print("Invalid Input, Please enter an integer")

print("Execution Stopped")


# ------------------------------------------
# 6. Multiple Except Blocks (ExceptionEg4.py)
# ------------------------------------------
try:
    print("Execution Started")
    a = int(input("Enter a value: "))
    b = int(input("Enter b value: "))
    result = a / b
    print("Result is:", result)
except ZeroDivisionError as e:
    print("You cannot divide by zero")
    print("Exception Message is:", e)
except ValueError as e:
    print("Invalid Input, Please enter a valid integer")
    print("Exception Message is:", e)

print("Execution Finished")


# ------------------------------------------
# 7. Try-Except-Else Clause (ExceptionEg5.py)
# ------------------------------------------
try:
    a = int(input("Enter a value: "))
    b = int(input("Enter b value: "))
    result = a / b
except ZeroDivisionError as e:
    print("Don't divide by zero")
    print("Exception Message is:", e)
else:
    print("No Exception in try block, due to that I am getting executed")
    print("Result:", result)

print("END")


# ------------------------------------------
# 8. Nested Try-Except (ExceptionEg6.py)
# ------------------------------------------
try:
    a = int(input("Enter a number: "))
    try:
        b = int(input("Enter another number: "))
        result = a / b
        print("Result is:", result)
    except ZeroDivisionError as e:
        print("Don't divide by zero")
except ValueError:
    print("Invalid Input, Please enter a valid integer")

print("END")


# ------------------------------------------
# 9. Default / Generic Except Block (DefaultExceptBlock.py)
# ------------------------------------------
try:
    a = int(input("Enter a number: "))
    print("Value of a:", a)
except ZeroDivisionError:
    print("Don't divide by zero")
except Exception as e:
    print("An error occurred:", e)

print("END")


# ------------------------------------------
# 10. The Finally Block (finally.py)
# ------------------------------------------
try:
    a = int(input("Enter a number: "))
    print("Value of a:", a)
except ZeroDivisionError as e:
    print("Don't divide by zero", e)
except ValueError as e:
    print("Invalid input:", e)
finally:
    print("I am always executed for you..")

print("END")


# ------------------------------------------
# 11. Inspecting Exception Objects (ExceptionType.py)
# ------------------------------------------
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    res = a / b
    print("result is ", res)
except ZeroDivisionError as e:
    print("Exception Type:", type(e).__name__)
    print("Exception Message:", e)
    print("Exception class name:", e.__class__.__name__)
    print("Exception Data:", type(e))