"""
student.py

Defines the student class for the university package

"""


class Student():
    """ Represents a student enrolled in the university system"""

    def __init__(self, student_id, student_name, email_id ):
        
        """ 
        initialises a new student object with student_id,
          student_name, and email_id
        
        """

        # store the basis details as attributes of them object 
        self.student_id = student_id
        self.student_name = student_name
        self.email_id = email_id

        # Grades is a dictionary: {course_id: grade}
        # we start with an empty dict - grades are added later.
        self.grades = {}

#--------------------------------------------------------------

# METHOD 1 : add_grade


    def add_grade(self, course_id, grade):  
    
        """ adds a grade for a course to the student record 
         it returns true if the grade was saved, false if the input was invalid 
        """
    
        if  0 <= grade <= 100:
            self.grades[course_id] = grade
            return true 
        else:
            print(f" [!] Invalid grade '{grade}' must be between 0 and 100")
            return false

    #--------------------------------------------------------------

# Method 2 : get_avg_grade

    def get_avg_grade(self):
        """
        will calculate avg grade across all courses for the student
        
        returns average grade across all courses, or None if no grades are available
        """

        # to avoid division by zero, we check if there are any grades first
        if not self.grades:
            return None
        
        
        total_grades = sum(self.grades.values())
        count_of_grades = len(self.grades)
        
        # we round the result to 2 decimal places for better readability
        return round(total_grades / count_of_grades, 2)
    

    #--------------------------------------------------------------

    # METHOD 3 : Get_grade_letter 


    def get_grade_letter(self, avarage = None):
        """
        Converts a numeric grade for a course into a letter (A, B, C, D, F)
        
        """

        score = avarage if avarage is not None else self.get_avg_grade()


        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:      
            return "D"
        else:
            return "F"  
        
#-------------------------------------------------------------- 

# METHOD 4 : display_transcript


    def display_transcript(self):
        """
        Print a transcript for the student, showing cource, grades, 
        overall avg etc.

        """

        print(f"\n{'=' * 50 }")
        print(f" TRANSCRIPT -- {self.student_name} ({self.student_id})")
        print(f" EMAIL : {self.email_id}")
        print(f"\n{'=' * 50 }")


        if not self.grades:
            print("NO GRADES AVAILABLE")

        else:
            for course_id, grade in self.grades.items():
                letter = self.get_grade_letter(grade)
                
                # TO create spacing between the columns we multiply space(' ') 
                # by a number to get the desired spacing 
                print(f" Course ID : {(' ') * 10} Grade : {(' ') * 10} Grade Letter : ")
                print(f" {(' ') * 3} {course_id} {(' ') * 15} {grade} {(' ') * 20} {letter}")


        avarage = self.get_avg_grade()
        letter = self.get_grade_letter()
        print(f"\n{'-' * 50 }")
        print(f" Avarage Grade : {avarage}   -> ({letter})")
        print(f"{'=' * 50 }")

#--------------------------------------------------------------

# METHOD 5 : to_txt_row


    def to_txt_row(self):
        """
        to convert the student data into a line for a .txt file 
        """

        # we will use | as the separator instead of comma 

        grades_str = 
        