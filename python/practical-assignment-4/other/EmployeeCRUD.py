employee_template = {
    "1001": {"Name": "Rahul Sharma", "Dept": "IT", "Salary": 50000},
    "1002": {"Name": "Priya Singh", "Dept": "HR", "Salary": 45000},
    "1003": {"Name": "Amit Kumar", "Dept": "Sales", "Salary": 40000}
}

DEPARTMENTS = ["HR", "IT", "Sales", "Finance", "Marketing"]

def print_menu():
    print("""
            #------------- Employee CRUD Menu -----------#
            1. Add Employee
            2. Update Employee
            3. Delete Employee
            4. Print Employee Records
            0. Exit
            """)

def is_exist(employees, EmployeeId):
    return EmployeeId in employees

def add_employee(employees):
    while True:
        EmployeeId = input("Enter EmployeeId (unique, numeric): ").strip()
        if not EmployeeId.isdigit():
            print("EmployeeId must be numeric.")
            continue
        if is_exist(employees, EmployeeId):
            print("EmployeeId already exists!")
            continue
        name = input("Enter Employee Name: ").strip()
        if not name.replace(" ", "").isalpha():
            print("Invalid name. Only letters allowed.")
            continue
        print("Departments:", ", ".join(DEPARTMENTS))
        dept = input("Enter Department: ").strip()
        if dept not in DEPARTMENTS:
            print("Invalid department.")
            continue
        salary = input("Enter Salary (numeric): ").strip()
        if not salary.isdigit():
            print("Salary must be numeric.")
            continue
        employees[EmployeeId] = {"Name": name, "Dept": dept, "Salary": int(salary)}
        print(f"Employee {EmployeeId} added successfully.")
        more = input("Want to add another employee? YES/NO: ").strip().lower()
        if more != 'yes':
            break
    return employees

def update_employee(employees):
    while True:
        EmployeeId = input("Enter EmployeeId to update: ").strip()
        if not is_exist(employees, EmployeeId):
            print("EmployeeId not found!")
            more = input("Try another EmployeeId? YES/NO: ").strip().lower()
            if more != 'yes':
                break
            continue
        print("Leave blank to keep current value.")
        name = input(f"Enter new Name ({employees[EmployeeId]['Name']}): ").strip()
        if name:
            if name.replace(" ", "").isalpha():
                employees[EmployeeId]["Name"] = name
            else:
                print("Invalid name. Keeping previous.")
        print("Departments:", ", ".join(DEPARTMENTS))
        dept = input(f"Enter new Dept ({employees[EmployeeId]['Dept']}): ").strip()
        if dept and dept in DEPARTMENTS:
            employees[EmployeeId]["Dept"] = dept
        elif dept:
            print("Invalid department. Keeping previous.")
        salary = input(f"Enter new Salary ({employees[EmployeeId]['Salary']}): ").strip()
        if salary and salary.isdigit():
            employees[EmployeeId]["Salary"] = int(salary)
        elif salary:
            print("Invalid salary. Keeping previous.")
        print(f"Employee {EmployeeId} updated successfully.")
        more = input("Want to update another employee? YES/NO: ").strip().lower()
        if more != 'yes':
            break
    return employees

def delete_employee(employees):
    while True:
        EmployeeId = input("Enter EmployeeId to delete: ").strip()
        if is_exist(employees, EmployeeId):
            del employees[EmployeeId]
            print(f"Employee {EmployeeId} deleted.")
        else:
            print("EmployeeId not found!")
        more = input("Delete another employee? YES/NO: ").strip().lower()
        if more != 'yes':
            break
    return employees

def print_employees(employees):
    if not employees:
        print("No employee records found.")
    else:
        print("\nEmployee Records:")
        for EmployeeId, record in employees.items():
            print(f"{EmployeeId}: {record}")

# def main():
#     employees = employee_template.copy()
#     functions = {
#         1: add_employee,
#         2: update_employee,
#         3: delete_employee,
#         4: print_employees
#     }
#     while True:
#         print_menu()
#         choice = input("Enter your choice: ").strip()
#         if not choice.isdigit():
#             print("Please enter a number.")
#             continue
#         choice = int(choice)
#         if choice == 0:
#             print("Exiting program...")
#             break
#         elif choice in functions:
#             functions[choice](employees)
#         else:
#             print("Invalid choice.")

# main()









# Result

# PS C:\Users\kalsa\OneDrive\Backup storage\OneDrive\Desktop\MSc computer science\bookish-couscous> & C:/Users/kalsa/AppData/Local/Microsoft/WindowsApps/python3.11.exe "c:/Users/kalsa/OneDrive/Backup storage/OneDrive/Desktop/MSc computer science/bookish-couscous/python/practical-assignment-3/Question3.py"
#             #------------- Employee CRUD Menu -----------#
#             1. Add Employee
#             2. Update Employee
#             3. Delete Employee
#             4. Print Employee Records
#             0. Exit

# Enter your choice: 1
# Enter EmployeeId (unique, numeric): 1001
# EmployeeId already exists!
# Enter EmployeeId (unique, numeric): 1002
# EmployeeId already exists!
# Enter EmployeeId (unique, numeric): 1003
# EmployeeId already exists!
# Enter EmployeeId (unique, numeric): 1005
# Enter Employee Name: Sandip Kalsait
# Departments: HR, IT, Sales, Finance, Marketing
# Enter Department: IT 
# Enter Salary (numeric): 45000
# Employee 1005 added successfully.
# Want to add another employee? YES/NO: no

#             #------------- Employee CRUD Menu -----------#
#             1. Add Employee
#             2. Update Employee
#             3. Delete Employee
#             4. Print Employee Records
#             0. Exit

# Enter your choice: 4

# Employee Records:
# 1001: {'Name': 'Rahul Sharma', 'Dept': 'IT', 'Salary': 50000}
# 1002: {'Name': 'Priya Singh', 'Dept': 'HR', 'Salary': 45000}
# 1003: {'Name': 'Amit Kumar', 'Dept': 'Sales', 'Salary': 40000}
# 1005: {'Name': 'Sandip Kalsait', 'Dept': 'IT', 'Salary': 45000}

#             #------------- Employee CRUD Menu -----------#
#             1. Add Employee
#             2. Update Employee
#             3. Delete Employee
#             4. Print Employee Records
#             0. Exit

# Enter your choice: 2
# Enter EmployeeId to update: 2
# EmployeeId not found!
# Try another EmployeeId? YES/NO: yes
# Enter EmployeeId to update: 1002
# Leave blank to keep current value.
# Enter new Name (Priya Singh): Priya Kalsait
# Departments: HR, IT, Sales, Finance, Marketing
# Enter new Dept (HR): IT
# Enter new Salary (45000): 50000
# Employee 1002 updated successfully.
# Want to update another employee? YES/NO: no

#             #------------- Employee CRUD Menu -----------#
#             1. Add Employee
#             2. Update Employee
#             3. Delete Employee
#             4. Print Employee Records
#             0. Exit

# Enter your choice: 3
# Enter EmployeeId to delete: 1002
# Employee 1002 deleted.
# Delete another employee? YES/NO: 4

#             #------------- Employee CRUD Menu -----------#
#             1. Add Employee
#             2. Update Employee
#             3. Delete Employee
#             4. Print Employee Records
#             0. Exit

# Enter your choice: 4

# Employee Records:
# 1001: {'Name': 'Rahul Sharma', 'Dept': 'IT', 'Salary': 50000}
# 1003: {'Name': 'Amit Kumar', 'Dept': 'Sales', 'Salary': 40000}
# 1005: {'Name': 'Sandip Kalsait', 'Dept': 'IT', 'Salary': 45000}

#             #------------- Employee CRUD Menu -----------#
#             1. Add Employee
#             2. Update Employee
#             3. Delete Employee
#             4. Print Employee Records
#             0. Exit

# Enter your choice: