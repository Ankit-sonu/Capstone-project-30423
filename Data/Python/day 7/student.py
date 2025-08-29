class Student:
    def __init__(self, roll_no, name, branch):
        self.roll_no = roll_no
        self.name    = name
        self.branch  = branch

    def __str__(self):
        return f"{self.roll_no}: {self.name} ({self.branch})"

s1 = Student(101, "A",  "CSE")
s2 = Student(102, "B","ECE")
s3 = Student(103, "C",  "ME")

students_list  = [s1, s2, s3]          
students_tuple = (s1, s2, s3)          
students_set   = {s1, s2, s3}          

print("List   :", students_list)
print("Tuple  :", students_tuple)
print("Set    :", students_set)
