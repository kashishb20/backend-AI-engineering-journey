"""
Day 6: FastAPI Introduction

Learned:
- What is FastAPI
- Creating real APIs
- Running server
- GET request using FastAPI
"""

from fastapi import FastAPI

# Create app
app = FastAPI()


# Root API
@app.get("/")
def home():
    return {"message": "Hello, this is my first API"}


# GET API - all students
@app.get("/students")
def get_students():
    return [
        {"name": "Kavya", "roll": 1, "marks": 90},
        {"name": "Rahul", "roll": 2, "marks": 80}
    ]


# GET API - student by roll
@app.get("/students/{roll}")
def get_student(roll: int):
    students = [
        {"name": "Kavya", "roll": 1, "marks": 90},
        {"name": "Rahul", "roll": 2, "marks": 80}
    ]

    for student in students:
        if student["roll"] == roll:
            return student

    return {"error": "Student not found"}