import getpass
import os
import passwordcheck as pc
import student_record as sr
import datetime
from datetime import datetime



def menu():

    while True:
        print("\nMenu:")
        print("1. Add Student Record")      
        print("2. Update Student Record")
        print("3. Delete Student Record")
        print("4. View Student Record")
        print("5. Search Student Record")
        print("6. Top Students by Average Marks")
        print("7. Exit")
        try:
            choice=int(input("Enter your choice (1-7): "))
        except ValueError:
            print("Please enter a valid number between 1 and 6.")
            continue
        if choice==7:
            print("Exiting...")
            break
        elif choice<1 or choice>7:
            print("Invalid Choice")
            continue    
        elif choice==1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Add Student Record")
            sr.add_student()
            print("Student Record added successfully.")
        elif choice==2: 
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Update Student Record")
            sr.update_students()
            print("Student Record updated successfully.")

        elif choice==3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Delete Student Record")
            sr.delete_student()
            print("Student Record deleted successfully.")   
        elif choice==4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("View Student Record")
            sr.view_students()
            print("Student Record viewed successfully.")   
        elif choice==5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Search Student Record")
            sr.search_student()
            print("Student Record searched successfully.")  
        elif choice==6:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Top Students by Average Marks")
            sr.top_students()
            print("Top Students displayed successfully.")   


    

            

    


   





