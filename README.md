# Student Academic Management System

## Project Overview
The Student Academic Management System is a Python-based command-line application designed to manage student information, subjects, marks, grades and academic performance.

It allows users to add, update, delete, search and view student records. It also automatically calculates total marks, percentages and grades and generates academic performance summaries.

## Features

- **Add Students:** Store student ID, name, class and subject marks.
- **Update Records:** Modify student details and subject marks.
- **Delete Students:** Remove student records.
- **Search Students:** Search using student ID or name.
- **View Records:** Display individual or all student records.
- **Marks Validation:** Accept only numeric marks between 0 and 100.
- **Automatic Calculations:** Calculate total marks, percentage and grades.
- **Performance Summary:** Generate class averages, highest and lowest percentages, grade distribution and subject-wise averages.
- **Data Persistence:** Store student information in a JSON file.

## Technologies Used

- Python 3
- JSON
- Lists and Dictionaries
- Functions
- pathlib

## Project Structure

```text
Student_Academic_Management/
│
├── student_management.py
├── students.json
└── README.md
```

The `students.json` file is created automatically when the first student record is added.

## How to Run

1. Install Python 3.
2. Save the program as `student_management.py`.
3. Open a terminal in the project folder.
4. Execute the following command:

```bash
python student_management.py
```

5. Select an option from the main menu.

## Main Menu

```text
===================================
   STUDENT ACADEMIC MANAGEMENT
===================================

1. Add Student
2. Update Student
3. Delete Student
4. Search Student
5. View All Students
6. Calculate Academic Results
7. Performance Summary
8. Exit
```

## Grading System

| Percentage | Grade |
|---|---|
| 90–100% | A+ |
| 80–89% | A |
| 70–79% | B |
| 60–69% | C |
| 50–59% | D |
| Below 50% | F |

## Academic Calculations

**Total Marks:**

Sum of marks obtained in all subjects.

**Percentage:**

(Total Marks Obtained / Maximum Marks) × 100

**Grade:**

Automatically assigned according to the calculated percentage.

## Data Storage

Student information is stored using a list of dictionaries. Subject marks are maintained using nested dictionaries.

JSON is used to save records permanently so that information remains available even after the application is closed.

## Input Validation

- Student IDs must be unique.
- Student names and classes cannot be empty.
- Marks must be numeric.
- Marks must be between 0 and 100.
- Duplicate subjects are not allowed when adding a student.
- Invalid menu choices are handled appropriately.

## Future Improvements

- Export academic reports to CSV or PDF.
- Add attendance management.
- Introduce subject-wise grading.
- Create a graphical user interface.
- Add student login and administrator access.

## Conclusion

This project demonstrates the use of Python functions, lists, dictionaries, loops, conditional statements, exception handling and JSON file handling to create a practical student academic management application.
