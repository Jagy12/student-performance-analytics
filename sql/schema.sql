CREATE DATABASE IF NOT EXISTS StudentPerformanceAnalyticsSystem;
USE StudentPerformanceAnalyticsSystem;

CREATE TABLE Departments (
    department_id VARCHAR(10) PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE Students (
    student_id VARCHAR(10) PRIMARY KEY,
    student_name VARCHAR(50) NOT NULL,
    contact_num VARCHAR(15) UNIQUE,
    address VARCHAR(100),
    department_id VARCHAR(10),
    major VARCHAR(50),

    FOREIGN KEY (department_id)
    REFERENCES Departments(department_id)
);

CREATE TABLE Subjects (
    subject_id VARCHAR(10) PRIMARY KEY,
    subject_name VARCHAR(50) NOT NULL,
    department_id VARCHAR(10),

    FOREIGN KEY (department_id)
    REFERENCES Departments(department_id)

);

CREATE TABLE Student_Subjects (
    student_id VARCHAR(10),
    subject_id VARCHAR(10),

    PRIMARY KEY(student_id, subject_id),

    FOREIGN KEY(student_id)
    REFERENCES Students(student_id),

    FOREIGN KEY(subject_id)
    REFERENCES Subjects(subject_id)
);

CREATE TABLE Marks (
    mark_id INT AUTO_INCREMENT PRIMARY KEY,

    student_id VARCHAR(10),
    subject_id VARCHAR(10),

    marks DECIMAL(5,2),

    FOREIGN KEY (student_id)
    REFERENCES Students(student_id),

    FOREIGN KEY (subject_id)
    REFERENCES Subjects(subject_id)
);
CREATE TABLE Attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,

    student_id VARCHAR(10) UNIQUE,

    attendance_percentage DECIMAL(5,2),

    FOREIGN KEY (student_id)
    REFERENCES Students(student_id)
);