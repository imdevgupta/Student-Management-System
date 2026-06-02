import db, config


def add_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")

    conn = db.get_connection()
    cursor = conn.cursor()

    query = f"""
    INSERT INTO {config.Db_Table}
    (name, age, course)
    VALUES (%s, %s, %s)
    """

    cursor.execute(query, (name, age, course))

    conn.commit()

    print("Student Added Successfully")

    cursor.close()
    conn.close()
    return
