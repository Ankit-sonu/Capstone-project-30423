import operations
import report

def get_marks():
    try:
        marks = input("Enter marks separated: ")
        marks_list = marks.split()
        result = []
        for m in marks_list:
            result.append(int(m))
        return result
    except:
        print("Invalid input. Try again.")
        return get_marks()
def menu():
    while True:
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Print Report")
        print("5. Sort Students")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == '1':
            name = input("Enter student name: ")
            marks = get_marks()
            operations.add_student(name, marks)

        elif choice == '2':
            name = input("Enter student name to update: ")
            marks = get_marks()
            operations.update_student(name, marks)

        elif choice == '3':
            name = input("Enter student name to delete: ")
            operations.delete_student(name)

        elif choice == '4':
            report.print_report()

        elif choice == '5':
            operations.sort_students()


        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select from 1 to 6.")

menu()
