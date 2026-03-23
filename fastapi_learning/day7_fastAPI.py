from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Request body model (VERY IMPORTANT)
class Student(BaseModel):
    name : str
    roll : int
    marks : int 


#Fake database 
students = []

#POST API -> add student 
@app.post("/student")
def add_student(student : Student):
    students.append(student)
    return {
        "message" : "Student added successfully",
        "data" : student 
    }

#GET API -> fetch all students 
@app.get ("/students")
def get_students():
    return students 
