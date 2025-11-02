from database import MongoDBConnection, EmployeeCRUD

def print_main_menu():
    print("""
    #------------- MongoDB Employee CRUD System -----------#
    1. Add Employee
    2. Update Employee
    3. Delete Employee
    4. List All Employees
    5. Get Employees by Department
    6. Department Statistics
    0. Exit
    """)

def print_department_statistics(crud):
    """Display department statistics"""
    print("\n--- Department Statistics ---")
    try:
        pipeline = [
            {
                "$group": {
                    "_id": "$dept",
                    "total_employees": {"$sum": 1},
                    "avg_salary": {"$avg": "$salary"},
                    "max_salary": {"$max": "$salary"},
                    "min_salary": {"$min": "$salary"}
                }
            },
            {
                "$project": {
                    "department": "$_id",
                    "total_employees": 1,
                    "avg_salary": {"$round": ["$avg_salary", 2]},
                    "max_salary": 1,
                    "min_salary": 1,
                    "_id": 0
                }
            }
        ]
        
        stats = list(crud.employees.aggregate(pipeline))
        
        if not stats:
            print("No data available!")
            return
        
        print(f"{'Department':<12} {'Total Emp':<12} {'Avg Salary':<12} {'Max Salary':<12} {'Min Salary':<12}")
        print("-" * 60)
        for stat in stats:
            print(f"{stat['department']:<12} {stat['total_employees']:<12} {stat['avg_salary']:<12} {stat['max_salary']:<12} {stat['min_salary']:<12}")
    
    except Exception as e:
        print(f"Error generating statistics: {e}")

def main():
    # Initialize database connection
    db_connection = MongoDBConnection()
    
    if not db_connection.connect():
        print("Failed to connect to database. Exiting...")
        return
    
    # Initialize CRUD operations
    crud = EmployeeCRUD(db_connection)
    
    # Menu options mapping
    menu_functions = {
        1: crud.add_employee,
        2: crud.update_employee,
        3: crud.delete_employee,
        4: crud.list_employees,
        5: crud.get_employees_by_department,
        6: lambda: print_department_statistics(crud)
    }
    
    while True:
        print_main_menu()
        choice = input("Enter your choice: ").strip()
        
        if not choice.isdigit():
            print("Please enter a valid number!")
            continue
        
        choice = int(choice)
        
        if choice == 0:
            print("Exiting program...")
            break
        elif choice in menu_functions:
            try:
                menu_functions[choice]()
            except Exception as e:
                print(f"Error executing operation: {e}")
        else:
            print("Invalid choice! Please try again.")
    
    # Close database connection
    db_connection.close()

if __name__ == "__main__":
    main()






"""
Output
PS C:\Users\kalsa\OneDrive\Backup storage\OneDrive\Desktop\MSc computer science\bookish-couscous\python\practical-assignment-11> pip install -r requirement.txt
Collecting pymongo (from -r requirement.txt (line 1))
  Downloading pymongo-4.15.3-cp311-cp311-win_amd64.whl.metadata (22 kB)
Collecting dnspython<3.0.0,>=1.16.0 (from pymongo->-r requirement.txt (line 1))
  Downloading dnspython-2.8.0-py3-none-any.whl.metadata (5.7 kB)
Downloading pymongo-4.15.3-cp311-cp311-win_amd64.whl (859 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 859.2/859.2 kB 6.0 MB/s eta 0:00:00
Downloading dnspython-2.8.0-py3-none-any.whl (331 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 331.1/331.1 kB 6.8 MB/s eta 0:00:00
Installing collected packages: dnspython, pymongo
Successfully installed dnspython-2.8.0 pymongo-4.15.3

[notice] A new release of pip is available: 24.0 -> 25.3
[notice] To update, run: C:\Users\kalsa\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\python.exe -m pip install --upgrade pip
PS C:\Users\kalsa\OneDrive\Backup storage\OneDrive\Desktop\MSc computer science\bookish-couscous\python\practical-assignment-11> python main.py                
Connected to MongoDB successfully!
Departments initialized successfully!

    #------------- MongoDB Employee CRUD System -----------#
    1. Add Employee
    2. Update Employee
    3. Delete Employee
    4. List All Employees
    5. Get Employees by Department
    6. Department Statistics
    0. Exit

Enter your choice: 1

--- Add New Employee ---
Enter Employee ID (4-digit): 83993
Error: Invalid Employee ID. Must be 4-digit number starting from 1000
Enter Employee ID (4-digit): 100
Error: Invalid Employee ID. Must be 4-digit number starting from 1000
Enter Employee ID (4-digit): 1002
Enter Employee Name: 2882
Error: Invalid Name. Only letters and spaces allowed (2-50 characters)
Enter Employee Name: Sandip Kalsait
Available Departments: HR, IT, Sales, Finance, Marketing
Enter Department: IT
Enter Salary: 900000
Enter Email: kalsaitsandip91@gmail.com
Employee 1002 added successfully!

    #------------- MongoDB Employee CRUD System -----------#
    1. Add Employee
    2. Update Employee
    3. Delete Employee
    4. List All Employees
    5. Get Employees by Department
    6. Department Statistics
    0. Exit

Enter your choice: 4

--- Employee List ---
ID       Name                 Department   Salary     Email
--------------------------------------------------------------------------------
1002     Sandip Kalsait       IT           900000     kalsaitsandip91@gmail.com

    #------------- MongoDB Employee CRUD System -----------#
    1. Add Employee
    2. Update Employee
    3. Delete Employee
    4. List All Employees
    5. Get Employees by Department
    6. Department Statistics
    0. Exit

Enter your choice: 5

--- Employees by Department ---
Enter Department name: IT

Employees in IT department:
ID       Name                 Salary     Email
-----------------------------------------------------------------
1002     Sandip Kalsait       900000     kalsaitsandip91@gmail.com

Total employees in IT: 1

    #------------- MongoDB Employee CRUD System -----------#
    1. Add Employee
    2. Update Employee
    3. Delete Employee
    4. List All Employees
    5. Get Employees by Department
    6. Department Statistics
    0. Exit

Enter your choice: 0
Exiting program...
MongoDB connection closed.
PS C:\Users\kalsa\OneDrive\Backup storage\OneDrive\Desktop\MSc computer science\bookish-couscous\python\practical-assignment-11>

 """