class Book:

    def __init__(self, pages):
        self.pages = pages

    def __str__(self):
        return str(self.pages)
        # This will get executed just like __init__() constructor
        # whenever an object is created this is going to get invoked automatically

    def __add__(self, other):
        return Book(self.pages + other.pages)
        # We need to return the object to add more than two values
        # because it only take two parameters

    def __mul__(self, other):
        return Book(self.pages * other.pages)


b1 = Book(100)
b2 = Book(200)
b3 = Book(300)
print(b1 + b2 + b3)
print(b1 * b2 * b3)  # Inorder to carry this operation we use MAGIC METHODS