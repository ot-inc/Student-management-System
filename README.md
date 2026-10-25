
# Student Management System

A database-driven Student Management System developed using Python, SQL, and SQLite.

The application allows users to register students, manage academic records, maintain subject information, record marks, calculate results, and generate student reports.

---

# About

The Student Management System is designed to assist educational institutions with organizing and maintaining student information.

The system provides a centralized platform for managing:

- Student records
- Academic information
- Subjects
- Marks
- Academic performance
- Result reporting

The project demonstrates practical software-development concepts including object-oriented programming, database integration, CRUD operations, validation, reporting, and data management.

---

# Problem Statement

Educational institutions often need a structured way to manage student records and academic information.

Manual record management can be time-consuming and prone to errors.

This system explores how software can simplify:

- Student registration
- Record management
- Academic tracking
- Result calculations
- Report generation

---

# Features

## Student Management

Users can:

- Add students
- View students
- Search students
- Update student information
- Delete students

---

## Subject Management

Users can:

- Add subjects
- View subjects
- Manage subject information

---

## Academic Records

Users can:

- Record marks
- Update marks
- Calculate averages
- View student performance

---

## Reporting

Users can:

- Generate reports
- View subject results
- Track academic performance
- Display average marks
- Determine pass or fail status

---

# Technologies Used

## Programming Language

```text
Python
```

---

## Database

```text
SQL
SQLite
```

---

## Development Concepts

```text
Object-Oriented Programming
CRUD Operations
Database Design
Input Validation
Error Handling
Reporting
```

---

# Project Structure

```text
student-management-system/
│
├── main.py
│
├── database/
│   ├── database.py
│   ├── schema.sql
│   └── students.db
│
├── models/
│   └── student.py
│
├── services/
│   ├── student_service.py
│   ├── subject_service.py
│   ├── grade_service.py
│   └── report_service.py
│
├── validators/
│   ├── student_validator.py
│   └── grade_validator.py
│
├── tests/
│   ├── test_students.py
│   └── test_grades.py
│
└── README.md
```

---

# Database Design

The system consists of three main tables.

## Students Table

Stores student information.

```sql
CREATE TABLE students (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    student_number TEXT UNIQUE,

    full_name TEXT,

    email TEXT,

    programme TEXT
);
```

---

## Subjects Table

Stores subject information.

```sql
CREATE TABLE subjects (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    subject_code TEXT UNIQUE,

    subject_name TEXT
);
```

---

## Grades Table

Stores marks and results.

```sql
CREATE TABLE grades (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    student_id INTEGER,

    subject_id INTEGER,

    mark REAL,

    FOREIGN KEY(student_id)
        REFERENCES students(id),

    FOREIGN KEY(subject_id)
        REFERENCES subjects(id)
);
```

---

# Student Workflow

## Step 1

Register a student.

Example:

```text
Student Number: STU001

Name: John Smith

Programme:
Software Development
```

---

## Step 2

Create subjects.

Example:

```text
PY101

Python Programming
```

---

## Step 3

Record marks.

Example:

```text
Student:
STU001

Subject:
PY101

Mark:
80
```

---

## Step 4

Generate results.

Example:

```text
Subject:
Python Programming

Mark:
80%

Result:
Distinction

Status:
PASS
```

---

# Example Result Classification

```text
75 - 100
Distinction

50 - 74
Pass

0 - 49
Fail
```

This grading scale is for demonstration purposes and can be customized.

---

# Example Student Report

```text
================================

STUDENT REPORT

Student:
John Smith

Programme:
Software Development

--------------------------------

PY101
Python Programming

Mark: 82%

Result: Distinction

--------------------------------

DB101
Database Systems

Mark: 74%

Result: Pass

--------------------------------

Average: 78%

Overall Status: PASS

================================
```

---

# CRUD Operations

The application demonstrates:

## Create

- Add students
- Add subjects
- Record grades

## Read

- View students
- View subjects
- View reports

## Update

- Update student details
- Modify grades

## Delete

- Remove student records
- Remove academic records

---

# Validation

The system validates:

- Student numbers
- Email addresses
- Marks
- Subject information
- Required fields

Examples:

```text
Mark must be between
0 and 100.

Email address is invalid.

Student number already exists.
```

---

# Error Handling

The application handles situations such as:

```text
Student not found

Subject not found

Duplicate student number

Invalid mark value

Missing required information
```

---

# Testing

The project includes unit tests for:

- Student validation
- Grade validation
- Result calculation
- Academic report generation

Run tests using:

```bash
python -m unittest discover tests
```

---

# Running The Project

## Clone Repository

```bash
git clone https://github.com/ot-inc/student-management-system.git
```

---

## Move To Project Folder

```bash
cd student-management-system
```

---

## Run Application

```bash
python main.py
```

---

# Skills Demonstrated

This project demonstrates:

- Python Programming
- SQL
- SQLite
- Object-Oriented Programming
- CRUD Operations
- Data Validation
- Error Handling
- Database Design
- Academic Reporting
- Problem Solving

---

# Future Improvements

Planned upgrades include:

- User Authentication
- Administrator Dashboard
- Lecturer Dashboard
- Student Portal
- Web Interface
- Flask Backend
- ASP.NET Core Version
- SQL Server Integration
- REST APIs
- Report Exporting
- PDF Reports
- Email Notifications

---

# Learning Outcomes

Through this project I gained practical experience in:

- Database development
- Software architecture
- Data management
- Record management systems
- Python programming
- Testing
- Input validation
- Backend development concepts

---

# Author

**Joseph Mankele Molope**

Software Developer | FNB App Academy 2026 Graduate

Interested in:

- Software Engineering
- Full-Stack Development
- Education Technology
- Public-Service Technology
- Database Systems
- Financial Technology

---

# Project Status

Active Portfolio Project

---

# License

This project was created for educational and portfolio purposes.
