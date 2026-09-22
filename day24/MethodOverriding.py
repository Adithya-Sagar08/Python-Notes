# --- Base Class (Parent) ---
class Animal:
    def make_sound(self):
        return "Some generic animal sound"


# --- Derived Classes (Children overriding the parent method) ---
class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


# --- Overriding with super() to extend parent functionality ---
class LoudDog(Dog):
    def make_sound(self):
        # Calls the parent's (Dog) method and adds extra behavior
        parent_sound = super().make_sound()
        return f"{parent_sound.upper()} (LOUDLY!)"


# --- Execution ---
generic_animal = Animal()
dog = Dog()
cat = Cat()
loud_dog = LoudDog()

print("Animal:  ", generic_animal.make_sound())  # Some generic animal sound
print("Dog:     ", dog.make_sound())             # Woof! Woof!
print("Cat:     ", cat.make_sound())             # Meow!
print("LoudDog: ", loud_dog.make_sound())        # WOOF! WOOF! (LOUDLY!)