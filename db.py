import mysql.connector

from config import Db_Table, DB_Database, DB_config


def create_Database():
    conn = mysql.connector.connect(**DB_config)
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_Database}")
    conn.commit()
    cursor.close()
    conn.close()


def get_connection():

    db_config = DB_config.copy()
    db_config["database"] = DB_Database
    return mysql.connector.connect(**db_config)


def create_Table():

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS {Db_Table}
        (student_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        age INT NOT NULL,
        course VARCHAR(100) NOT NULL
)""")

    conn.commit()
    cursor.close()
    conn.close()
