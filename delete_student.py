import db, config


def delete_student_details():

    conn = db.get_connection()
    cursor = conn.cursor()

    id = int(input("Enter the id: "))
    query = """DELETE FROM student WHERE student_id = %s"""
    cursor.execute(query, (id,))
    conn.commit()

    print(f"DELETED Succesfully")

    cursor.close()
    conn.close()
