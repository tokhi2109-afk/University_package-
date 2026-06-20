"""
course.py
---------
Defines the course class for the university package
this course has course id, name, credits and a list of enrolled students 
"""


class Course:
    """
    represents a course offered by the universiry 
    """

    def __init__(self, course_id, course_name, credits, lecturer_id = None):
        """
        initialises a new course object with course_id, course_name, credits, and optional lecturer_id
        """

        self.course_id = course_id
        self.course_name = course_name
        self.credits = credits
        self.lecturer_id = lecturer_id

        self.enrolled_students - [] # starts as an empty list 



#--------------------------------------------------------------
# METHOD 1 : enroll_student 
#--------------------------------------------------------------


    def enroll_student(self, student_id):
        """ adds a student to the course, returns true if the student
        was enrolled, false if the student was already enrolled
        """
        
        if student_id in self.enrolled_students:
            print(f" [!] student {student_id} is already enrolled in {self.course_id}")

            return False 
        
        self.enrolled_students.append(student_id)
        print(f" Student {student_id} enrolled in course {self.course_id}")

        return True

#--------------------------------------------------------------
# METHOD 2 :remove_student
#--------------------------------------------------------------


    def remove_student(self, student_id):
        """
        Removes a student from the course, returns true if the student was removed, 
        false if the student was not enrolled to begin with.
        """

        if student_id not in self.enrolled_students:
            print(f" [!] student {student_id} is not enrolled in course {self.course_id}")

            return False 
        
        self.enrolled_students.remove(student_id)
        print(f" Student {student_id} has been removed from the course {self.course_id}")

        return True



#--------------------------------------------------------------
# METHOD 3 : assign_lecturer 
#--------------------------------------------------------------


    def assign_lecturer(self, lecturer_id):
        """ assigns a lecturer to the course """

        self.lecturer_id = lecturer_id 
        print(f" Lecturer {lecturer_id} has been assigned to the course {self.course_id}")



#--------------------------------------------------------------
# METHOD 3 : get_enrolled_students
#--------------------------------------------------------------


    def get_count(self):
        """ Returns the number of students currently enrolled """

        return len(self.enrolled_students)


#--------------------------------------------------------------
# METHOD 4 : display info 
#--------------------------------------------------------------


    def display_info(self):
        """ this would print a summary of this course in the 
            diesired format """
        
        print(f" \n {'=' * 50 }")
        print(f"  Course   : {self.course_name}")
        print(f"  Code     : {self.course_id}")
        print(f"  Credits  : {self.credits}")

        lecturer_display = self.lecturer_id if self.lecturer_id else "Not Assigned"
        print(f"  Lecturer : {lecturer_display}")
        print(f"  Students : ({self.get_count()}):")


        if not self.enrolled_students:
            print("      - No students enrolled yet")
        else:
            # a loop to list all enrolled students 

            for code in self.enrolled_students:
                print(f" [{self.enrolled_students.index(code)}] {code}")

        print(f"{'=' * 50 }\n")             


#--------------------------------------------------------------
# METHOD 5 : to_txt_row 
#--------------------------------------------------------------


    def to_txt_row(self):

        """ to convert the course data into a line for a .txt file """

        students_str = ""
        for student_id in self.enrolled_students:
            students_str  = students_str + student_id + ":"

        if students_str:
            students_str = students_str[:-1] 
        
        lecturer_str = self.lecturer_id if self.lecturer_id else ""
        return f"{self.course_id}|{self.course_name}|{self.credits}|{lecturer_str}|{students_str}"

    def __str__(self):
        """Short readable description of the course."""
        return(
            f"Course [{self.course_id}] {self.course_name} "
            f" | Credits: {self.credits} | Enrolled Students: {self.get_count()}"

            )
