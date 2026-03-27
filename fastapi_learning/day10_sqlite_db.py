"""
Day 10: FastAPI with SQLite Database

Learned:
- How to connect database
- Store data permanently
- Use SQL queries
"""

from fastapi import FastAPI , HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# Connect to database (create file if not exists)
conn = sqlite3.connect("Student.db", check_same_thread=False)
cursor = conn.cursor()

#create table
cursor.execute(""" CREATE TABLE IF NOT EXISTS students (roll INTEGER PRIMARY KEY , name TEXT , marks INTEGER)""")
conn.commit()

#model
class Student(BaseModel):
    name: str
    roll: int 
    marks: int

#HOME
@app.get("/")
def home():
    return {"message":"Database API running"}

#CREATE 
@app.post("/students")
def add_student(student: Student):
    try:
        cursor.execute("INSERT INTO students (roll, name, marks) VALUES (?, ?, ?)",
            (student.roll, student.name, student.marks))
        conn.commit()
        return{"message":"Student added "}
    except : 
        raise HTTPException(status_code=400, detail="Student already exists")



# READ ALL
@app.get("/students")
def get_students():
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    students = []
    for row in data:
        students.append({
            "roll": row[0],
            "name": row[1],
            "marks": row[2]
        })

    return students

#READ ONE
@app.get("/students/{roll}")
def get_student_by_roll(roll: int):
    cursor.execute("SELECT * FROM students WHERE roll=?", (roll,))
    row = cursor.fetchone()

    if row:
        return {"roll": row[0], "name": row[1], "marks": row[2]}
    raise HTTPException(status_code=404, detail="Student not found")


@app.get("/students/{roll}")
def get_student(roll: int):
    cursor.execute("SELECT * FROM students WHERE roll=?", (roll,))
    row = cursor.fetchone()

    if row:
        return {"roll": row[0], "name": row[1], "marks": row[2]}
    raise HTTPException(status_code=404, detail="Student not found")