import EmployeeCRUD
from tabulate import tabulate

employees = EmployeeCRUD.employee_template.copy()

# Department-wise Employee Count
def department_wise_count(employees):
    dept_count = {}
    for employee in employees.values():
        dept_count[employee['Dept']] = dept_count.get(employee['Dept'], 0) + 1

    table = [(dept, count) for dept, count in dept_count.items()]
    return "\nDepartment-wise Employee Count:\n" + tabulate(table, headers=["Department", "Employee Count"], tablefmt="grid")

# Display Employees from a Specific Department
def display_employees_from_department(employees):
    print("\nAvailable Departments:")
    print(EmployeeCRUD.DEPARTMENTS)
    dept = input("\nEnter the department name: ").strip()

    filtered = [
        (emp_id, employee['Name'], employee['Salary'])
        for emp_id, employee in employees.items()
        if employee['Dept'].lower() == dept.lower()
    ]

    if not filtered:
        return f"\nNo employees found in {dept} Department.\n"

    return f"\nEmployees in {dept} Department:\n" + tabulate(filtered, headers=["EmployeeId", "Name", "Salary"], tablefmt="grid")

# Display Top 3 Salaries with Complete Employee Details
def display_top_salaries(employees):
    sorted_employees = sorted(
        employees.items(), key=lambda x: x[1]['Salary'], reverse=True
    )[:3]

    table = [
        (emp_id, emp['Name'], emp['Dept'], emp['Salary'])
        for emp_id, emp in sorted_employees
    ]

    return "\nTop 3 Salaries with Employee Details:\n" + tabulate(
        table, headers=["EmployeeId", "Name", "Department", "Salary"], tablefmt="grid"
    )

def main():
    functions = {
        1: EmployeeCRUD.add_employee,
        2: EmployeeCRUD.update_employee,
        3: EmployeeCRUD.delete_employee,
        4: EmployeeCRUD.print_employees,
        5: department_wise_count,
        6: display_employees_from_department,
        7: display_top_salaries
    }

    while True:
        print("""        
        #------------- Employee CRUD Menu -----------#
        1. Add Employee
        2. Update Employee
        3. Delete Employee
        4. Print Employee Records
        5. Department-wise Employee Count
        6. Display Employees from a Specific Department
        7. Display Top 3 Salaries with Complete Employee Details
        0. Exit
        """)
        choice = input("Enter your choice: ").strip()

        if not choice.isdigit():
            print("Please enter a valid number.")
            continue

        choice = int(choice)
        if choice == 0:
            print("Exiting program...")
            break
        elif choice in functions:
            result = functions[choice](employees)
            if result:
                print(result)
        else:
            print("Invalid choice. Please try again.")


main()
