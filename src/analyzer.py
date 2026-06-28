import pandas as pd
from  database import get_connection
from data_loader import *

conn = get_connection()

## 1. Number of students per department👇

def students_per_department():
    students_df = load_students()
    dept_count = students_df.groupby('department_id')['student_id'].count()
    return dept_count
# print(students_per_department())

## 2. Average marks of students👇

def average_marks_per_student():
    marks_df = load_marks()
    avg_marks = marks_df.groupby('student_id')['marks'].mean()
    return avg_marks
# print(average_marks_per_student())

## 3. Topper details👇

def topper():
    students_df = load_students()
    departments_df = load_departments()
    avg_marks = average_marks_per_student()
    topper_mark = avg_marks.max()
    topper_id = avg_marks.idxmax()
    merged = pd.merge(students_df,
                      departments_df,
                      on='department_id')
    topper_details = merged[merged['student_id'] == topper_id]
    
    return topper_mark, topper_id, topper_details
# print(topper())

# 4. Average Marks by Department👇

def average_marks_per_department():
    students_df = load_students()
    marks_df = load_marks()

    average_marks = pd.merge(
    students_df,
    marks_df,
    on='student_id'
)
    department_df = average_marks.groupby('department_id')['marks'].mean()
    return department_df
# print(average_marks_per_department())

# 5. Average attendance per department👇
def average_attendance_per_dept():
    students_df = load_students()
    attendance_df = load_attendance()

    merged = pd.merge(
    students_df,
    attendance_df,
    on= 'student_id'
)
    dept_wise_attendance = merged.groupby('department_id')['attendance_percentage'].mean()
    return dept_wise_attendance
# print(average_attendance_per_dept())

## 6. Top 10 students 👇

def top_ten():

    students_df = load_students()

    avg_marks = average_marks_per_student()

    top_10 = avg_marks.sort_values(
        ascending=False
    ).head(10)

    top_10 = top_10.reset_index()

    top_10.rename(
        columns={'marks':'average_marks'},
        inplace=True
    )

    merged = pd.merge(
        top_10,
        students_df,
        on='student_id'
    )
    return merged[
        [
            'student_id',
            'student_name',
            'department_id',
            'average_marks'
        ]
    ]
# print(top_ten())

## 7. Topper Department wise contribution👇

def topper_department_contribution():
    students_df = load_students()

    merged = top_ten()
    dept_count = merged.groupby('department_id')['student_id'].count()
    return dept_count
# print(topper_department_contribution())


## 8. High performer percentage / Pass percentage per department👇
def High_performer_percentage():
    students_df = load_students()
    avg_marks = average_marks_per_student()
    avg_marks = avg_marks.reset_index()
    avg_marks['high'] = avg_marks['marks'] >= 80
    merged = pd.merge(
        avg_marks,
        students_df,
        on = 'student_id'
)
    high_percentage = merged.groupby(
        'department_id'
    )['high'].mean() * 100

    low_percentage = 100 - high_percentage

    return high_percentage, low_percentage
# print(High_performer_percentage())

## 9. Filetring Low and High attendance👇

# attendance_df = load_attendance()

# students_df = load_students()

# students_attendance = pd.merge(
#     attendance_df,
#     students_df,
#     on='student_id'
# )

# low_attendance = students_attendance[
#     students_attendance['attendance_percentage'] < 85
# ]

# print("\nStudents with Low Attendance:")
# print(
#     low_attendance[
#         ['student_id','student_name','attendance_percentage']
#     ]
# )

# high_attendance = students_attendance[
#     students_attendance['attendance_percentage'] > 95
# ]

# print("\nStudents with High Attendance:")
# print(
#     high_attendance[
#         ['student_id','student_name','attendance_percentage']
#     ]
# )

# 10.Marks Vs Attendance👇

def marks_vs_attendance():
    marks_df = load_marks() 
    attendance_df = load_attendance()

    avg_marks = average_marks_per_student().reset_index()
    merged = pd.merge(
        avg_marks,
        attendance_df,
        on = 'student_id'
    )
    return merged
# print(marks_vs_attendance())



# REPORT EXPORTS

def export_topper_details_report():

    topper_mark, topper_id, topper_details = topper()

    topper_details.to_csv(
        'reports/topper_details.csv',
        index=False
    )


def export_top_10_students_report():

    top_10 = top_ten()

    top_10.to_csv(
        'reports/top_10_students.csv',
        index=False
    )


def export_average_marks_department_report():

    average_marks = average_marks_per_department()

    average_marks.reset_index().to_csv(
        'reports/average_marks_department.csv',
        index=False
    )


def export_average_attendance_department_report():

    attendance = average_attendance_per_dept()

    attendance.reset_index().to_csv(
        'reports/average_attendance_department.csv',
        index=False
    )


def export_high_performer_report():

    high_percent, low_percent = High_performer_percentage()

    high_percent.reset_index().to_csv(
        'reports/high_performer_percentage.csv',
        index=False
    )


def export_students_per_department_report():

    students = students_per_department()

    students.reset_index().to_csv(
        'reports/students_per_department.csv',
        index=False
    )


def export_marks_vs_attendance_report():

    data = marks_vs_attendance()

    data.to_csv(
        'reports/marks_vs_attendance.csv',
        index=False
    )


def export_topper_department_contribution_report():

    contribution = topper_department_contribution()

    contribution.reset_index().to_csv(
        'reports/topper_department_contribution.csv',
        index=False
    )

def export_all_reports():

    export_topper_details_report()
    export_top_10_students_report()
    export_average_marks_department_report()
    export_average_attendance_department_report()
    export_high_performer_report()
    export_students_per_department_report()
    export_marks_vs_attendance_report()
    export_topper_department_contribution_report()

    print("All reports exported.")