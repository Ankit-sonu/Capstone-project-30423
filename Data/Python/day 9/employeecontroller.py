from employeeetl.employeeservice import EmployeeService

if __name__ == '__main__':
    service = EmployeeService()
    employeerawdata = service.read_from_excel("employeesdata.xlsx")
    cleaneddata = service.clean_employee_data(employeerawdata)
    service.load_employee_data_todb(cleaneddata)
    print("The data is cleaned and loaded to db")