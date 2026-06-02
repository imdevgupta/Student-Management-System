import db, config


def all_student_details():
    conn = db.get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """SELECT * FROM student"""

    cursor.execute(query)
    student = cursor.fetchall()

    if student:
        print(f"\n===== ALL STUDENT DETAILS =====")
        for students in student:
            for key, value in students.items():
                print(f"{key} : {value}")
    else:
        print(f"No Record found.")

    cursor.close()
    conn.close()


def get_student_details():
    conn = db.get_connection()
    cursor = conn.cursor(dictionary=True)

    id = int(input("Enter the id: "))
    query = """SELECT * FROM student WHERE student_id = %s"""
    value = id

    cursor.execute(query, (id,))
    student = cursor.fetchone()

    if student:
        print(f"===== STUDENT DETAILS =====")
        for key, value in student.items():
            print(f"{key} : {value}")
    else:
        print(f"No Record found.")

    cursor.close()
    conn.close()
