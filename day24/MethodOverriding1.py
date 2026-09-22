"""
Here, the parent class method gets overridden 
by the child class method.
"""


class Media:

    def show(self):
        print("This is the Media Class")


class Book(Media):

    def show(self):
        print("We read books")


# --- Execution ---
b = Book()
b.show()  # Output: We read books