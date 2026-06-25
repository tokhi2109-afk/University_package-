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
COURSES_FILE = "courses.txt"
LECTURERS_FILE = "lecturers.txt"



#---------------------------------------------------------------------------------
# SAVE FUNCTIONS : 
#---------------------------------------------------------------------------------


def save_students(students_dict):
    """ write all student records to students.txt """

    
    try:
        # "w" = write mode. overwrites the file each time we save
        with open(STUDENTS_FILE, "w") as f:
            for student in students_dict.values():
                f.write(student.to_txt_row() + "\n")
        
        print(f" Students Data saved to '{STUDENTS_FILE}'.")
    
    except IOError as error:
        print(f" \n[!] Could Not Save Students Data: {error}\n")



def save_courses(courses_dict):
    """ write all course records to courses.txt"""


    try:
        with open(COURSES_FILE, "w") as f:
            for course in courses_dict.values():
                f.write(course.to_txt_row() + "\n")

        print(f" Cources Data Saved to '{COURSES_FILE}'.")

    
    except IOError as error:
            print(f" \n[!] Could Not Save Cources Data : {error}\n")




def save_lecturers(lecturers_dict):
    """ write all lecturer records to lecturers.txt"""


    try:
        with open(LECTURERS_FILE, "w") as f:
            for course in lecturers_dict.values():
                f.write(course.to_txt_row() + "\n")

        print(f" Lecturer Data Saved to '{LECTURERS_FILE}'.")

    
    except IOError as error:
            print(f" \n[!] Could Not Save Cources Data: {error}\n")



def save_all(department):
    """ saves students, courses and lecturers in one call """
     
    print(f" \nSaving all data..... ")

    save_students(department.students)
    save_courses(department.courses)
    save_lecturers(department.lecturers)



#---------------------------------------------------------------------------------
# Load FUNCTIONS : 
#---------------------------------------------------------------------------------


def load_students(department):
    """ read students.txt and populate the department with student objects."""
    try:
        with open(STUDENTS_FILE, "r") as f:
            for line in f:
                line = line.strip() # remove the \n at the end

                if not line:        # skip blank lines
                    continue 
                
                parts = line.split("|", 3) # split into at most 4 piece 
                if len(parts) < 3:         # skip broken lines 
                    continue

                student_id = parts[0]
                student_name = parts[1]
                email_id = parts[2]
                grades_str = parts[3] if len(parts) == 4  else ""

                student = Student(student_id, student_name, email_id)


                if grades_str:
                    for pair in grades_str.split(";"):
                        if ":" in pair:
                            course_id, grade = pair.split(":", 1)
                            try:
                                student.grades[course_id] = float(grade)
                            except ValueError:
                                pass 

                department.students[student_id] = student 
                
                print("here are my students")
                print(student)


        print(f"\n Loaded STUDENTS from file.")

    except FileNotFoundError:
        #no file yet - that's fine, just nothing to load
        pass
    except IOError as error:
        print(f" \n[!] could not load students: {error}\n")




def load_courses(department):
    """ read courses.txt and populate the department with course objects."""

    try:
        with open(COURSES_FILE, "r") as f:
            for line in f:
                line = line.strip() # remove the \n at the end

                if not line:        # skip blank lines
                    continue 
                
                parts = line.split("|", 4) # split into at most 4 piece 
                if len(parts) < 3:         # skip broken lines 
                    continue


                Course_id = parts[0]
                Course_name = parts[1]

                try:
                    credits = int(parts[2])
                except ValueError:
                    continue 

                lecturer_id = parts[3] if len(parts) > 3 and parts[3] else None
                students_str = parts[4] if len(parts) > 4 else ""

                course = Course(Course_id, Course_name, credits, lecturer_id)

                if students_str:
                    course.enrolled_students = [
                        s for s in students_str.split(";") if s 
                    ]
                
                department.courses[Course_id] = course 
        print(f" \nLoaded COURSES from file ")

 
    except FileNotFoundError:
        pass
    except IOError as error:
        print(f" \n[!] could not load Courses: {error}\n")




def load_lecturers(department):
    """ read lecturers.txt and populate the department with Lecturer objects."""

    try:
        with open(LECTURERS_FILE, "r") as f:
            for line in f:
                line = line.strip() # remove the \n at the end

                if not line:        # skip blank lines
                    continue 
                
                parts = line.split("|", 4) # split into at most 5 piece 
                if len(parts) < 4:         # skip broken lines 
                    continue


                lecturer_id = parts[0]
                name = parts[1]
                email_id = parts[2]
                specialisation = parts[3] 
                courses_str = parts[4] if len(parts) > 4 else ""

                lecturer = Lecturer(lecturer_id, name, email_id, specialisation)

                if courses_str:
                    lecturer.courses_taught = [
                        c for c in courses_str.split(";") if c
                    ]
                
                department.lecturers[lecturer_id] = lecturer 
        print(f" Loaded Lecturers from file ")

 
    except FileNotFoundError:
        pass
    except IOError as error:
        print(f" \n[!] could not load Lecturers: {error}\n")


def load_all(department):
    """ loads students, courses and lecturers all in one call"""


    print(f"\nLoading Saved Data....")
    load_students(department)
    load_lecturers(department)
    load_courses(department)
    