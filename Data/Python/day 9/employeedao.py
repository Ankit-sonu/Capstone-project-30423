import mysql.connector


class EmployeeDao:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Password@1",
            database="training"
        )
        self.cursor = self.conn.cursor()


    def add_employee(self, employees):
        sql = "insert into employeetl(empid,name,age,dept,notes,salary,remarks) values (%s,%s,%s,%s,%s,%s,%s)"
        #values = (employee.empid,employee.name,employee.age,employee.dept,employee.notes,employee.salary,employee.remarks)
        self.cursor.executemany(sql, employees)
        self.conn.commit()