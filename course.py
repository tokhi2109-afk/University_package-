"""course module represents courses"""


class Course():
    """represents courses"""
    def __init__(self, name, id, credit = 1):

        self.name = name
        self.id = id 
        self.credit = credit 


        self.students = {} # id of students in the class

    def add_student(self, student_id, mark = None):
        
        self.students[student_id] = Mark 

    def get_avg_mark(self):
         num = 0 
         sum = 0 
         
        for k, v in self.students:
           

            if v :
                sum =+ v 
                num += 1
        if num:
            return sum / num
         
        return None

    def __str__(self):
        s = "=================================\n"
        s += f"name: {self.name}, id:{self.id}\n"
        s += f"GPA: {self.get_gpa()}\n"
        s += f"Courses: {str(self.courses)}\n"
        s = "==================================\n "
