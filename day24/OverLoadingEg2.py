"""In Python, method overloading can be achieved
by using default parameters or arbitrary arguments (*args)."""


class Test:

    @staticmethod
    def add(*numbers):
        total = 0
        for num in numbers:
            total += num
        print(f"The Sum is {total}")


# --- Execution ---
t = Test()
t.add(10)
t.add(10, 20)
t.add(10, 20, 30)