import sqlite3

from database.database import create_table
from services.student_service import (
    add_student,
    delete_student,
    search_student,
    view_student,
)


def main():
    create_table()

    while True:
        print("\n==========")
        print("STUDENT MANAGEMENT SYSTEM")
        print("==========")

        print("1. Add student")
        print("2. View students")
        print("3. Search student")
        print("4. Delete student")
        print("5. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            student_number = input("Student number: ").strip()
            name = input("Name: ").strip()

            while True:
                age_input = input("Age: ").strip()
                try:
                    age = int(age_input)
                    break
                except ValueError:
                    print("Age must be a valid integer.")

            course = input("Course: ").strip()

            if not student_number or not name or not course:
                print("Student number, name, and course are required.")
                continue

            try:
                add_student(student_number, name, age, course)
                print("Student added successfully.")
            except sqlite3.IntegrityError:
                print("A student with this student number already exists.")

        elif choice == "2":
            students = view_student()

            print("\nRegistered Students\n")

            if not students:
                print("No students found.")
            else:
                for student in students:
                    print(student)

        elif choice == "3":
            student_number = input("Enter Student Number: ").strip()
            student = search_student(student_number)

            if student:
                print(student)
            else:
                print("Student not found.")

        elif choice == "4":
            student_number = input("Enter Student Number: ").strip()
            deleted = delete_student(student_number)

            if deleted:
                print("Student deleted.")
            else:
                print("Student not found.")

        elif choice == "5":
            print("Goodbye.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye.")