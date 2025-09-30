import getpass
import os
import passwordcheck as pc
import capstone_1 as c
import datetime 

# Login System
USERNAME=pc.USERNAME
PASSWORD=pc.PASSWORD

username=input("Enter username: ")
password=getpass.getpass("Enter password: ")

if username==USERNAME and password==PASSWORD:
    print("Login Successfull")
    print(f"Welcome To Student Management System, {username}")
    try:
        c.menu()
    except Exception as e:
        print(f"An error occurred while accessing the student management system: {e}")
elif username!=USERNAME and password==PASSWORD:
    print("Invalid Username")
elif username==USERNAME and password!=PASSWORD:
    print("Invalid Password")
else:
    print("Invalid Username and Password")