"""


main.py
-------

this is the entryp point for the university management

RUN THIS FULE TO START THE PROGRAM:
    python main.py


this module will present a menu based interface, you type in a number to 
nagivate between options, and all data is loaded to and from .txt files

"""


from department import Department
import file_handler



#------------------------------------------------------------------------
# small functions to avoid repeating code
#------------------------------------------------------------------------

def print_opening():
    """ prints the opening text"""

    print(f"\n\n\n{'=' * 55}")
    print("   UNIVERSITY MANAGEMENT SYSTEM")
    print("      School of Programming ")
    print(f"{'=' * 55} \n\n")
   

def get_input(prompt, allow_empty=False):
    """ prompt the user for text input and strip spaces
     function would keep asking untill a non-empty input in givem """
    
    while True:
        value = input(prompt).strip()
        if value or allow_empty:
            return value
        print(" \n\n[!] Input Cannot Be Empty, Please Try Again.\n\n")


def get_float_input(prompt, min_val=0.0, max_val= 100.0):
    """ prompt the user for a floar value within a range
        this would also prevent user typing 'abc' instead of a number
    """
    
    while True:
        raw = input(prompt).strip()
    
        try:
            value = float(raw)
        
            if min_val <= value <= max_val:
                return value
        
            else:
                print(f"  \n\n[!] please enter a value between {min_val} and {max_val}.\n\n")
        
        except ValueError:
            # we land here if user typed an invalid value
            print(f" \n\n[!] '{raw}' is not a valid number. \nPlease try again!\n\n ")


def get_int_input(prompt, min_val=1, max_val=10):
    """ prompt for integer value within 1-10"""

    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        
            if min_val <= value <= max_val:
                return value
            
            else:
                print(f"  \n\n[!] please enter a value between {min_val} and {max_val}.\n\n")
        
        except ValueError:
            # we land here if user typed an invalid value
            print(f" \n\n[!] '{raw}' is not a valid integer. \nPlease try again! \n\n ")





#------------------------------------------------------------------------
# PRINTING MENU SCREENS 
#------------------------------------------------------------------------


def student_ment(dept):
    """ sub menu for all student related tasks"""

    while True:
        print("\n\n--- STUDENT MENU ------------------------\n")
        print("1. Add new student.")
        print("2. Remove a student")
        print("3. View all students")
        print("4. View student transcript")
        print("0. Back to main menu")
        print("---------------------------------------------")
print("\n\n--- STUDENT MENU ------------------------\n")
print("1. Add new student.")
print("2. Remove a student")
print("3. View all students")
print("4. View student transcript")
print("0. Back to main menu")
print("---------------------------------------------\n\n")

