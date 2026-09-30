
# Importing Abstract Base Class tools
from abc import ABC, abstractmethod


# Base abstract class to represent any person in the university
class Person(ABC):

    def __init__(self, person_name, person_age):
        self._name = person_name
        self._age = person_age

    # Abstract method that child classes must implement
    @abstractmethod
    def get_role(self):
        pass

    # Common method to get name and age
    def get_basic_info(self):
        return f"Name: {self._name}, Age: {self._age}"

    # Method to get full information including role
    def get_details(self):
        return f"{self.get_basic_info()}, Role: {self.get_role()}"


# Student class that inherits from Person
class Student(Person):

    def __init__(self, student_name, student_age, student_id, course):
        super().__init__(student_name, student_age)
        self._student_id = student_id
        self._course = course

    # Role implementation
    def get_role(self):
        return "Student"

    # Additional information specific to student
    def get_student_info(self):
        return (
            f"{self.get_details()}, "
            f"Student ID: {self._student_id}, "
            f"Course: {self._course}"
        )


# Professor class that inherits from Person
class Professor(Person):

    def __init__(self, professor_name, professor_age, professor_id, department):
        super().__init__(professor_name, professor_age)
        self._p_id = professor_id
        self._department = department

    # Role implementation
    def get_role(self):
        return "Professor"

    # Additional information specific to professor
    def get_professor_info(self):
        return (
            f"{self.get_details()}, "
            f"Professor ID: {self._p_id}, "
            f"Department: {self._department}"
        )


# AdminStaff class that inherits from Person
class AdminStaff(Person):

    def __init__(
        self,
        staff_name,
        staff_age,
        staff_id,
        designation
    ):
        super().__init__(staff_name, staff_age)
        self._staff_id = staff_id
        self._designation = designation

    # Role implementation
    def get_role(self):
        return "Admin Staff"

    # Additional information specific to admin staff
    def get_staff_info(self):
        return (
            f"{self.get_details()}, "
            f"Staff ID: {self._staff_id}, "
            f"Designation: {self._designation}"
        )


# University class to manage list of people
class University:
    university_name = "Stanford University"

    def __init__(self):
        self.__people = []

    def add_person(self, person: Person):
        self.__people.append(person)

    def display_all(self):
        if not self.__people:
            print("No people registered yet.")
        else:
            for person in self.__people:
                print(person.get_details())

    @classmethod
    def get_university_name(cls):
        return cls.university_name

    @staticmethod
    def welcome_message():
        return "Welcome to the Stanford University Management System"


# Start of the program
print(University.welcome_message())
print("University:", University.get_university_name())

# Create University system object
university = University()


# Menu for user input
while True:
    print("\n--- University Menu ---")
    print("1. Register Student")
    print("2. Register Professor")
    print("3. Register Admin Staff")
    print("4. Display All People")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "0":
        print("Thank you! Exiting the system.")
        break

    elif choice == "1":
        # Input student details
        student_name_input = input("Enter Student Name: ")
        student_age_input = int(input("Enter Age: "))
        student_id_input = input("Enter Student ID: ")
        course_input = input("Enter Course Name: ")

        student = Student(
            student_name_input,
            student_age_input,
            student_id_input,
            course_input
        )

        university.add_person(student)
        print("Student Registered Successfully!")

    elif choice == "2":
        # Input professor details
        professor_name_input = input("Enter Professor Name: ")
        professor_age_input = int(input("Enter Age: "))
        professor_id_input = input("Enter Employee ID: ")
        department_input = input("Enter Department: ")

        professor = Professor(
            professor_name_input,
            professor_age_input,
            professor_id_input,
            department_input
        )

        university.add_person(professor)
        print("Professor Registered Successfully!")

    elif choice == "3":
        # Input admin staff details
        staff_name_input = input("Enter Staff Name: ")
        staff_age_input = int(input("Enter Age: "))
        staff_id_input = input("Enter Staff ID: ")
        designation_input = input("Enter Designation: ")

        admin_staff = AdminStaff(
            staff_name_input,
            staff_age_input,
            staff_id_input,
            designation_input
        )

        university.add_person(admin_staff)
        print("Admin Staff Registered Successfully!")

    elif choice == "4":
        # Display all people registered
        print("\n--- List of Registered People ---")
        university.display_all()

    else:
        print("Invalid option. Please choose again.")

name = input(...)
age = int(input(...))
