from functions import (
    initialize_files,
    add_student,
    add_course_for_student,
    show_student_information,
    delete_student
)

def main():
    initialize_files()
    
    while True:
        print("\n" + "=" * 50)
        print("                 Student Registration                 ")
        print("                   System in Python                   ")
        print("=" * 50)
        print("                      Main Menu                       ")
        print("             Student Registration System              ")
        print("=" * 50)
        print("    Options:")
        print("          1. Add Student")
        print("          2. Add Course for a Student")
        print("          3. Show Student Information")
        print("          4. Delete Student")
        print("          5. Exit")
        print("=" * 50)
        
        choice = input("Enter an option: ").strip()
        
        if choice == '1':
            add_student()
        elif choice == '2':
            add_course_for_student()
        elif choice == '3':
            show_student_information()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()