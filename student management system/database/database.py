import os
import sqlite3

DATABASE = os.path.join("data", "students.db")


def create_table():
    os.makedirs(os.path.dirname(DATABASE), exist_ok=True)

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT name
        FROM sqlite_master
        WHERE type = 'table' AND name = 'students'
        """
    )
    table_exists = cursor.fetchone() is not None

    if table_exists:
        cursor.execute("PRAGMA table_info(students)")
        columns = [column[1] for column in cursor.fetchall()]

        if "student_number" not in columns and "students_number" in columns:
            cursor.execute("ALTER TABLE students RENAME TO students_old")
            cursor.execute(
                """
                CREATE TABLE students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_number TEXT NOT NULL UNIQUE,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    course TEXT NOT NULL
                )
                """
            )
            cursor.execute(
                """
                INSERT INTO students (student_number, name, age, course)
                SELECT students_number, name, age, course
                FROM students_old
                """
            )
            cursor.execute("DROP TABLE students_old")
    else:
        cursor.execute(
            """
            CREATE TABLE students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_number TEXT NOT NULL UNIQUE,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                course TEXT NOT NULL
            )
            """
        )

    conn.commit()
    conn.close()