"""
main.py
-------
Entry point for the University Management System.

Run this file to start the program:
    python main.py

This module presents a menu-driven interface. The user types a number
to navigate between options. All data is saved to and loaded from CSV files.
"""

# We import our own modules — this is how Python organises code across files
from department import Department
import file_handler


# ===========================================================================
#  HELPER FUNCTIONS  (small utilities to avoid repeating code)
# ===========================================================================

def print_banner():
    """Print the application welcome banner."""
    print("\n" + "=" * 55)
    print("   🏛️  UNIVERSITY MANAGEMENT SYSTEM")
    print("   School of Computer ")
    print("=" * 55)


def get_input(prompt, allow_empty=False):
    """
    Prompt the user for text input and strip whitespace.

    This wraps the built-in input() to handle blank inputs gracefully.

    Args:
        prompt (str): The message shown to the user.
        allow_empty (bool): If False, keep asking until non-empty input given.

    Returns:
        str: The cleaned input string.
    """
    while True:
        value = input(prompt).strip()
        if value or allow_empty:
            return value
        print("  [!] Input cannot be empty. Please try again.")


def get_float_input(prompt, min_val=0.0, max_val=100.0):
    """
    Prompt the user for a float (decimal) value within a range.

    This is an example of EXCEPTION HANDLING — we catch the error
    that occurs when someone types "abc" instead of a number.

    Args:
        prompt (str): Display message.
        min_val (float): Minimum accepted value.
        max_val (float): Maximum accepted value.

    Returns:
        float: A valid number within the range.
    """
    while True:
        raw = input(prompt).strip()
        try:
            # float() converts a string like "85.5" to the number 85.5
            # If the string is "hello", float() raises a ValueError
            value = float(raw)

            if min_val <= value <= max_val:
                return value
            else:
                print(f"  [!] Please enter a value between {min_val} and {max_val}.")

        except ValueError:
            # We land here if float(raw) failed — e.g., user typed "abc"
            print(f"  [!] '{raw}' is not a valid number. Please try again.")


def get_int_input(prompt, min_val=1, max_val=10):
    """
    Prompt the user for an integer value within a range.

    Args:
        prompt (str): Display message.
        min_val (int): Minimum accepted value.
        max_val (int): Maximum accepted value.

    Returns:
        int: A valid integer within the range.
    """
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
            if min_val <= value <= max_val:
                return value
            else:
                print(f"  [!] Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print(f"  [!] '{raw}' is not a valid integer. Please try again.")


# ===========================================================================
#  MENU SCREENS
# ===========================================================================

def student_menu(dept):
    """
    Sub-menu for all student-related operations.

    Args:
        dept (Department): The active department object.
    """
    while True:
        print("\n── STUDENT MENU ──────────────────────────")
        print("  1. Add new student")
        print("  2. View all students")
        print("  3. View student transcript")
        print("  4. Remove student")
        print("  0. Back to main menu")
        print("──────────────────────────────────────────")

        choice = input("  Enter choice: ").strip()

        if choice == "1":
            print("\n  — Add New Student —")
            sid   = get_input("  Student ID  (e.g. S003): ")
            name  = get_input("  Full Name              : ")
            email = get_input("  Email Address          : ")
            dept.add_student(sid, name, email)

        elif choice == "2":
            dept.list_all_students()

        elif choice == "3":
            sid = get_input("  Enter Student ID: ")
            student = dept.get_student(sid)
            if student:
                student.display_transcript()
            else:
                print(f"  [!] No student found with ID '{sid}'.")

        elif choice == "4":
            sid = get_input("  Enter Student ID to remove: ")
            dept.remove_student(sid)

        elif choice == "0":
            break   # exit this while loop → return to main menu

        else:
            print("  [!] Invalid choice. Please enter a number from the menu.")


def course_menu(dept):
    """
    Sub-menu for all course-related operations.

    Args:
        dept (Department): The active department object.
    """
    while True:
        print("\n── COURSE MENU ───────────────────────────")
        print("  1. Add new course")
        print("  2. View all courses")
        print("  3. View course details")
        print("  4. Enrol student in course")
        print("  5. Record a student grade")
        print("  0. Back to main menu")
        print("──────────────────────────────────────────")

        choice = input("  Enter choice: ").strip()

        if choice == "1":
            print("\n  — Add New Course —")
            code    = get_input("  Course Code  (e.g. CS101)      : ")
            title   = get_input("  Course Title                   : ")
            credits = get_int_input("  Credits (1-10)             : ", 1, 10)
            dept.add_course(code, title, credits)

        elif choice == "2":
            dept.list_all_courses()

        elif choice == "3":
            code = get_input("  Enter Course Code: ")
            course = dept.get_course(code)
            if course:
                course.display_info()
            else:
                print(f"  [!] No course found with code '{code}'.")

        elif choice == "4":
            sid  = get_input("  Student ID  : ")
            code = get_input("  Course Code : ")
            dept.enrol_student_in_course(sid, code)

        elif choice == "5":
            print("\n  — Record Grade —")
            sid   = get_input("  Student ID  : ")
            code  = get_input("  Course Code : ")
            grade = get_float_input("  Grade (0-100): ", 0, 100)
            dept.record_grade(sid, code, grade)

        elif choice == "0":
            break

        else:
            print("  [!] Invalid choice.")


def lecturer_menu(dept):
    """
    Sub-menu for all lecturer-related operations.

    Args:
        dept (Department): The active department object.
    """
    while True:
        print("\n── LECTURER MENU ─────────────────────────")
        print("  1. Add new lecturer")
        print("  2. View all lecturers")
        print("  3. View lecturer profile")
        print("  4. Assign lecturer to course")
        print("  0. Back to main menu")
        print("──────────────────────────────────────────")

        choice = input("  Enter choice: ").strip()

        if choice == "1":
            print("\n  — Add New Lecturer —")
            lid   = get_input("  Lecturer ID  (e.g. L001): ")
            name  = get_input("  Full Name               : ")
            email = get_input("  Email Address           : ")
            spec  = get_input("  Specialisation          : ")
            dept.add_lecturer(lid, name, email, spec)

        elif choice == "2":
            dept.list_all_lecturers()

        elif choice == "3":
            lid = get_input("  Enter Lecturer ID: ")
            lecturer = dept.get_lecturer(lid)
            if lecturer:
                lecturer.display_profile()
            else:
                print(f"  [!] No lecturer found with ID '{lid}'.")

        elif choice == "4":
            lid  = get_input("  Lecturer ID : ")
            code = get_input("  Course Code : ")
            dept.assign_lecturer_to_course(lid, code)

        elif choice == "0":
            break

        else:
            print("  [!] Invalid choice.")


# ===========================================================================
#  MAIN FUNCTION  — the top-level menu
# ===========================================================================

def main():
    """
    Main function: initialise the department, load saved data,
    and display the top-level interactive menu.

    This is the function that runs when the program starts.
    """
    print_banner()

    # Create the department object
    dept = Department("School of Computer Science ")

    # Load any previously saved data from CSV files
    file_handler.load_all(dept)

    # ── Main Menu Loop ───────────────────────────────────────────────
    # This while True loop keeps the program running until user chooses 0
    while True:
        print("\n══ MAIN MENU ══════════════════════════════")
        dept.department_summary()
        print("  1. Student Management")
        print("  2. Course Management")
        print("  3. Lecturer Management")
        print("  4. Save all data")
        print("  0. Exit")
        print("═══════════════════════════════════════════")

        choice = input("  Enter choice: ").strip()

        if choice == "1":
            student_menu(dept)

        elif choice == "2":
            course_menu(dept)

        elif choice == "3":
            lecturer_menu(dept)

        elif choice == "4":
            file_handler.save_all(dept)

        elif choice == "0":
            # Ask user to confirm before quitting — good UX
            confirm = input("  Save before exiting? (y/n): ").strip().lower()
            if confirm == "y":
                file_handler.save_all(dept)
            print("\n  Goodbye! 👋\n")
            break   # exit the main while loop → program ends

        else:
            print("  [!] Invalid choice. Please enter 0–4.")


# ===========================================================================
#  ENTRY POINT
# ===========================================================================

# This is a Python convention:
#   __name__ == "__main__" is True only when you run THIS file directly.
#   If another file imports main.py, the block below will NOT run.
#   This prevents the menu from auto-launching on import.
if __name__ == "__main__":
    main()