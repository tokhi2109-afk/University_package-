"""
lecturer.py
-----------
Defines the Lecturer class for the University Management System.
A lecturer has an ID, name, specialisation, and a list of courses they teach.
"""


class lecturer:
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
