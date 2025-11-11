#Matthew Rozendaal
#11/10/25
# Module 8, Exercise 2

# This program loads a class list JSON into memory and displays it
# It then adds a new student to the list 
# Displays the updated list
# Then saves the updated list back to the JSON file
import json
import os

def display_class_list(class_list):
    for student in class_list:
        print(f"{student['L_Name']}, {student['F_Name']}  - ID: {student['Student_ID']}, Email: {student['Email']}")

def create_new_student(firstName, lastName, studentID, email):
    return {
        "F_Name":firstName,
        "L_Name": lastName,
        "Student_ID": studentID,
        "Email": email
    }

def main():
    current_directory = os.getcwd()
    # Load the class list from the JSON file
    with open(current_directory +"\\student.json", "r") as file:
        class_list = json.load(file)

    # Display the current class list
    display_class_list(class_list)
    print("This is the original Student list")

    # Add a new student to the list
    class_list.append(create_new_student("Matthew", "Rozendaal", 9878778, "mrozendaal@my365.bellevue.edu"))

    # Display the updated class list
    display_class_list(class_list)

    print("This is the updated Student list")

    # Save the updated class list back to the JSON file
    with open("student.json", "w") as file:
        json.dump(class_list, file)
    
    print("Json has been updated")

if __name__ == "__main__":
    main()

