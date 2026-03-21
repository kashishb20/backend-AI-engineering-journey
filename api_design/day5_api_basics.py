"""
Day 5: API Basics

Learned:
- What is API
- Request and Response
- GET and POST methods
- Simulated API using Python functions
"""

# FAKE DATABASE (ACTS LIKE BACKEND DATA STORAGE)
students = [
    {"name": "Kavya","roll":1,"marks":50},
    {"name":"Ajay","roll":2,"marks" :87}
]

# GET API -> FETCH ALL STUDENTS 
def get_students():
    return students 

#GET API -> FETCH STUDENTS BY ROLL NUMBER
def get_student_by_roll(roll):
    for student in students :
        if student["roll"] == roll :
            return student 
    return "Student not found"

#POST API -> ADD A NEW STUDENT & HANDLING DUPLICATE ROLL NUMBERS 
def add_student(name,roll,marks):
    for student in students :
        if student["roll"] == roll:
            return "Roll number already exists"
        
    new_student = {
        "name": name ,
        "roll" : roll ,
        "marks" : marks
    }
    students.append(new_student)
    return "Student added successfully"


# -----Testing (stimulating api calls)------
print("All Students:")
print(get_students())

print("\nGet Student with Roll 3:")
print(get_student_by_roll(3))
print("\nGet Student with Roll 2:")
print(get_student_by_roll(2))

print("\nAdding New student :")
print(add_student("Ankita",3,99))
print(add_student("Sia",4,88))

print("\nAll Students after adding :")
print(get_students())