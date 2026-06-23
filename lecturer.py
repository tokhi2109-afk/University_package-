"""
lecturer.py
-----------
Defines the Lecturer class for the University Management System.
A lecturer has an ID, name, specialisation, and a list of courses they teach.
"""


class Lecturer:
    """ represents a lecturer at the university """

    def __init__(self, lecturer_id, name, email, specialisation):
        """ initialises a new lecturer """

        self.lecturer_id = lecturer_id
        self.name = name 
        self.email = email 
        self.specialisation = specialisation

        # list of courses this lecturer is assigned to 
        self.courses_taught = [] 

#--------------------------------------------------------------
# METHOD 1 : assign_cource
#--------------------------------------------------------------


    def assign_course(self, course_id):
        """ assigns a course to this lecturer's teaching list
            it returns true if course was assigned, 
            flase if it was already assigned 
        """

        if course_id in self.courses_taught:
            print(f"\n[!] {self.name} is already assigned to the course {course_id}.\n")

            return False 
        
        self.courses_taught.append(course_id)
        print(f"\nCourse {course_id} has successfully been assigned to {self.name}\n")

        return True 


#--------------------------------------------------------------
# METHOD 2 : remove_course
#--------------------------------------------------------------


    def remove_course(self, course_id):
        """ removes course from lecturers list
            returns true if removed, false if couse was never assigned """
        
        if course_id not in self.courses_taught:
            print(f" \n[!] Course {course_id} is not assigned to {self.name}\n")

            return False
        
        self.courses_taught.remove(course_id)
        print(f" \nCourse {course_id} has been removed from {self.name}'s schedule\n")


#--------------------------------------------------------------
# METHOD 3 : get_workload
#--------------------------------------------------------------


    def get_workload(self):
        """ returns the number of courses taught by the lecturer """

        return len(self.courses_taught)
    

#--------------------------------------------------------------
# METHOD 4 : display_profile
#--------------------------------------------------------------


    def display_profile(self):
        """ Prints a formated profile for the lecturer """

        print(f"\n{'='* 50}")
        print(f"  LECTURER       : {self.name}")
        print(f"  ID.            : {self.lecturer_id}")
        print(f"  EMAIL          : {self.email}")
        print(f"  SPECIALISATION : {self.specialisation}")
        print(f"  COURSES TAUGHT : ({self.get_workload()}):")


        if not self.courses_taught:
            print("     -NO COURSES ASSIGNED YET!")

        else:
            #for loop to list each course taught with index
            for code in self.courses_taught:
                print(f" [{self.courses_taught.index(code)}] {code}")
        print(f"{'='* 50}\n")



#--------------------------------------------------------------
# METHOD 5 : to_txt_row
#--------------------------------------------------------------


    def to_txt_row(self):

        """ transforms lecturer data into a line for .txt file """   

        courses_str = ""
        for code in self.courses_taught:
            courses_str = courses_str + code + ";"

        if courses_str:
            courses_str = courses_str[:-1] # this drops the ";" in the end 

        return (
            f"{self.lecturer_id}|{self.name}|{self.email}|"
            f"{self.specialisation}|{courses_str}"
        )
    

    def __str__(self):
        """Short readable description of the course."""
        return(
            f"Lecturer [{self.lecturer_id}] {self.name} "
            f" | {self.specialisation} | Courses : {self.get_workload()}"

            )

