# Student Management System CLI based using Database

import config, db, add_student, get_student, delete_student, update_student

db.create_Database()
db.create_Table()

print(f"===== STUDENT MANAGEMENT SYSTEM ===== ")

Repeat = True

while Repeat:
    print(
        f"Enter your choice to perform the action:\n1. Create new Student\n2. View Student Details\n3. Update Student Details\n4. Delete Student Details\n5. Search Student Details\n6. Exit the System"
    )

    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            add_student.add_student()
        case 2:
            get_student.all_student_details()
        case 3:
            update_student.update_student_details()
        case 4:
            delete_student.delete_student_details()
        case 5:
            get_student.get_student_details()
        case 6:
            Repeat = False
        case _:
            print("Invalid Choice Try again!")
