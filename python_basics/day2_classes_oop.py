"""
Day2: Implemented classes &  methods
Concepts covered:
- Class creation
- Constructor (__init__)
- Instance methods
- Updating object state
- Basic logic (pass/fail)
"""
class Student :

    #constructor 
    def __init__(self,name,roll,marks):
        self.name = name 
        self.roll = roll
        self.marks = marks 

    #Methods to display details 
    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll: {self.roll}")
        print(f"Marks: {self.marks}")
        print(f"Passed: {self.is_passed()}")
    #method to update marks 
    def update_marks(self,new_marks):
        self.marks = new_marks

    #Method to tell pass or not 
    def is_passed(self):
        return self.marks >= 40

#Creating objects 
s1 = Student("Kashish",1,88)
s2 = Student("Ankita",2,90)

#display  data (method 1)
# s1.display()
# print("-----")
# s2.display()

#display  data (method 2)
students = [s1,s2]
for s in students :
    print ("-----")
    s.display()
 #   print(f"Passed : {s.is_passed()}")
#update marks 
s1.update_marks(96)

print("After updating marks : ")
s1.display()
