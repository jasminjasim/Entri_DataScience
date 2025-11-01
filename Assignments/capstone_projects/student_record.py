import datetime
import itertools as it
from datetime import datetime
def add_student():

    student_record = "student_records.txt"  
    name=input("Enter Student Name:")
    rollnumber=int(input("Enter Student Roll Number:"))
    age=int(input("Enter Student Age:"))        
    department=input("Enter Student Department:")
    mark1=int(input("Enter Student Mark 1:"))
    mark2=int(input("Enter Student Mark 2:"))
    mark3=int(input("Enter Student Mark 3:")
    )
    with open(student_record, "a") as s:
        s.write(f"{name},{rollnumber},{age},{department},{mark1},{mark2},{mark3},{datetime.now()}\n")

 
def view_students():
    student_record = "student_records.txt"  
    with open(student_record, "r") as s:
        records = s.readlines()
        for record in records:
            print(record.strip())
def update_students():
    student_record = "student_records.txt"  
    rollnumber=int(input("Enter Student Roll Number to Update:"))
    name=input("Enter New Student Name :")
    age=input("Enter New Student Age :")        
    department=input("Enter New Student Department :")
    mark1=input("Enter New Student Mark 1 :")
    mark2=input("Enter New Student Mark 2 :")
    mark3=input("Enter New Student Mark 3 :")
    with open(student_record, "r") as s:
        records = s.readlines()
    with open(student_record, "w") as s:
        for record in records:
            rec = record.strip().split(',')
            if int(rec[1]) == rollnumber:
                s.write(f"{name},{rollnumber},{age},{department},{mark1},{mark2},{mark3},{datetime.now()}\n")
            else:
                s.write(record)

def delete_student():
    student_record = "student_records.txt"  
    rollnumber=int(input("Enter Student Roll Number to Delete:"))
    with open(student_record, "r") as s:
        records = s.readlines()
    with open(student_record, "w") as s:
        for record in records:
            rec = record.strip().split(',')
            if int(rec[1]) != rollnumber:
                s.write(record)
def search_student():   
    student_record = "student_records.txt"  
    name = input("Enter Student Name to Search (leave blank if not searching by name): ").strip()
    department = ""
    if not name:
        department = input("Enter Student Department to Search: ").strip() 
    with open(student_record, "r") as s:
        records = s.readlines()
        found = False
        for record in records:
            rec = record.strip().split(',')    
            if name and rec[0] == name:
                print(record.strip())
                found = True
            elif department and rec[3] == department:
                print(record.strip())
                found = True
        
        if not found:
            print("Student Record not found.")
def top_students():
    student_record = "student_records.txt"  
    with open(student_record, "r") as s:
        records = s.readlines()
        top_student = None
        top_average = -1
        for record in records:
            rec = record.strip().split(',')
            marks = list(map(int, rec[4:7]))
            average = sum(marks) / len(marks)
            if average > top_average:
                top_average = average
                top_student = record.strip()
        if top_student:
            print("Top Student Record:")
            print(top_student)
        else:
            print("No student records found.")