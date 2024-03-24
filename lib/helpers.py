from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)


def find_employee_by_name():
    name = input("Enter the employee's name: ")
    employee = Employee.find_by_name(name)
    print(employee) if employee else print(
        f'Employee {name} not found')


def find_employee_by_id():
    #using a trailing underscore not to override the built-in id function
    id_ = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id_)
    print(employee) if employee else print(f'Employee {id_} not found')


def department_exists(department_id):
    department = Department.find_by_id(department_id)
    if department:
        employees = department.employees()
        if employees:
            return True
        else:
            print("Error creating employee: Department exists but has no employees.")
            return False
    else:
        print("Error creating employee: Department ID does not exist.")
        return False

def create_employee():
    name = input("Enter the employee's name: ")
    job_title = input("Enter the employee's job title: ")
    department_id = int(input("Enter the department id of the employee: "))


    if not department_exists(department_id):
        return

    try:
        employee = Employee.create(name, job_title, department_id)
        print(f'Success: {employee}')
    except ValueError as exc:
        print("Error creating employee: ", exc)


def update_employee():
    employee_id = int(input("Enter the ID of the employee to update: "))
    employee = Employee.find_by_id(employee_id)
    if not employee:
        print("Employee with the provided ID does not exist.")
        return
    new_name = input("Enter the updated name : ").strip()
    new_job_title = input("Enter the updated job title : ").strip()
    new_department_id = input("Enter the updated department id : ").strip()
    if new_name:
        employee.name = new_name
    if new_job_title:
        employee.job_title = new_job_title
    if new_department_id:
        employee.department_id = int(new_department_id)
    try:
        employee.update()
        print("Employee details updated successfully.")
    except Exception as exc:
        print("Error updating employee details:", exc)



def delete_employee():
    id_ = input("Enter the employee's id: ")
    if employee := Employee.find_by_id(id_):
        employee.delete()
        print(f'Employee {id_} deleted')
    else:
        print(f'Employee {id_} not found')


def list_department_employees():
    # Prompt user to enter the ID of the department
    department_id = int(input("Enter the ID of the department: "))

    # Checking if the department exists
    department = Department.find_by_id(department_id)
    if not department:
        print("Department with the provided ID does not exist.")
        return

    # getting employees associated with the department
    employees = department.employees()

    if not employees:
        print("No employees found in this department.")
    else:
        print(f"Employees in Department {department.name}:")
        for employee in employees:
            print(f"ID: {employee.id}, Name: {employee.name}, Job Title: {employee.job_title}")