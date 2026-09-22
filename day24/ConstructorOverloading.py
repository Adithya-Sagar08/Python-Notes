# Option 1: Default arguments (Most common & Pythonic)
class TestDefault:
    def __init__(self, a=None):
        if a is None:
            print("No arguments constructor")
        else:
            self.a = a
            print(f"One argument constructor with value: {self.a}")


# Option 2: Variable arguments (*args)
class TestArgs:
    def __init__(self, *args):
        if len(args) == 0:
            print("No arguments constructor")
        elif len(args) == 1:
            self.a = args[0]
            print(f"One argument constructor with value: {self.a}")
        else:
            print(f"Multiple arguments constructor with values: {args}")


# Option 3: Class methods (Alternative constructors)
class TestClassMethod:
    def __init__(self, a):
        self.a = a
        print(f"One argument constructor with value: {self.a}")

    @classmethod
    def empty(cls):
        print("No arguments constructor")
        return cls(a=None)


# --- Execution ---
print("=== Testing Default Arguments ===")
t1 = TestDefault()
t2 = TestDefault(10)

print("\n=== Testing Variable Arguments (*args) ===")
t3 = TestArgs()
t4 = TestArgs(10)
t5 = TestArgs(10, 20, 30)

print("\n=== Testing Class Methods ===")
t6 = TestClassMethod.empty()
t7 = TestClassMethod(10)