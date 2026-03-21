"""
Day 3: Implemented file handling and data parsing in Python
Data handling helps save data and reuse it later 
file handling = data persistence  
"""

# WRITING TO FILE 
file = open("students.txt","w")
file.write("kashish,3,87\n")
file.write("Ankitaa,3,79\n")
file.close()

#READING FULL FILE
file = open("students.txt","r")
data=file.read()
print(data)
file.close()

#READING LINE BY LINE 
file = open("students.txt","r")
for line in file:
    print(line.strip())
file.close()

#CLASS DEFINITION 
class Student :
    def __init__(self,name,roll,marks):
        self.name = name 
        self.roll = int(roll)
        self.marks = int(marks)

    def display(self):
        print(f"{self.name},{self.roll},{self.marks}")

#CONVERT FILE DATA INTO OBJECTS 
file = open("students.txt","r")
students = []

for line in file:
    name,roll,marks = line.strip().split(",")

    s= Student(name,roll,marks)
    students.append(s)
file.close()

# DISPLAY OBJECTS 
for s in students:
        s.display()

#BEST PRACTICE (WITH OPEN)
with open("students.txt","r")as file:
        data =file.read()
        print (data)
