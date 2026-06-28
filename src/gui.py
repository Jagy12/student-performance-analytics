from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from analyzer import (
    students_per_department,
    average_marks_per_department,
    top_ten,
    topper
)
from visualizer import (students_per_department_chart,
    average_marks_per_department_chart,
    top_10_students_chart)


## Functions For Analysis & Visualisation:👇

def clear_visualization():
    widgets = visualize_frame.winfo_children()

    for widget in widgets:
        if widget != visualize:
            widget.destroy()

def display_chart(fig):

    clear_visualization()

    canvas = FigureCanvasTkAgg(
        fig,
        master=visualize_frame
    )

    canvas.draw()
    plt.close(fig)

    canvas.get_tk_widget().grid(
    column=0,
    row=1,
    sticky="nsew",
    padx=10,
    pady=10
)
    
def show_students_per_department():

    result = students_per_department()
    output.delete("1.0", END)
    output.insert(
        END,
        "Here are the number of students in each department:\n\n"
    )
    for dept, count in result.items():
        output.insert(END, f"{dept} ---> {count}\n")

    fig = students_per_department_chart()
    display_chart(fig)

def show_average_marks_per_department():

    result = average_marks_per_department()
    output.delete("1.0", END)
    output.insert(
        END,
        "Here are the average marks of students in each department:\n\n"
    )
    for dept, marks in result.items():
        output.insert(END, f"{dept} ---> {marks: .2f}\n")

    fig = average_marks_per_department_chart()
    display_chart(fig)
def show_top_ten():

    result = top_ten()
    output.delete("1.0", END)

    output.insert(
    END,
    "Here are the details of top 10 students:\n\n"
)

    for _, row in result.iterrows():
        output.insert(
        END,
        f"{row['student_id']} --> "
        f"{row['student_name']} --> "
        f"{row['department_id']} --> "
        f"{row['average_marks']:.2f}\n"
    )
    fig = top_10_students_chart()
    display_chart(fig)

def show_topper():
    clear_visualization()
    topper_mark, topper_id, topper_details = topper()

    output.delete("1.0", END)

    output.insert(
        END,
        "🏆 Top Performing Student\n\n"
    )

    for _, row in topper_details.iterrows():

        output.insert(
            END,
            f"Marks      : {topper_mark:.2f}\n"
            f"Student ID : {topper_id}\n"
            f"Topper Name : {row['student_name']}\n"        
            f"Department ID : {row['department_id']}\n"        
            f"Department Name : {row['department_name']}\n"        
            f"Major : {row['major']}\n" 
        )       


window = Tk()
window.state("zoomed")
window.minsize(1200,700)

window.title('STUDENT PERFORMANCE ANALYTICS SYSTEM')

## FRAMES 👇

head_frame = Frame(window,
                   relief='solid')
left_frame = Frame(window,
                   bd=2,
                   relief='solid')
right_frame = Frame(window,
                   bd=2,
                   relief='solid')

## SUB FRAME 👇

analysis_frame = Frame(right_frame,
                       bd=2,
                       relief='solid')

visualize_frame = Frame(right_frame,
                       bd=2,
                       relief='solid')

## FRAME PLACEMENT👇

head_frame.grid_columnconfigure(0, weight=1)
head_frame.grid(column=0,
                row=0,
                columnspan=2)

left_frame.grid(column=0,
                row=1,
                sticky='ns')

right_frame.grid_columnconfigure(0, weight=1)
right_frame.grid_columnconfigure(1, weight=3)

right_frame.grid_rowconfigure(1, weight=1)
right_frame.grid(column=1,
                 row=1,
                sticky='nsew')


analysis_frame.grid_columnconfigure(0, weight=1)
analysis_frame.grid_rowconfigure(1, weight=1)

analysis_frame.grid(column=0,row=1, sticky="nsew")
visualize_frame.grid(column=1,row=1, sticky="nsew")

visualize_frame.grid_columnconfigure(0, weight=1)
visualize_frame.grid_rowconfigure(1, weight=1)

window.grid_rowconfigure(1,weight=1)
window.grid_columnconfigure(1,weight=1)


## LABEL WIDGET 👇

## HEADING👇

heading = Label(head_frame,
              text=' Student Performance Analytics System',
              font=("Arial", 18, "bold"))

heading.grid(column=0,
             row=0,
             sticky='ew',
             pady=10)

## LEFT MENU👇

menu = Label(left_frame,
              text=' MENU',
              font=("Arial", 14, "bold"),
              padx=10,
              pady=10)

menu.grid(column=0,row=0)

## OUTPUT AREA👇

output_label = Label(right_frame,
              text=' OUTPUT AREA',
              font=("Arial", 14, "bold"),
              padx=10,
              pady=10)
output_label.grid(column=0,
            row=0
)

analysis = Label(analysis_frame,
                 text='Analysis',
                 font=('Arial', 14, 'bold'))
analysis.grid(column=0, row=0)

visualize = Label(visualize_frame,
                 text='Visualization',
                 font=('Arial', 14, 'bold'))
visualize.grid(column=0, row=0)


## TEXT WIDGET👇

output = Text(
    analysis_frame
)
output.grid(column=0,
            row=1,
            sticky='nsew'
)
output.config(font=("Consolas", 11))

## BUTTONS👇
#1.
student_per_dept_button = Button(left_frame,
                 text= 'Students per Department',
                 command=show_students_per_department,
                 fg = 'Black',
                 width=25
                 )
student_per_dept_button.grid(column=0,
                             row=1,
                             padx=10,
                             pady=5)

#2.
average_marks_per_dept_button = Button(left_frame,
                 text= 'Average Marks per Department',
                 command=show_average_marks_per_department,
                 fg = 'Black',
                 width=25
                 )
average_marks_per_dept_button.grid(column=0,
                             row=2,
                             padx=10,
                             pady=5)

#3.
top_ten_button = Button(left_frame,
                 text= 'Top 10 Students',
                 command=show_top_ten,
                 fg = 'Black',
                 width=25
                 )
top_ten_button.grid(column=0,
                             row=3,
                             padx=10,
                             pady=5)

#4.
show_topper_button = Button(left_frame,
                 text= 'Topper',
                 command=show_topper,
                 fg = 'Black',
                 width=25
                 )
show_topper_button.grid(column=0,
                             row=4,
                             padx=10,
                             pady=5)


exit_button = Button(left_frame,
                 text= 'Exit',
                 fg = 'Black',
                 width=25,
                 command=window.destroy)

exit_button.grid(column=0,
                 row=5,
                 padx=10,
                 pady=5)


if __name__ == "__main__":
    window.mainloop()




