import sqlite3

from database.database import DATABASE


def add_student(student_number, name, age, course):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO students (student_number, name, age, course)
        VALUES (?, ?, ?, ?)
        """,
        (
            student_number.strip(),
            name.strip(),
            age,
            course.strip(),
        ),
    )

    conn.commit()
    conn.close()


def view_student():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students ORDER BY id")
    records = cursor.fetchall()

    conn.close()
    return records


def search_student(student_number):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM students
        WHERE student_number = ?
        """,
        (student_number.strip(),),
    )

    record = cursor.fetchone()
    conn.close()
    return record


def delete_student(student_number):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM students
        WHERE student_number = ?
        """,
        (student_number.strip(),),
    )

    deleted = cursor.rowcount > 0
    conn.commit()
    conn.close()
    return deleted