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

# LISTBOX

listbox = Listbox(root, width=100, height=12, font=("Arial", 10))
listbox.grid(row=9, column=0, columnspan=2, padx=10, pady=20)

# RUN PROGRAM

root.mainloop()