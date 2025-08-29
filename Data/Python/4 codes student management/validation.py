def validate_marks(marks):
    for mark in marks:
        if mark < 0 or mark > 100:
            print("Invalid mark:", mark)
            return False
    return True