"""
Day 9: CRUD Operations in FastAPI

Learned:
- Update data using PUT
- Delete data using DELETE
- Full CRUD operations
"""
from fastapi import FastAPI 
from fastapi import HTTPException
from pydantic import BaseModel 

app = FastAPI()

#Model 
class Student(BaseModel):
    name: str 
    roll: int
    marks: int 

#Fake database
students = []

#CREATE 
@app.post("/students")
def add_student(student: Student):
    students.append(student)
    return {"message":"Student added" , "data":student}

#READ 
@app.get("/students") #return all 
def get_students():
    return students 

# Get students by roll  
@app.get("/students/{roll}")#returns one  
def get_student_by_roll(roll: int):
    for s in students:
        if s.roll == roll:
            return s
    raise HTTPException(status_code=404, detail="Student not found")

#UPDATE 
@app.put("/students/{roll}")
def update_student(roll: int, updated_student: Student):
    for i, s in enumerate(students):
        if s.roll == roll:
            students[i] = updated_student
            return{"message": "Student updated","data": updated_student}
    return {"error":"student not found"}


#DELETE
@app.delete("/students/{roll}")
def delete_student(roll: int):
    for i, s in enumerate(students):
        if s.roll == roll:
            deleted = students.pop(i)
            return{"message": "Student deleted", "data" :deleted}
    return {"error": "student not found"}