import pandas as pd
from database import get_connection

conn = get_connection()
def load_departments():
    return pd.read_sql(
        "SELECT * FROM Departments",
        conn
    )

def load_students():
    return pd.read_sql(
        "SELECT * FROM Students",
        conn
    )
def load_subjects():
    return pd.read_sql(
        "SELECT * FROM Subjects",
        conn
    )
def student_subjects():
    return pd.read_sql(
        "SELECT * FROM Student_Subjects",
        conn
    )
def load_marks():
    return pd.read_sql(
        "SELECT * FROM Marks",
        conn
    )
def load_attendance():
    return pd.read_sql(
        "SELECT * FROM Attendance",
        conn
    )
conn.close()