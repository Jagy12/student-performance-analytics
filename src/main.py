from visualizer import *

while True:

    print("\n===== STUDENT PERFORMANCE ANALYTICS =====")
    print("1. Students Per Department")
    print("2. Average Marks Per Department")
    print("3. High Performer Percentage")
    print("4. Average Attendance Per Department")
    print("5. Top 10 Students")
    print("6. Attendance vs Marks")
    print("7. Attendance vs Marks")
    print("8. Export All Reports")
    print("9. Export All Charts")
    print("10. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":
        students_per_department_chart()
        plt.show()

    elif choice == "2":
        average_marks_per_department_chart()
        plt.show()

    elif choice == "3":
        high_performer_chart()
        plt.show()

    elif choice == "4":
        attendance_per_department_chart()
        plt.show()

    elif choice == "5":
        top_10_students_chart()
        plt.show()

    elif choice == "6":
        attendance_vs_marks_chart()
        plt.show()

    elif choice == "7":
        export_topper_department_contribution_chart()
        plt.show()

    elif choice == "8":
        export_all_reports()

    elif choice == "9":
        export_students_per_department_chart()
        export_average_marks_department_chart()
        export_high_performer_chart()
        export_average_attendance_chart()
        export_top_10_students_chart()
        export_attendance_vs_marks_chart()
        export_topper_department_contribution_chart()

    elif choice == "10":
        print("Goodbye!")
        break