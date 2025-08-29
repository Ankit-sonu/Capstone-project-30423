import data_store

def print_report():
    if not data_store.students:
        print("No student records found.")
        return

    print("\nStudent Report")
    for name in data_store.students:
        marks = data_store.students[name]
        total = 0
        for mark in marks:
            total += mark
        average = total / len(marks)
        print("Name:", name)
        print("Marks:", marks)
        print("Total:", total)
        print("Average:", round(average, 2))
        print("-" * 30)