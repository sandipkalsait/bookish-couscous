# Assignment 4 - MSI Report on Existing CRUD Application

## Existing CRUD Application: Employee Management

This report examines the functionality of the existing Employee Management CRUD (Create, Read, Update, Delete) application, which helps in managing employee records in an organization.


### Employee Template
An employee record consists of the following data:
- **EmployeeId** (unique identifier)
- **Name** (employee's name)
- **Dept** (department the employee works in)
- **Salary** (employee's salary)

```python
employee_template = {
    "1001": {"Name": "Rahul Sharma", "Dept": "IT", "Salary": 50000},
    "1002": {"Name": "Priya Singh", "Dept": "HR", "Salary": 45000},
    "1003": {"Name": "Amit Kumar", "Dept": "Sales", "Salary": 40000}
}
```

### Questions for the Employees

1. **Department-wise Employee Count**  
   - Objective: Display the total number of employees in each department.
   

2. **Display Employees from a Specific Department**  
   - Objective: Show all employees belonging to a particular department as selected by the user.
  

3. **Display Top 3 Salaries with Complete Employee Details**  
   - Objective: List the top 3 highest-paid employees along with their full details (name, role, department, etc.).
   - If multiple employees share the same salary, the system will showcase all employees with that salary.  
   - This ensures that even if more than 3 employees have the same top salary, they will all be displayed in the results.

