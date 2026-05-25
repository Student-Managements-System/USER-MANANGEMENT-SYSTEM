from tkinter import *
from tkinter import messagebox
import os

FILE_NAME = "students.txt"



# FILE FUNCTIONS




# GUI FUNCTIONS



# TKINTER WINDOW


root = Tk()
root.title("Student Management System")
root.geometry("800x500")
root.config(bg="white")

# LABELS

title_label = Label(
    root,
    text="Student Management System",
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