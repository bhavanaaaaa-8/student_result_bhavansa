
import json
from pathlib import Path

DATA_FILE = Path("students.json")


# 1. DATA MANAGEMENT

def load_students():
    if DATA_FILE.exists():
        try:
            with DATA_FILE.open("r") as file:
                data = json.load(file)
                if isinstance(data, list):
                    return data
        except (json.JSONDecodeError, OSError):
            print("Error loading student records.")

    return []


def save_students(students):
    try:
        with DATA_FILE.open("w") as file:
            json.dump(students, file, indent=4)
    except OSError:
        print("Error saving student records.")


# 2. MARKS VALIDATION

def validate_marks(marks):
    try:
        marks = float(marks)

        if 0 <= marks <= 100:
            return marks

        print("Marks must be between 0 and 100.")
        return None

    except ValueError:
        print("Please enter valid numeric marks.")
        return None


def get_marks():
    while True:
        marks = input("Enter marks (0-100): ")
        valid_marks = validate_marks(marks)

        if valid_marks is not None:
            return valid_marks


# 3. ACADEMIC CALCULATIONS

def calculate_total(subjects):
    return sum(subjects.values())


def calculate_percentage(subjects):
    if not subjects:
        return 0

    total = calculate_total(subjects)
    maximum = len(subjects) * 100

    return (total / maximum) * 100


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


# 4. FIND STUDENT

def find_student(students, student_id):
    for student in students:
        if student["id"] == student_id:
            return student

    return None


# 5. ADD STUDENT

def add_student(students):
    student_id = input("Enter student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    if find_student(students, student_id):
        print("Student ID already exists.")
        return

    name = input("Enter student name: ").strip()
    student_class = input("Enter class: ").strip()

    if not name or not student_class:
        print("Name and class cannot be empty.")
        return

    subjects = {}

    print("\nEnter subject names and marks.")
    print("Type 'done' when finished.")

    while True:
        subject = input("\nEnter subject: ").strip()

        if subject.lower() == "done":
            break

        if not subject:
            print("Subject name cannot be empty.")
            continue

        if any(s.lower() == subject.lower() for s in subjects):
            print("Subject already exists.")
            continue

        subjects[subject] = get_marks()

    if not subjects:
        print("At least one subject is required.")
        return

    student = {
        "id": student_id,
        "name": name,
        "class": student_class,
        "subjects": subjects
    }

    students.append(student)
    save_students(students)

    print("\nStudent added successfully!")


# 6. UPDATE STUDENT

def update_student(students):
    student_id = input("Enter student ID: ").strip()
    student = find_student(students, student_id)

    if not student:
        print("Student not found.")
        return

    print("\n1. Update Name")
    print("2. Update Class")
    print("3. Update Subject Marks")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        name = input("Enter new name: ").strip()

        if name:
            student["name"] = name

    elif choice == "2":
        student_class = input("Enter new class: ").strip()

        if student_class:
            student["class"] = student_class

    elif choice == "3":
        subject = input("Enter subject name: ").strip()

        if not subject:
            print("Subject name cannot be empty.")
            return

        existing = next(
            (s for s in student["subjects"]
             if s.lower() == subject.lower()),
            None
        )

        if existing:
            student["subjects"][existing] = get_marks()
        else:
            student["subjects"][subject] = get_marks()

    else:
        print("Invalid choice.")
        return

    save_students(students)
    print("Student record updated successfully!")


# 7. DELETE STUDENT

def delete_student(students):
    student_id = input("Enter student ID: ").strip()
    student = find_student(students, student_id)

    if not student:
        print("Student not found.")
        return

    confirm = input(
        f"Delete record of {student['name']}? (yes/no): "
    ).strip().lower()

    if confirm == "yes":
        students.remove(student)
        save_students(students)
        print("Student deleted successfully.")
    else:
        print("Deletion cancelled.")


# 8. DISPLAY STUDENT DETAILS

def display_student(student):
    subjects = student["subjects"]

    total = calculate_total(subjects)
    percentage = calculate_percentage(subjects)
    grade = calculate_grade(percentage)
    maximum = len(subjects) * 100

    print("\n========== STUDENT DETAILS ==========")

    print("Student ID:", student["id"])
    print("Name:", student["name"])
    print("Class:", student["class"])

    print("\nSubject Marks:")

    for subject, marks in subjects.items():
        print(f"{subject}: {marks}/100")

    print("\n========== ACADEMIC RESULTS ==========")

    print(f"Total Marks: {total:g}/{maximum}")
    print(f"Percentage: {percentage:.2f}%")
    print("Grade:", grade)

    print("======================================")


# 9. SEARCH STUDENT

def search_student(students):
    query = input("Enter student ID or name: ").strip().lower()

    if not query:
        print("Please enter a search value.")
        return

    results = []

    for student in students:
        if (query == student["id"].lower()
                or query in student["name"].lower()):
            results.append(student)

    if not results:
        print("No matching student found.")
        return

    for student in results:
        display_student(student)


# 10. VIEW ALL STUDENTS

def view_all_students(students):
    if not students:
        print("No student records available.")
        return

    for student in students:
        display_student(student)


# 11. PERFORMANCE SUMMARY

def performance_summary(students):
    if not students:
        print("No records available.")
        return

    averages = [
        calculate_percentage(s["subjects"])
        for s in students if s["subjects"]
    ]

    if not averages:
        print("No marks available.")
        return

    print("\n====== PERFORMANCE SUMMARY ======")

    print("Total Students:", len(students))
    print(f"Class Average: {sum(averages)/len(averages):.2f}%")
    print(f"Highest Percentage: {max(averages):.2f}%")
    print(f"Lowest Percentage: {min(averages):.2f}%")

    top_student = max(
        (s for s in students if s["subjects"]),
        key=lambda s: calculate_percentage(s["subjects"])
    )

    print("Top Performer:", top_student["name"])

    print("\nGrade Distribution:")

    grades = {
        "A+": 0, "A": 0, "B": 0,
        "C": 0, "D": 0, "F": 0
    }

    for average in averages:
        grade = calculate_grade(average)
        grades[grade] += 1

    for grade, count in grades.items():
        print(f"Grade {grade}: {count} students")

    print("\nSubject-wise Average:")

    subject_data = {}

    for student in students:
        for subject, marks in student["subjects"].items():
            key = subject.lower()

            if key not in subject_data:
                subject_data[key] = {
                    "name": subject,
                    "total": 0,
                    "count": 0
                }

            subject_data[key]["total"] += marks
            subject_data[key]["count"] += 1

    for data in subject_data.values():
        average = data["total"] / data["count"]

        print(f"{data['name']}: {average:.2f}%")

    print("=================================")


# 12. MAIN MENU

def main_menu():
    print("\n===================================")
    print("   STUDENT ACADEMIC MANAGEMENT")
    print("===================================")

    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. View All Students")
    print("6. Calculate Academic Results")
    print("7. Performance Summary")
    print("8. Exit")


# 13. MAIN FUNCTION

def main():
    students = load_students()

    while True:
        main_menu()

        choice = input("\nEnter your choice (1-8): ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            update_student(students)

        elif choice == "3":
            delete_student(students)

        elif choice == "4":
            search_student(students)

        elif choice == "5":
            view_all_students(students)

        elif choice == "6":
            student_id = input("Enter student ID: ").strip()
            student = find_student(students, student_id)

            if student:
                display_student(student)
            else:
                print("Student not found.")

        elif choice == "7":
            performance_summary(students)

        elif choice == "8":
            print("\nThank you for using the application!")
            break

        else:
            print("Invalid choice. Please select 1-8.")


# PROGRAM EXECUTION

if __name__ == "__main__":
    main()
