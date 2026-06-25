# University Management System

A Python-based command-line application for managing students, courses,
and lecturers in a university department.

---

## Purpose

This system allows department staff to:
- Register and manage students, courses, and lecturers
- Enrol students in courses
- Record and review student grades
- Assign lecturers to courses
- Persist all data between sessions using .txt files

---

## Project Structure

```
university_system/
│
├── main.py            # Entry point — run this file to start the program
├── department.py      # Department class (central coordinator)
├── student.py         # Student class
├── course.py          # Course class
├── lecturer.py        # Lecturer class
├── file_handler.py    # .txt file read/write functions
    ├── students.txt   # Saved student records
    ├── courses.txt    # Saved course records
    └── lecturers.txt  # Saved lecturer records
```

---

## Installation

No external libraries are required. Only the Python standard library is used.

1. Clone or download this repository.
2. Run the downloaded files in any python tool eg, pycharm or vs-code. 
2. Navigate into the project folder:
   ```
   
   ```


---

## How to Run

```bash
python main.py
```

This opens the interactive main menu. Use number keys to navigate.

---

## Example Usage

```
=======================================================
   🏛️  UNIVERSITY MANAGEMENT SYSTEM
   School of Computer Science
=======================================================

══ MAIN MENU ══════════════════════════════
  DEPARTMENT: School of Computer Science
  Students  : 3
  Courses   : 3
  Lecturers : 2

  1. Student Management
  2. Course Management
  3. Lecturer Management
  4. Save all data
  0. Exit
```


## IMPORTANT entering // during an input, will cancel the operation 
## and take you back to the sub menu of the operation

### Adding a Student
Select `1 → 1`, then enter:
- Student ID: `S004`
- Name: `John Doe`
- Email: `john@uni.edu`

### Enrolling in a Course
Select `2 → 4`, enter the student ID and course code.

### Recording a Grade
Select `2 → 5`, enter student ID, course code, and numeric grade (0–100).

### Viewing a Transcript
Select `1 → 3`, enter a student ID to see all grades and average.

---

## Key Features

| Feature                | Where Implemented         |
|------------------------|---------------------------|
| Classes & Objects      | `student.py`, `course.py`, `lecturer.py`, `department.py` |
| Methods (4+ per class) | All class files            |
| Loops                  | `main.py`, `department.py` |
| Conditionals           | All files                  |
| File I/O (CSV)         | `file_handler.py`          |
| Exception Handling     | `file_handler.py`, `main.py` |
| Multiple Modules       | 5 separate `.py` files     |
| PEP 8 + Docstrings     | All files                  |
| Interactive Menu       | `main.py`                  |

---

## Data Persistence

All data is stored in plain-text .txt files inside the root folder.
The program loads data automatically on startup and saves on command or exit.

Example `students.csv`:
```
S001,Alice Smith,alice@uni.edu,CS101:88;MA201:75
S002,Bob Jones,bob@uni.edu,CS101:91;CS202:79
```

---

## Python Concepts Demonstrated

- **Classes and OOP**: Four classes with attributes, constructors (`__init__`), and methods
- **Dictionaries**: Used for O(1) lookups of students, courses, lecturers
- **Lists**: Enrolled student IDs, taught course codes
- **For loops**: Iterating collections for display and CSV output
- **While loops**: Menu navigation keeps running until user exits
- **If/elif/else**: Validation, grade letter conversion, menu 
- **try/except**: Catching `ValueError` (bad number input) and `IOError` (file errors)
- **File**: `open()`, `.read()`, `.write()`, `.strip()`, `.split()`
- **Modules**: Code split across 5 files; imported with `from X import Y`
- **Docstrings**:  documented to PEP 257 standard

---

## written by 

Pranav Tokhi
Gisma University of Applied Sciences
GH1045521
