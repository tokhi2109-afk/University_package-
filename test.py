"""
main.py
-------

this is the entry point for the university management

RUN THIS FILE TO START THE PROGRAM:
    python main.py

this module will present a menu based interface, you type in a number to
navigate between options, and all data is loaded to and from .txt files

during the navigation into the menu enter // to go back to the sub menu
"""


from department import Department
import file_handler


# ---------------------------------------------------------------------------
# small functions to avoid repeating code
# ---------------------------------------------------------------------------

def print_opening():
    """prints the opening text"""
    print(f"\n\n\n{'=' * 55}")
    print("   UNIVERSITY MANAGEMENT SYSTEM")
    print("      School of Programming ")
    print(f"{'=' * 55} \n\n")


def get_input(prompt, allow_empty=False):
    """
    Prompt the user for text input and strip whitespace.
    """
    while True:
        value = input(prompt).strip()
        if value or allow_empty:
            return value
        print("  [!] Input cannot be empty. Please try again.")


def get_float_input(prompt, min_val=0.0, max_val=100.0):
    """
    Prompt the user for a float (decimal) value within a range.
    Exception handling catches non-numeric input.
    """
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
            if min_val <= value <= max_val:
                return value
            else:
                print(f"  [!] Please enter a value between {min_val} and {max_val}.")
        except ValueError:
            print(f"  [!] '{raw}' is not a valid number. Please try again.")


def get_int_input(prompt, min_val=1, max_val=10):
    """
    Prompt the user for an integer value within a range.
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
    // at any prompt cancels the current operation and returns to this menu.
    """
    while True:
        print("\n-- STUDENT MENU ------------------------------------------")
        print("  1. Add new student")
        print("  2. View all students")
        print("  3. View student transcript")
        print("  4. Remove student")
        print("  0. Back to main menu")
        print("----------------------------------------------------------")

        choice = input("  Enter choice: ").strip()

        if choice == "1":
            print("\n  - Add New Student -")

            sid = get_input("  Student ID  (e.g. S003): ").upper()
            if sid == "//":
                continue          # // typed - skip rest, loop back to show menu

            name = get_input("  Full Name              : ").lower()
            if name == "//":
                continue

            email = get_input("  Email Address          : ").lower()
            if email == "//":
                continue

            dept.add_student(sid, name, email)

        elif choice == "2":
            dept.list_all_students()

        elif choice == "3":
            while True:
                sid = get_input("  Enter Student ID: ").upper()
                if sid == "//":
                    break         # exit inner loop, menu redraws
                student = dept.get_student(sid)
                if student:
                    student.display_transcript()
                    break
                else:
                    print(f"  [!] No student found with ID '{sid}'.")

        elif choice == "4":
            while True:
                sid = get_input("  Enter Student ID to remove: ").upper()
                if sid == "//":
                    break
                student = dept.get_student(sid)
                if student:
                    dept.remove_student(sid)
                    break
                else:
                    print(f"  [!] No student found with ID '{sid}'.")

        elif choice == "0":
            break                 # exit student menu, back to main menu

        else:
            print("  [!] Invalid choice. Please enter a number from the menu.")


def course_menu(dept):
    """
    Sub-menu for all course-related operations.
    // at any prompt cancels the current operation and returns to this menu.
    """
    while True:
        print("\n-- COURSE MENU -------------------------------------------")
        print("  1. Add new course")
        print("  2. View all courses")
        print("  3. View course details")
        print("  4. Enrol student in course")
        print("  5. Record a student grade")
        print("  6. Remove a course")
        print("  0. Back to main menu")
        print("----------------------------------------------------------")

        choice = input("  Enter choice: ").strip()

        if choice == "1":
            print("\n  - Add New Course -")

            code = get_input("  Course Code  (e.g. CS101): ").upper()
            if code == "//":
                continue

            title = get_input("  Course Title             : ").lower()
            if title == "//":
                continue

            credits = get_int_input("  Credits (1-10)           : ", 1, 10)
            dept.add_course(code, title, credits)

        elif choice == "2":
            dept.list_all_courses()

        elif choice == "3":
            while True:
                code = get_input("  Enter Course Code: ").upper()
                if code == "//":
                    break
                course = dept.get_course(code)
                if course:
                    course.display_info()
                    break
                else:
                    print(f"  [!] No course found with code '{code}'.")

        elif choice == "4":
            # Step 1 - keep asking until we get a valid student ID or //
            sid = None
            while True:
                sid = get_input("  Enter Student ID: ").upper()
                if sid == "//":
                    break
                student = dept.get_student(sid)
                if student:
                    break
                else:
                    print(f"  [!] No student found with ID '{sid}'.")

            if sid == "//":
                continue          # cancelled at student step, back to menu

            # Step 2 - keep asking until we get a valid course code or //
            while True:
                code = get_input("  Enter Course ID: ").upper()
                if code == "//":
                    break
                course = dept.get_course(code)
                if course:
                    dept.course_enroll_student_(sid, code)
                    break
                else:
                    print(f"  [!] No course found with ID '{code}'.")

        elif choice == "5":
            print("\n  - Record Grade -")

            # Step 1 - valid student
            sid = None
            while True:
                sid = get_input("  Enter Student ID: ").upper()
                if sid == "//":
                    break
                student = dept.get_student(sid)
                if student:
                    break
                else:
                    print(f"  [!] No student found with ID '{sid}'.")

            if sid == "//":
                continue

            # Step 2 - valid course
            code = None
            while True:
                code = get_input("  Enter Course ID: ").upper()
                if code == "//":
                    break
                course = dept.get_course(code)
                if course:
                    break
                else:
                    print(f"  [!] No course found with ID '{code}'.")

            if code == "//":
                continue

            # Step 3 - grade
            grade = get_float_input("  Grade (0-100): ", 0, 100)
            dept.record_grade(sid, code, grade)

        elif choice == "6":
            print("\n  - Remove a Course -")
            while True:
                code = get_input("  Enter Course ID: ").upper()
                if code == "//":
                    break
                course = dept.get_course(code)
                if course:
                    dept.remove_course(code)
                    break
                else:
                    print(f"  [!] No course found with ID '{code}'.")

        elif choice == "0":
            break

        else:
            print("  [!] Invalid choice.")


def lecturer_menu(dept):
    """
    Sub-menu for all lecturer-related operations.
    // at any prompt cancels the current operation and returns to this menu.
    """
    while True:
        print("\n-- LECTURER MENU -----------------------------------------")
        print("  1. Add new lecturer")
        print("  2. View all lecturers")
        print("  3. View lecturer profile")
        print("  4. Assign lecturer to course")
        print("  0. Back to main menu")
        print("----------------------------------------------------------")

        choice = input("  Enter choice: ").strip()

        if choice == "1":
            print("\n  - Add New Lecturer -")

            lid = get_input("  Lecturer ID  (e.g. L001): ").upper()
            if lid == "//":
                continue

            name = get_input("  Full Name               : ").lower()
            if name == "//":
                continue

            email = get_input("  Email Address           : ").lower()
            if email == "//":
                continue

            spec = get_input("  Specialisation          : ").lower()
            if spec == "//":
                continue

            dept.add_lecturer(lid, name, email, spec)

        elif choice == "2":
            dept.list_all_lecturers()

        elif choice == "3":
            while True:
                lid = get_input("  Enter Lecturer ID: ").upper()
                if lid == "//":
                    break
                lecturer = dept.get_lecturer(lid)
                if lecturer:
                    lecturer.display_profile()
                    break
                else:
                    print(f"  [!] No lecturer found with ID '{lid}'.")

        elif choice == "4":
            # Step 1 - valid lecturer
            lid = None
            while True:
                lid = get_input("  Enter Lecturer ID: ").upper()
                if lid == "//":
                    break
                lecturer = dept.get_lecturer(lid)
                if lecturer:
                    break
                else:
                    print(f"  [!] No lecturer found with ID '{lid}'.")

            if lid == "//":
                continue

            # Step 2 - valid course
            while True:
                code = get_input("  Course Code: ").upper()
                if code == "//":
                    break
                course = dept.get_course(code)
                if course:
                    dept.course_assign_lecturer(lid, code)
                    break
                else:
                    print(f"  [!] No course found with ID '{code}'.")

        elif choice == "0":
            break

        else:
            print("  [!] Invalid choice.")


# ===========================================================================
#  MAIN FUNCTION
# ===========================================================================

def main():
    """
    Main function: initialise the department, load saved data,
    and display the top-level interactive menu.
    """
    print_opening()

    dept = Department("School of Computer Science")
    file_handler.load_all(dept)

    while True:
        print("\n== MAIN MENU =============================================")
        dept.department_summary()
        print("  1. Student Management")
        print("  2. Course Management")
        print("  3. Lecturer Management")
        print("  4. Save all data")
        print("  0. Exit")
        print("==========================================================")

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
            confirm = input("  Save before exiting? (y/n): ").strip().lower()
            if confirm == "y":
                file_handler.save_all(dept)
            print("\n  Goodbye!\n")
            break
        else:
            print("  [!] Invalid choice. Please enter 0-4.")


if __name__ == "__main__":
    main()
