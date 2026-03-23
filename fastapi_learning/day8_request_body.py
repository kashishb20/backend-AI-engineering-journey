"""
Day 8: Request Body in FastAPI

Learned:
- What is request body
- How FastAPI handles JSON input
- Pydantic models

"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Pydantic model (defines structure of incoming data)
class Student(BaseModel):
    name: str
    roll: int
    marks: int

#Fake database 
students=[]

# GET API -> check server working
@app.get("/")
def home():
    return{"message":"API is running :) "}

# POST API -> add student using request body
@app.post("/add_student")
def add_student(student: Student):
    students.append(student)
    return {
        "message": "Student added successfully",
        "data": student
    }

# POST API -> add student using request body
@app.get("/students")
def get_students():
    return students