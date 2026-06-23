
"""
department.py
-------------
Defines the Department class, which acts as the central controller
for the University Management System.
 """


from student import Student
from course import Course
from lecturer import Lecturer

 

class Department:
    """this would the the main 'manager' class for this project
       it woudl hold the dictionaries of all students, courses, 
        and lecturers and would coordingate between them """
    

    def __init__(self, name):
        """initialises the Department"""

        self.name = name

        #use dictionaries(key -> object) for lookups by id 
        self.students = {}
        self.courses = {}
        self.lecturers = {}


#------------------------------------------------------------------
# student_management
#------------------------------------------------------------------

    #adding a student
    def add_student(self, student_id, student_name, email_id):
        
        #prevent duplicate id entry 
        if student_id in self.students:
            print(f"  \n[!] Student ID '{student_id}' already exists.\n")
            return None
        
        student = Student(student_id, student_name, email_id)
        self.students[student_id] = student
        print(f" \nStudent '{student_name} has been added with ID '{student_id}'.\n")
        return student


    #removing a student
    def remove_student(self, student_id):
        """ return true if successfully removed 
           """
        
        removed = self.students.pop(student_id) #removes and returns the item 
        print(f" \nStudent' {removed.student_name} removed.\n")

        return True 
    

    def get_student(self, student_id):
        """ search and return Student Objevt by ID 
        returns None if no ID found """

        return self.students.get(student_id)
    





    def add_course(self, course_id, course_name, credits):
        """ create and register a new course """

        if course_id in self.courses:
            print(f" \n[!] Course '{course_id}' already exists.\n")
            return None
            
        course = Course(course_id, course_name, credits)
        self.courses[course_id] = course
        print(f"  \nCourse '{course_name}' has been added.\n")
        return course 
    

    def remove_course(self, course_id):
        """ return true if successfully removed 
    """
        
        
        
        removed = self.courses.pop(course_id) #removes and returns the item 
        print(f" \nStudent' {removed.course_name} removed.\n")

        return True 


    def get_course(self, course_id):
        """ Search a couse by its ID"""
        return self.courses.get(course_id)
    


#------------------------------------------------------------------
# Lecturer_management
#------------------------------------------------------------------


    def add_lecturer(self, lecturer_id, name, email, specialisation):
        """Create and reguster a new lecturer"""


        if lecturer_id in self.lecturers:
            print(f" \n[!] Lecturer ID '{lecturer_id}' already exists\n")
            return None
        
        lecturer = Lecturer(lecturer_id, name, email, specialisation)
        self.lecturers[lecturer_id] = lecturer 
        print(f" \nLecturer '{name}' added with ID '{lecturer_id}\n")
        return lecturer 
    
    def remove_lecturer (self, lecturer_id):
        """ return true if successfully removed 
 """
        
      
        removed = self.lecturers.pop(lecturer_id) #removes and returns the item 
        print(f" \nStudent' {removed.name} removed.\n")

        return True 



    def get_lecturer(self, lecturer_id):
        """search a lecturer by ID """
        return self.lecturers.get(lecturer_id)
    

#------------------------------------------------------------------
# Cross_entry_operations
#------------------------------------------------------------------


     
    def course_enroll_student_(self, student_id, course_id):
        """enroll student in a course and return true if successful """


        student = self.get_student(student_id)
        course = self.get_course(course_id)

        
        return course.enroll_student(student_id)
    


    def course_assign_lecturer(self, lecturer_id, course_id):
        """ assign a lecturer to a course and update both objects 
        return true if successful """


        lecturer = self.get_lecturer(lecturer_id)
        course = self.get_course(course_id)




        
        course.assign_lecturer(lecturer_id)
        lecturer.assign_course(course_id)
        return True 
    

    def record_grade(self, student_id, course_id, grade):
        """ record a student's grade for a specific course
        return true if the grade was saved """

        student = self.get_student(student_id)
        course = self.get_course(course_id)
        
        if student_id not in course.enrolled_students:
            print(f" \n[!] Student '{student_id}' is not enrolled in '{course_id}\n")
            return False
        
        return student.add_grade(course_id, grade)
    


#------------------------------------------------------------------
# Listing and summary 
#------------------------------------------------------------------


    def list_all_students(self):
        """ print of all students in the department."""

        print(f"\n\n {'=' * 55}")
        print(f"  ALL STUDENTS - {len(self.students)}")
        print(f"{'=' * 55}")

        if not self.students:
            print("   No Students Registered Yet!")

        else:
            count = 1
            for student_id, student_obj in self.students.items():
                print(f" [{count}] {student_id}: {student_obj.student_name}")
                count += 1
            
        
        print(f"{'=' * 55}\n\n")
            
            
                

    def list_all_courses(self):
        """ print all courses in the department """
        print(f"\n{'=' * 55}")
        print(f"  ALL Courses - {len(self.courses)}")
        print(f"{'=' * 55}")
       
        if not self.courses:
            print(". No Courses Registered Yet.")
        
        else:
            count = 1
            for course_id, course in self.courses.items():
                print(f" [{count}] {course_id}: {course.course_name}")
                count += 1


    def list_all_lecturers(self):
      
        """ print all courses in the department """
        
        print(f"\n{'=' * 55}")
        print(f"  ALL LECTURERS - {len(self.lecturers)}")
        print(f"{'=' * 55}")
        
        if not self.lecturers:
            print(". No Lecturers Registered Yet.")
        
        else:
        
            count = 1
            for lecturer_id, lecturer in self.lecturers.items():
                print(f" [{count}] {lecturer_id}: {lecturer.name}")
                count += 1


    def department_summary(self):
        """ print a summary of the department """
        """ returns number of students, cources and lecturers """
        
        print(f"\n\n{'=' * 55}")
        print(f"  DEPARTMENT   : {self.name}")
        print(f"  Students     : {len(self.students)}")
        print(f"  Cources      : {len(self.courses)}")
        print(f"  Lecturers    : {len(self.lecturers)}")
        print(f"{'=' * 55} \n\n")

    def check_course(self, courses):
        def checker(user_input):
            # Checks if the input matches existing course id
            if user_input in courses:
                return True
            return False
        return checker 