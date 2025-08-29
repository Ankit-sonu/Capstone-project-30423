
import data_store
import validation

def add_student(name, marks):
    if validation.validate_marks(marks):
        data_store.students[name] = marks
        print("Student added successfully.")
    else:
        print("Failed")

def update_student(name, marks):
    if name in data_store.students:
        if validation.validate_marks(marks):
            data_store.students[name] = marks
            print("Marks updated.")
        else:
            print("Invalid marks.")
    else:
        print("Student not found.")

def delete_student(name):
    if name in data_store.students:
        del data_store.students[name]
        print("Student deleted.")
    else:
        print("Student not found.")

def sort_students():
    sorted_list = []
    for name in data_store.students:
        total = 0
        for mark in data_store.students[name]:
            total += mark
        sorted_list.append([name, total])

    for i in range(len(sorted_list)):
        for j in range(i + 1, len(sorted_list)):
            if sorted_list[i][1] < sorted_list[j][1]:
                temp = sorted_list[i]
                sorted_list[i] = sorted_list[j]
                sorted_list[j] = temp

    print("\nStudents sorted by total marks:")
    for entry in sorted_list:
        print("Name:", entry[0], "- Total Marks:", entry[1])