import matplotlib.pyplot as plt
import pandas as pd
from database import get_connection
from analyzer import *

conn = get_connection()

# 1.Number of students per department👇

def students_per_department_chart():
    students_by_dept = students_per_department()

    plt.figure(figsize=(5,3))

    plt.bar(
    students_by_dept.index,
    students_by_dept.values
)
    plt.xlabel('Department')
    plt.ylabel('Number of Students')
    plt.title('Students per Department')
    plt.xticks(rotation=45)
    plt.tight_layout()

    return plt.gcf()

    


# 2. Average Marks by Department👇
def average_marks_per_department_chart():
  average_marks = average_marks_per_department()

  plt.figure(figsize=(5,3))

  plt.bar(average_marks.index,
        average_marks.values)

  plt.xlabel('Department')
  plt.ylabel('Average marks of Students')
  plt.title('Average Marks by Department')

  plt.xticks(rotation=45)
  plt.tight_layout()

  return plt.gcf()

  

## 3. High performer percentage / Pass percentage per department👇

def high_performer_chart():
  high_percent, low_percent = High_performer_percentage()

  plt.figure(figsize=(10,5))

  plt.bar(
    high_percent.index,
    high_percent.values
)

  plt.xlabel('Department')
  plt.ylabel('High scorer Percentage')
  plt.title('High scorer Percentage per Department')

  

## 4. Average attendance per department👇
def attendance_per_department_chart():
  attendance_data = average_attendance_per_dept()
  plt.figure(figsize=(10,5))

  plt.bar(
    attendance_data.index,
    attendance_data.values)

  plt.xlabel('Departments')
  plt.ylabel('Attendance percentage')
  plt.title('Average attendance per department')

  


# 5. Top 10 Students Dashboard👇
def top_10_students_chart():
  top_10 = top_ten()

  plt.figure(figsize=(5,3))

  plt.barh(
    top_10['student_name'],
    top_10['average_marks']
)

  plt.xlabel('Average Marks')
  plt.ylabel('Student Name')
  plt.title('Top 10 Students')
  plt.xticks(rotation=45)
  plt.tight_layout()

  return plt.gcf()

  


## 6. Attendance Vs Marks👇
def attendance_vs_marks_chart():
  # attendance_df = pd.read_sql('SELECT * FROM Attendance;',conn)

  data = marks_vs_attendance()

  plt.figure(figsize=(10,5))

  plt.scatter(
    data['attendance_percentage'],
    data['marks'],
    alpha= .5,
    c='#2b4963'
)

  plt.xlabel('Attendance %')
  plt.ylabel('Average Marks')
  plt.title('Attendance vs Marks')

  

## Topper department contribution👇
def topper_department_contribution_chart():
    dept_count = topper_department_contribution()
    plt.figure(figsize=(10,10))
    plt.pie(dept_count.values, 
        labels=dept_count.index,
        autopct = '%1.1f%%',
        shadow=True)

    plt.title("Topper department contribution")
    

# 1. Marks distribution Histogram 👇
# marks_df = pd.read_sql('SELECT * FROM Marks',conn)

# plt.figure(figsize=(10,5))

# plt.hist(marks_df['marks'],
#          bins = 10,
#          color = '#032e02',
#          edgecolor = '#b9e3b8')

# plt.title('Histogram of Marks distribution')
# plt.xlabel('Marks')
# plt.ylabel('Frequency')




# CHART EXPORTS

def save_chart(filename):

    plt.tight_layout()

    plt.savefig(
        f'charts/{filename}',
        dpi=300
    )

    print(f'{filename} saved.')


def export_students_per_department_chart():
    students_per_department_chart()
    save_chart('students_per_department.png')
    plt.close()


def export_average_marks_department_chart():
    average_marks_per_department_chart()
    save_chart('average_marks_department.png')
    plt.close()


def export_high_performer_chart():
    high_performer_chart()
    save_chart('high_performer_percentage.png')
    plt.close()


def export_average_attendance_chart():
    attendance_per_department_chart()
    save_chart('average_attendance_department.png')
    plt.close()


def export_top_10_students_chart():
    top_10_students_chart()
    save_chart('top_10_students.png')
    plt.close()


def export_attendance_vs_marks_chart():
    attendance_vs_marks_chart()
    save_chart('attendance_vs_marks.png')
    plt.close()


def export_topper_department_contribution_chart():
    topper_department_contribution_chart()
    save_chart('topper_department_contribution.png')
    plt.close()


if __name__ == "__main__":

    export_students_per_department_chart()
    export_average_marks_department_chart()
    export_high_performer_chart()
    export_average_attendance_chart()
    export_top_10_students_chart()
    export_attendance_vs_marks_chart()
    export_topper_department_contribution_chart()