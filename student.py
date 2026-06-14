"""student module for simple university example"""


class Student():
    """represents a student with basic details."""



    def __init__(self, name, id):
        self.name = name 
        self.id = id

        self.courses={}


    def add_course(self, course_id):
        self.courses[course_id] = None 

    def add_mark(self, course_id, mark):
        self.courses[course_id] = mark

    def get_gpa(self):  
        #to get gpa we have to implement weighted avg.
        # course should implement course.credid * student.course[course_id]
        pass 

   
    def __str__(self):
        s = "=================================\n"
        s += f"name: {self.name}, id:{self.id}\n"
        s += f"GPA: {self.get_gpa()}\n"
        s += f"Courses: {str(self.courses)}\n"
        s = "==================================\n "
def main():
    """this is a test function for student class"""

    print("test1: ")
    s1 = Student("John doe", 1001)
    s1.add_course("B100S032026")
    print(s1)


if __name__ == "__main__":
    main()