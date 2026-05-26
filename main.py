# VELEZ
def compute_average():
    students = read_students_data()

    if not students:
        messagebox.showinfo(
            "Average",
            "No student records found!"
        )
        return

    total = 0

    for student in students:
        total += float(student["grade"])

    average = total / len(students)

    messagebox.showinfo(
        "Average Grade",
        f"Average Grade: {average:.2f}"
    )