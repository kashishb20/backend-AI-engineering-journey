"""
DAY 4 
JSON is lightweigt data format used for data exchange 
between client and server , commonly used in APIs

JSON = JavaScript Object Notation
a standard way to store and transfer data

"""

import json
#CREATING PYTHON DICTIONARY
student = {
    "name": "Jiya" ,
    "roll" : 1 ,
    "marks" : 50 
}

#CONVERT PYTHON -> JSON STRING 
json_data = json.dumps(student)
print("JSON Data:" , json_data)

# CONVERT JSON -> PYTHON  
data = json.loads(json_data)
print("Name : " , data["name"])

#WRITE JSON TO FILE 
with open("students.json","w") as file:
    json.dump(student,file)

# READ JSON FROM FILE 
with open("students.json","r") as file :
    data = json.load(file)
   
print("From File : ",data)

