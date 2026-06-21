"""
file_handler.py

This module saves and loads Students, Courses, and Lectures to/from
plain .txt files.

Each record is stored as a line in the file.

"""


from student import Student
from course import Course 
from lecturer import Lecturer 


STUDENTS_FILE = "students.txt"
COURSES_FILE = "cources.txt"
LECTURERS_FILE = "lecturers.txt"



#---------------------------------------------------------------------------------
# SAVE FUNCTIONS : 
#---------------------------------------------------------------------------------


def save_students(students_dict):
    """ write all student records to students.txt """

    
    try:
        # "w" = write mode. overwrites the file each time we save
        with open(STUDENTS_FILE, "W") as f:
            for student in students_dict.values():
                f.write(student.to_txt_row() + "\n")
        print(f" Students Data saved to '{STUDENTS_FILE}'.")
    
    except IOError as error:
        print(f" [!] Could Not Save Students Data: {error}")



def save_courses(courses_dict):
    """ write all course records to courses.txt"""


    try:
        with open(COURSES_FILE, "w") as f:
            for course in courses_dict.values():
                f.write(course.to_txt_row() + "\n")

        print(f" Cources Data Saved to '{COURSES_FILE}'.")

    
    except IOError as error:
            print(f" [!] Could Not Save Cources Data : {error}")




def save_lecturers(lecturers_dict):
    """ write all lecturer records to lecturers.txt"""


    try:
        with open(LECTURERS_FILE, "w") as f:
            for course in lecturers_dict.values():
                f.write(course.to_txt_row() + "\n")

        print(f" Lecturer Data Saved to '{COURSES_FILE}'.")

    
    except IOError as error:
            print(f" [!] Could Not Save Cources Data: {error}")



def save_all(department):
    """ saves students, courses and lecturers in one call """
     
    print(f"\n Saving all data..... ")

    save_students(department.students)
    save_courses(department.courses)
    save_lecturers(department.lecturers)



#---------------------------------------------------------------------------------
# Load FUNCTIONS : 
#---------------------------------------------------------------------------------
