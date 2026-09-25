import os

STUDENTS_FILE = "students.txt"
COURSES_FILE = "courses.txt"

def initialize_files():
    """Ensures the text storage files exist."""
    for filename in [STUDENTS_FILE, COURSES_FILE]:
        if not os.path.exists(filename):
            open(filename, "w").close()

def add_student():
    print("\n--- Add Student ---")
    student_id = input("Enter Student ID: ").strip()
    name = input("Enter Student Name: ").strip()
    
    # Check if student already exists
    if student_exists(student_id):
        print("Error: Student ID already exists!")
        return

    with open(STUDENTS_FILE, "a") as f:
        f.write(f"{student_id},{name}\n")
    print("Student added successfully!")

def student_exists(student_id):
    if not os.path.exists(STUDENTS_FILE):
        return False
    with open(STUDENTS_FILE, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if parts and parts[0] == student_id:
                return True
    return False

def add_course_for_student():
    print("\n--- Add Course for a Student ---")
    student_id = input("Enter Student ID: ").strip()
    
    if not student_exists(student_id):
        print("Error: Student ID not found!")
        return
        
    course_name = input("Enter Course Name: ").strip()
    
    with open(COURSES_FILE, "a") as f:
        f.write(f"{student_id},{course_name}\n")
    print("Course added successfully for the student!")

def show_student_information():
    print("\n--- Student Information ---")
    if not os.path.exists(STUDENTS_FILE):
        print("No student records found.")
        return

    # Load students
    students = {}
    with open(STUDENTS_FILE, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) >= 2:
                students[parts[0]] = parts[1]

    # Load courses
    courses = {}
    if os.path.exists(COURSES_FILE):
        with open(COURSES_FILE, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) >= 2:
                    s_id, c_name = parts[0], parts[1]
                    if s_id not in courses:
                        courses[s_id] = []
                    courses[s_id].append(c_name)

    if not students:
        print("No students registered yet.")
        return

    for s_id, name in students.items():
        print(f"\nStudent ID: {s_id}")
        print(f"Name: {name}")
        print("Enrolled Courses:")
        enrolled = courses.get(s_id, [])
        if enrolled:
            for course in enrolled:
                print(f"  - {course}")
        else:
            print("  - None")
        print("-" * 30)

def delete_student():
    print("\n--- Delete Student ---")
    student_id = input("Enter Student ID to delete: ").strip()

    if not student_exists(student_id):
        print("Error: Student ID not found!")
        return

    # Remove from students.txt
    updated_students = []
    with open(STUDENTS_FILE, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if parts and parts[0] != student_id:
                updated_students.append(line)

    with open(STUDENTS_FILE, "w") as f:
        f.writelines(updated_students)

    # Remove associated courses from courses.txt
    updated_courses = []
    if os.path.exists(COURSES_FILE):
        with open(COURSES_FILE, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if parts and parts[0] != student_id:
                    updated_courses.append(line)

        with open(COURSES_FILE, "w") as f:
            f.writelines(updated_courses)

    print("Student and their associated courses deleted successfully!")