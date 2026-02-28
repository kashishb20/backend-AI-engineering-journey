"""
Day 1: Functions and OOP Basics
Focus: Clean function design, error handling, and basic class structure
"""

# Function 1: Calculate GPA
def calculate_gpa(grades):
    if not grades:
        raise ValueError("Grades list cannot be empty")

    total = sum(grades)
    return round(total / len(grades), 2)


# Function 2: Validate email format (basic)
def validate_email(email):
    if "@" in email and "." in email:
        return True
    return False


# Function 3: Safe division with error handling
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"


# Class Example
class Student:
    def __init__(self, name, semester, grades):
        self.name = name
        self.semester = semester
        self.grades = grades

    def get_gpa(self):
        return calculate_gpa(self.grades)

    def introduce(self):
        return f"Hi, I am {self.name}, currently in semester {self.semester}."


# Testing the code
if __name__ == "__main__":
    student = Student("Kashish", 4, [8.8, 7.8, 9.0])
    print(student.introduce())
    print("GPA:", student.get_gpa())
    print("Email Valid:", validate_email("test@email.com"))
    print("Division Result:", safe_divide(10, 2))