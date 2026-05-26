from tkinter import *
from tkinter import messagebox
import os

FILE_NAME = "students.txt"



# FILE FUNCTIONS

def add_student():
    name = name_entry.get().strip()
    student_id = id_entry.get().strip()
    age = age_entry.get().strip()
    grade = grade_entry.get().strip()

    # Validation
    if name == "" or student_id == "" or age == "" or grade == "":
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        age = int(age)
        grade = float(grade)
    except ValueError:
        messagebox.showerror("Error", "Age must be integer and Grade must be number!")
        return

    # Check duplicate ID
    students = read_students_data()

    for student in students:
        if student["id"] == student_id:
            messagebox.showerror("Error", "Student ID already exists!")
            return

    # Save to file
    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{student_id},{age},{grade}\n")

    messagebox.showinfo("Success", "Student added successfully!")

    clear_fields()
    display_students()


def read_students_data():
    students = []

    if not os.path.exists(FILE_NAME):
        return students

    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip()

            if line:
                name, student_id, age, grade = line.split(",")

                student = {
                    "name": name,
                    "id": student_id,
                    "age": age,
                    "grade": grade
                }

                students.append(student)

    return students


def display_students():
    listbox.delete(0, END)

    students = read_students_data()

    if not students:
        listbox.insert(END, "No records found.")
        return

    for student in students:
        display_text = (
            f"Name: {student['name']} | "
            f"ID: {student['id']} | "
            f"Age: {student['age']} | "
            f"Grade: {student['grade']}"
        )

        listbox.insert(END, display_text)


def search_student():
    target_id = id_entry.get().strip()

    if target_id == "":
        messagebox.showerror("Error", "Enter Student ID to search!")
        return

    students = read_students_data()

    found = False

    listbox.delete(0, END)

    for student in students:
        if student["id"] == target_id:
            display_text = (
                f"Name: {student['name']} | "
                f"ID: {student['id']} | "
                f"Age: {student['age']} | "
                f"Grade: {student['grade']}"
            )

            listbox.insert(END, display_text)
            found = True
            break

    if not found:
        messagebox.showinfo("Search Result", "Student not found!")


def update_student():
    target_id = id_entry.get().strip()

    if target_id == "":
        messagebox.showerror("Error", "Enter Student ID to update!")
        return

    students = read_students_data()

    updated = False

    for student in students:
        if student["id"] == target_id:

            new_name = name_entry.get().strip()
            new_age = age_entry.get().strip()
            new_grade = grade_entry.get().strip()

            if new_name != "":
                student["name"] = new_name

            if new_age != "":
                try:
                    int(new_age)
                    student["age"] = new_age
                except ValueError:
                    messagebox.showerror("Error", "Age must be integer!")
                    return

            if new_grade != "":
                try:
                    float(new_grade)
                    student["grade"] = new_grade
                except ValueError:
                    messagebox.showerror("Error", "Grade must be number!")
                    return

            updated = True
            break

    if updated:
        with open(FILE_NAME, "w") as file:
            for student in students:
                file.write(
                    f"{student['name']},"
                    f"{student['id']},"
                    f"{student['age']},"
                    f"{student['grade']}\n"
                )

        messagebox.showinfo("Success", "Student updated successfully!")

        clear_fields()
        display_students()

    else:
        messagebox.showerror("Error", "Student ID not found!")


def delete_student():
    target_id = id_entry.get().strip()

    if target_id == "":
        messagebox.showerror("Error", "Enter Student ID to delete!")
        return

    students = read_students_data()

    new_students = []
    deleted = False

    for student in students:
        if student["id"] == target_id:
            deleted = True
        else:
            new_students.append(student)

    if deleted:
        with open(FILE_NAME, "w") as file:
            for student in new_students:
                file.write(
                    f"{student['name']},"
                    f"{student['id']},"
                    f"{student['age']},"
                    f"{student['grade']}\n"
                )

        messagebox.showinfo("Success", "Student deleted successfully!")

        clear_fields()
        display_students()

    else:
        messagebox.showerror("Error", "Student ID not found!")


def read_students_data():
    """Read student records from the data file."""
    if not os.path.exists(FILE_NAME):
        return []

    students = []
    with open(FILE_NAME, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            parts = line.split(",")
            if len(parts) != 4:
                continue

            students.append({
                "name": parts[0],
                "id": parts[1],
                "age": parts[2],
                "grade": parts[3],
            })

    return students


def add_student():
    """Add a new student record to the file."""
    name = name_entry.get().strip()
    student_id = id_entry.get().strip()
    age = age_entry.get().strip()
    grade = grade_entry.get().strip()

    if not name or not student_id or not age or not grade:
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        int(age)
    except ValueError:
        messagebox.showerror("Error", "Age must be an integer!")
        return

    try:
        float(grade)
    except ValueError:
        messagebox.showerror("Error", "Grade must be a number!")
        return

    students = read_students_data()
    if any(student["id"] == student_id for student in students):
        messagebox.showerror("Error", "Student ID already exists!")
        return

    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{student_id},{age},{grade}\n")

    messagebox.showinfo("Success", "Student added successfully!")
    clear_fields()
    display_students()


def compute_average():
    """Compute and display the average grade of all students."""
    students = read_students_data()
    if not students:
        messagebox.showinfo("Average Grade", "No student records available.")
        return

    grades = []
    for student in students:
        try:
            grades.append(float(student["grade"]))
        except ValueError:
            continue

    if not grades:
        messagebox.showinfo("Average Grade", "No valid grade values found.")
        return

    average = sum(grades) / len(grades)
    messagebox.showinfo("Average Grade", f"Average grade: {average:.2f}")


def show_grade_graph():
    """Display a simple bar graph of student grades."""
    students = read_students_data()
    if not students:
        messagebox.showinfo("Graph", "No student records available.")
        return

    grades = []
    names = []
    for student in students:
        try:
            grades.append(float(student["grade"]))
            names.append(student["name"])
        except ValueError:
            continue

    if not grades:
        messagebox.showinfo("Graph", "No valid grade values available.")
        return

    graph_window = Toplevel(root)
    graph_window.title("Grade Graph")
    graph_window.geometry("760x420")

    canvas = Canvas(graph_window, width=740, height=380, bg="white")
    canvas.pack(padx=10, pady=10)

    margin_x = 60
    margin_y = 40
    chart_width = 660
    chart_height = 300
    max_grade = max(grades + [100])
    bar_width = chart_width / max(len(grades), 1)

    canvas.create_line(margin_x, margin_y, margin_x, margin_y + chart_height, width=2)
    canvas.create_line(margin_x, margin_y + chart_height, margin_x + chart_width, margin_y + chart_height, width=2)

    for i, grade in enumerate(grades):
        x0 = margin_x + i * bar_width + 10
        x1 = x0 + bar_width * 0.7
        y1 = margin_y + chart_height
        y0 = y1 - (grade / max_grade) * chart_height

        canvas.create_rectangle(x0, y0, x1, y1, fill="#4caf50", outline="#2e7d32")
        canvas.create_text((x0 + x1) / 2, y0 - 10, text=f"{grade:.1f}", font=("Arial", 8), fill="#333")
        canvas.create_text((x0 + x1) / 2, y1 + 12, text=names[i][:10], font=("Arial", 8), fill="#333")

    for step in range(0, 6):
        y = margin_y + chart_height - step * (chart_height / 5)
        value = int(max_grade * step / 5)
        canvas.create_line(margin_x - 5, y, margin_x, y, width=1)
        canvas.create_text(margin_x - 10, y, text=str(value), anchor=E, font=("Arial", 8))


def clear_fields():
    """Clear all input fields in the form."""
    name_entry.delete(0, END)
    id_entry.delete(0, END)
    age_entry.delete(0, END)
    grade_entry.delete(0, END)
    id_entry.focus_set()


# GUI FUNCTIONS



# TKINTER WINDOW


root = Tk()
root.title("Student Management System")
root.geometry("800x500")
root.config(bg="white")

# LABELS

title_label = Label(
    root,
    text="USTP Student ID System",
    font=("Arial", 20, "bold"),
    bg="white"
)

title_label.grid(row=0, column=0, columnspan=2, pady=20)

Label(root, text="Name:", bg="white", font=("Arial", 12)).grid(row=1, column=0, sticky=E, padx=(10, 5), pady=5)
Label(root, text="Student ID:", bg="white", font=("Arial", 12)).grid(row=2, column=0, sticky=E, padx=(10, 5), pady=5)
Label(root, text="Age:", bg="white", font=("Arial", 12)).grid(row=3, column=0, sticky=E, padx=(10, 5), pady=5)
Label(root, text="Grade:", bg="white", font=("Arial", 12)).grid(row=4, column=0, sticky=E, padx=(10, 5), pady=5)

# ENTRY FIELDS

name_entry = Entry(root, width=30, font=("Arial", 12), bd=3, relief="solid")
id_entry = Entry(root, width=30, font=("Arial", 12), bd=3, relief="solid")
age_entry = Entry(root, width=30, font=("Arial", 12), bd=3, relief="solid")
grade_entry = Entry(root, width=30, font=("Arial", 12), bd=3, relief="solid")

name_entry.grid(row=1, column=1, padx=(0, 10), pady=5, sticky=W)
id_entry.grid(row=2, column=1, padx=(0, 10), pady=5, sticky=W)
age_entry.grid(row=3, column=1, padx=(0, 10), pady=5, sticky=W)
grade_entry.grid(row=4, column=1, padx=(0, 10), pady=5, sticky=W)

# BUTTONS

Button(root, text="Add Student", width=20, bg="green", fg="white",
       command=add_student).grid(row=5, column=0, pady=10)

Button(root, text="Display Students", width=20, bg="blue", fg="white",
       command=display_students).grid(row=5, column=1, pady=10)

Button(root, text="Search Student", width=20, bg="orange", fg="white",
       command=search_student).grid(row=6, column=0, pady=10)

Button(root, text="Update Student", width=20, bg="purple", fg="white",
       command=update_student).grid(row=6, column=1, pady=10)

Button(root, text="Delete Student", width=20, bg="red", fg="white",
       command=delete_student).grid(row=7, column=0, pady=10)

Button(root, text="Compute Average", width=20, bg="black", fg="white",
       command=compute_average).grid(row=7, column=1, pady=10)

Button(root, text="Clear Fields", width=20, bg="gray", fg="white",
       command=clear_fields).grid(row=8, column=0, pady=10)

Button(root, text="Show Grade Graph", width=20, bg="#005f73", fg="white",
       command=show_grade_graph).grid(row=8, column=1, pady=10)

# LISTBOX

listbox = Listbox(root, width=100, height=12, font=("Arial", 10))
listbox.grid(row=9, column=0, columnspan=2, padx=10, pady=20)

# RUN PROGRAM

root.mainloop()