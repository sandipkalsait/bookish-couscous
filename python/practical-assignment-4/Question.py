import EmployeeCRUD

employees = EmployeeCRUD.employee_template.copy()

# Department-wise Employee Count
def department_wise_count(employees):
    dept_count = {}
    for employee in employees.values():
        dept_count[employee['Dept']] = dept_count.get(employee['Dept'], 0) + 1

    result = "\nDepartment-wise Employee Count:\n"
    for dept, count in dept_count.items():
        result += f"{dept}: {count} employees\n"
    return result

# Display Employees from a Specific Department
def display_employees_from_department(employees):
    print(EmployeeCRUD.DEPARTMENTS)
    dept = input("\nEnter the department name: ").strip()
    result = f"\nEmployees in {dept} Department:\n"
    found = False
    for emp_id, employee in employees.items():
        if employee['Dept'].lower() == dept.lower():
            result += f"EmployeeId: {emp_id}, Name: {employee['Name']}, Salary: {employee['Salary']}\n"
            found = True

    if not found:
        result += "No employees found in this department.\n"
    
    return result

# Display Top 3 Salaries with Complete Employee Details
def display_top_salaries(employees):
    top_salaries = []
    max_salary = '-1'

    for emp_id, employee in employees.items():
        if len(top_salaries) < 3:
            top_salaries.append((emp_id, employee))
            max_salary = employee['Salary']
        elif employee['Salary'] == max_salary:
            top_salaries.append((emp_id, employee))

    result = "\nTop Salaries with Employee Details:\n"
    for emp_id, employee in top_salaries:
        result += f"EmployeeId: {emp_id}, Name: {employee['Name']}, Dept: {employee['Dept']}, Salary: {employee['Salary']}\n"
    
    return result

def main():
    # Menu
    functions = {
        1: EmployeeCRUD.add_employee,
        2: EmployeeCRUD.update_employee,
        3: EmployeeCRUD.delete_employee,
        4: EmployeeCRUD.print_employees,
        5: department_wise_count,
        6: display_employees_from_department,
        7: display_top_salaries
        # 8: export_reports
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
            #  if choice == 8:
            #     functions[choice](employees)
            #  else:
            #     result = functions[choice](employees)
            print(result)
        else:
            print("Invalid choice. Please try again.")

# def save_report_to_file(filename, content):
#     with open(filename, "w") as file:
#         file.write(content)
#     print(f"Report saved to {filename}\n")

# def export_reports(employees):
#     print("Exporting all reports...\n")
    
#     # Generate reports
#     dept_count_report = department_wise_count(employees)
#     dept_employees_report = display_employees_from_department(employees)
#     top_salaries_report = display_top_salaries(employees)
    
#     # Save files
#     save_report_to_file("Department_Wise_Count_Report.txt", dept_count_report)
#     save_report_to_file("Employees_From_All_Departments_Report.txt", dept_employees_report)
#     save_report_to_file("Top_Salaries_Report.txt", top_salaries_report)

main()
