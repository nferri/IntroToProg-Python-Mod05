# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using lists and files to work with data
# Change Log: (Who, When, What)
#   Natalie Ferri, 7/25/2024, Staring script and adding to the code
#   Natalie Ferri, 7/26/2024, Defining variables and importing json module
#   Natalie Ferri, 7/27/2024, Experimenting with exception handling
#   Natalie Ferri, 7/27/2024, Debugging the duplicating inputs -- issue with json reading from dictionary not list
# ------------------------------------------------------------------------------------------ #

import json

# Define the Data Constants

FILE_NAME: str = "Enrollments.json" #changed from csv to json

MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a student for a course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

# Define the Data Variables

student_first_name: str = "" # first name of a student entered by the user.
student_last_name: str = ""  # last name of a student entered by the user.
course_name: str = "" # name of a course entered by the user.
#json_data: str = "" # JavaScript Object Notation File -- NEW VARIABLE, but not used.
file = None  # reference to an opened file.
menu_choice: str = "" # choice made by the user.
student_data: dict = {} # student data dictionary
students: list = [] # a table of student data


# Multi-list function
# Extract and read the data from the JSON file
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()

except FileNotFoundError as e: # If FileNotFound print error
    print ("JSON file does not exist. Create JSON before running this script.\n")
    print ("-- Technical Error Message -- ")
    print (e, e.__doc__, type(e), sep='\n')

except Exception as e: # If other error print message
    print ("There was a non-specific error.\n")
    print ("-- Technical Error Message -- ")
    print (e, e.__doc__, type(e), sep='\n')

finally:
    if file.closed == False:
        file.close()

# Present and Process the data
while True:

    # Present the menu of choices
    print (MENU)
    menu_choice = input("Select an option: ") # Decides the logic loop
    print (" ") # Spacing
    
    # Input user data
    if menu_choice == "1":
        try: # Introduces user input exception handling
            
            student_first_name = input("Enter the student's first name in all caps: ")
            if not student_first_name.isupper():
                raise AttributeError("Error: The first name should be in all caps.\n") # If name is not in all caps, error

            student_last_name = input("Enter the student's last name in all caps: ")        
            if not student_last_name.isupper():
                raise AttributeError("Error: The last name should be in all caps.\n") # If name is not in all caps, error

            course_name = input("Enter course name: ") 

            # Dictionary for JSON
            student_data = {
                            "FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name,
                            }

            students.append(student_data)
            
            print(f"Student {student_data["FirstName"]} {student_data["LastName"]} is registered for {student_data["CourseName"]}.\n")        
            
        except AttributeError as e:
            print (e)  # Prints the custom message for AttributeError
            print ("-- Error Message -- \n")
            print ("WRITE YOUR NAME IN CAPS \n")
            print (e, e.__doc__, type(e), sep='\n')

        except Exception as e:
            print ("Error: There was a problem with your entered data. \n") # Prints the custom message for other errors
            print ("Please retry \n")
            print (e, e.__doc__, type(e), sep='\n')

        continue
    
# Present the current data
    elif menu_choice == "2":
        for student in students:
            print(f"{student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]} \n")
            # Printing logged rows in list

        continue

# Save the data to a file
    elif menu_choice == "3":
        try: 
            file = open(FILE_NAME, "w") # Writing to JSON
            json.dump(students, file) # Storing data to the JSON
            file.close()
            print ("The student data has been saved.")       
        
        except TypeError as e: # TypeError message
            print ("Please check that the data is a valid format \n")
            print ("-- Technical Error Message -- ")
            print (e, e.__doc__, type(e), sep='\n')
            
        except Exception as e: # Other error message
            print ("-- Error Message -- ")
            print ("Built-In Python error info: ")
            print (e, e.__doc__, type(e), sep='\n')
            
        finally: # Close JSON file
            if file.closed == False:
                file.close()

        continue

# Stop the loop
    elif menu_choice == "4":
        break  # Out of the loop

    else: # Reminder to only choose from the menu options
        print ("Please only choose option 1, 2, 3, or 4.")

# Signifies end of program
print ("Thank you for your input. Goodbye. \n")
