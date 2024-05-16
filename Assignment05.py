# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   Alex Kover, 5/14/24, Created Script
# ------------------------------------------------------------------------------------------ #
import json  # imports json module

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
json_data: str = ""  # Holds data to write to json file
student_data: dict = {}  # one row of student data where all keys are strings
students: list = []  # a table of student data
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")  # reads file
    students = json.load(file)   # loads json file data into dict file
    file.close()
except Exception as E:  # error handling
    print("An error occurred when reading the file.")
    print("Check that the file exists and is in json format.")
    print("---Error Details---")
    print(E.__doc__)
    print(E.__str__())
finally:
    if file.closed == False:  # closes file if not already closed
        file.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha(): # catches if user enters a number in a name
                raise ValueError("The student's name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha(): # catches if user enters a number in a name
                raise ValueError("The student's name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name, "LastName": student_last_name, "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as E:  # gives user value error details
            print(E)
            print("---Error Details---")
            print(E.__doc__)
            print(E.__str__())
        except Exception as E: # gives user general error message
            print("There was an error with the data you entered.")
            print("---Error Details---")
            print(E.__doc__)
            print(E.__str__())
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":

        try:
            file = open(FILE_NAME, "w") # opens json file in write mode
            json.dump(students,file)  # dumps data from students dict to file
            file.close()
            print("The following data was saved to file!")
            for student in students:  # displays data that was saved to file
                print(f"Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}")
        except Exception as E:
            if file.closed == False:
                file.close()
            print("There was an error writing data to the file.")  # error message to user if writing to file fails
            print("Check that the file is not currently open in another program.")
            print("---Error Details---")
            print(E.__doc__)
            print(E.__str__())
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
