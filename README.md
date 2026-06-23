 📊 Student Performance Analytics System

A Python-based Data Analytics project that analyzes student academic performance, attendance, and departmental statistics using MySQL, Pandas, and Matplotlib.

This project demonstrates the complete data analytics workflow:

* Data Storage using MySQL
* Data Extraction using Pandas
* Data Analysis using Pandas
* Data Visualization using Matplotlib
* Report Generation using CSV exports
* Chart Exporting as PNG files
* Menu-Driven Analytics Dashboard

---

 🚀 Features

 Department Analysis

 1. Students per Department

Displays the number of students enrolled in each department.

 2. Average Marks per Department

Calculates the average marks scored by students department-wise.

 3. High Performer Percentage

Shows the percentage of students scoring above the defined high-performance threshold in each department.

 4. Average Attendance per Department

Calculates the average attendance percentage for every department.

 5. Topper Department Contribution

Shows which departments contribute the most students to the Top 10 performers list.

---

 Student Performance Analysis

 1. Average Marks per Student

Calculates average marks across all subjects for every student.

 2. Topper Identification

Finds the overall topper of the institution.

 3. Top 10 Students Dashboard

Displays the highest-performing students based on average marks.

 4. Marks vs Attendance Analysis

Analyzes the relationship between attendance percentage and academic performance.

---

 Report Generation

Generate CSV reports automatically for:

* Students per Department
* Average Marks per Department
* Average Attendance per Department
* High Performer Percentage
* Top 10 Students
* Topper Details
* Topper Department Contribution
* Marks vs Attendance Analysis

Reports are stored in:

```text
reports/
```

---

 Chart Export

Generate PNG charts automatically for:

* Students per Department
* Average Marks per Department
* High Performer Percentage
* Average Attendance per Department
* Top 10 Students
* Marks vs Attendance
* Topper Department Contribution

Charts are stored in:

```text
charts/
```

---

 🛠️ Technologies Used

 Programming Language

* Python 3

 Database

* MySQL

 Libraries

* Pandas
* Matplotlib
* MySQL Connector Python

---

 📂 Project Structure

```text
student-performance-analytics/
│
├── charts/
│   ├── students_per_department.png
│   ├── average_marks_department.png
│   ├── average_attendance_department.png
│   ├── high_performer_percentage.png
│   ├── top_10_students.png
│   ├── attendance_vs_marks.png
│   └── topper_department_contribution.png
│
├── reports/
│   ├── students_per_department.csv
│   ├── average_marks_department.csv
│   ├── average_attendance_department.csv
│   ├── high_performer_percentage.csv
│   ├── top_10_students.csv
│   ├── topper_details.csv
│   ├── topper_department_contribution.csv
│   └── marks_vs_attendance.csv
│
├── sql/
│   ├── schema.sql
│   └── sample_data.sql
│
├── src/
│   ├── database.py
│   ├── data_loader.py
│   ├── analyzer.py
│   ├── visualizer.py
│   └── main.py
│
├── requirements.txt
└── README.md
```

---

 ⚙️ Installation

 Clone Repository

```bash
git clone https://github.com/your-username/student-performance-analytics.git

cd student-performance-analytics
```

---

 Create Virtual Environment

```bash
python -m venv venv
```

Activate:

 Windows

```bash
venv\Scripts\activate
```

 Linux / Mac

```bash
source venv/bin/activate
```

---

 Install Dependencies

```bash
pip install -r requirements.txt
```

---

 🗄️ Database Setup

Create the database:

```sql
CREATE DATABASE studentperformanceanalyticssystem;
```

Execute:

```sql
schema.sql
```

Then load sample data:

```sql
sample_data.sql
```

Update MySQL credentials inside:

```python
database.py
```

```python
host="localhost"
user="root"
password="your_password"
database="studentperformanceanalyticssystem"
```

---

 ▶️ Running the Project

Run:

```bash
python src/main.py
```

---

 📋 Menu Options

```text
1. Students Per Department
2. Average Marks Per Department
3. High Performer Percentage
4. Average Attendance Per Department
5. Top 10 Students
6. Attendance vs Marks
7. Topper Department Contribution
8. Export All Reports
9. Export All Charts
10. Exit
```

---

 📈 Example Analytics Performed

* Department-wise student distribution
* Department performance comparison
* Attendance trend analysis
* Academic performance ranking
* Top performer identification
* Correlation between attendance and marks
* Department contribution to top performers

---

 🎯 Learning Outcomes

This project helped demonstrate:

 Python

* Functions
* Modules
* File Handling
* Project Structuring

 Pandas

* DataFrames
* GroupBy Operations
* Filtering
* Aggregation
* Merging DataFrames

 SQL

* Database Design
* Data Retrieval
* Relationships
* Querying

 Data Visualization

* Bar Charts
* Horizontal Bar Charts
* Pie Charts
* Scatter Plots

 Software Development

* Modular Design
* Report Generation
* Data Analytics Workflow
* Portfolio Project Development

---

 🔮 Future Improvements

Planned Version 2 Features:

* Tkinter GUI Dashboard
* Student Search Feature
* Department Filters
* Interactive Charts
* PDF Report Generation
* User Authentication
* Real-Time Data Updates
* Advanced Analytics Dashboard

---

👨‍💻 Author

Developed as a Data Analytics and Python Portfolio Project.

Focus Areas:

* Python Programming
* SQL & Databases
* Data Analysis
* Data Visualization
* Data Science Preparation
* Placement-Oriented Projects

---

Screenshots

Screenshots will be added after the GUI version of the project is completed.


⭐ If You Like This Project

Consider giving the repository a star and sharing feedback.
