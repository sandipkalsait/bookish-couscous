import pymongo
import re
from datetime import datetime

class MongoDBConnection:
    def __init__(self, connection_string="mongodb://localhost:27017/", db_name="company_db"):
        self.connection_string = connection_string
        self.db_name = db_name
        self.client = None
        self.db = None
    
    def connect(self):
        try:
            self.client = pymongo.MongoClient(self.connection_string)
            self.db = self.client[self.db_name]
            print("Connected to MongoDB successfully!")
            return True
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")
            return False
    
    def close(self):
        if self.client:
            self.client.close()
            print("MongoDB connection closed.")

class EmployeeCRUD:
    def __init__(self, db_connection):
        self.db = db_connection.db
        self.employees = self.db.employees
        self.departments = self.db.departments
        
        # Predefined departments
        self.DEPARTMENTS = ["HR", "IT", "Sales", "Finance", "Marketing"]
        self.initialize_departments()
    
    def initialize_departments(self):
        """Initialize departments collection with predefined departments"""
        try:
            for dept_name in self.DEPARTMENTS:
                if not self.departments.find_one({"name": dept_name}):
                    self.departments.insert_one({
                        "name": dept_name,
                        "created_at": datetime.now()
                    })
            print("Departments initialized successfully!")
        except Exception as e:
            print(f"Error initializing departments: {e}")
    
    def validate_employee_id(self, emp_id):
        """Validate Employee ID using RE module"""
        pattern = r'^[1-9]\d{3}$'  # 4-digit number, starting from 1000
        if re.match(pattern, emp_id):
            return True, "Valid Employee ID"
        return False, "Invalid Employee ID. Must be 4-digit number starting from 1000"
    
    def validate_name(self, name):
        """Validate Employee Name using RE module"""
        pattern = r'^[A-Za-z\s]{2,50}$'  # Only letters and spaces, 2-50 characters
        if re.match(pattern, name):
            return True, "Valid Name"
        return False, "Invalid Name. Only letters and spaces allowed (2-50 characters)"
    
    def validate_salary(self, salary):
        """Validate Salary using RE module"""
        pattern = r'^[1-9]\d{0,6}$'  # 1-7 digit number, minimum 1
        if re.match(pattern, salary):
            salary_num = int(salary)
            if 10000 <= salary_num <= 1000000:  # Reasonable salary range
                return True, "Valid Salary"
            else:
                return False, "Salary must be between 10000 and 1000000"
        return False, "Invalid Salary. Must be a positive number"
    
    def validate_email(self, email):
        """Validate Email using RE module"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, email):
            return True, "Valid Email"
        return False, "Invalid Email format"
    
    def is_employee_exists(self, emp_id):
        """Check if employee exists"""
        return self.employees.find_one({"emp_id": emp_id}) is not None
    
    def is_department_exists(self, dept_name):
        """Check if department exists"""
        return self.departments.find_one({"name": dept_name}) is not None
    
    def add_employee(self):
        """Add new employee with validation"""
        print("\n--- Add New Employee ---")
        
        while True:
            emp_id = input("Enter Employee ID (4-digit): ").strip()
            is_valid, message = self.validate_employee_id(emp_id)
            if not is_valid:
                print(f"Error: {message}")
                continue
            
            if self.is_employee_exists(emp_id):
                print("Error: Employee ID already exists!")
                continue
            break
        
        while True:
            name = input("Enter Employee Name: ").strip()
            is_valid, message = self.validate_name(name)
            if not is_valid:
                print(f"Error: {message}")
                continue
            break
        
        print("Available Departments:", ", ".join(self.DEPARTMENTS))
        while True:
            dept = input("Enter Department: ").strip()
            if not self.is_department_exists(dept):
                print("Error: Department does not exist!")
                continue
            break
        
        while True:
            salary = input("Enter Salary: ").strip()
            is_valid, message = self.validate_salary(salary)
            if not is_valid:
                print(f"Error: {message}")
                continue
            salary = int(salary)
            break
        
        while True:
            email = input("Enter Email: ").strip()
            is_valid, message = self.validate_email(email)
            if not is_valid:
                print(f"Error: {message}")
                continue
            break
        
        # Prepare statement for insertion
        employee_data = {
            "emp_id": emp_id,
            "name": name,
            "dept": dept,
            "salary": salary,
            "email": email,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }
        
        try:
            result = self.employees.insert_one(employee_data)
            if result.inserted_id:
                print(f"Employee {emp_id} added successfully!")
            else:
                print("Failed to add employee!")
        except Exception as e:
            print(f"Error adding employee: {e}")
    
    def update_employee(self):
        """Update employee details"""
        print("\n--- Update Employee ---")
        
        emp_id = input("Enter Employee ID to update: ").strip()
        if not self.is_employee_exists(emp_id):
            print("Error: Employee not found!")
            return
        
        employee = self.employees.find_one({"emp_id": emp_id})
        print(f"\nCurrent details: {employee}")
        
        updates = {}
        
        # Name update with validation
        name = input(f"Enter new Name (current: {employee['name']}, press Enter to skip): ").strip()
        if name:
            is_valid, message = self.validate_name(name)
            if is_valid:
                updates["name"] = name
            else:
                print(f"Error: {message}")
        
        # Department update
        print("Available Departments:", ", ".join(self.DEPARTMENTS))
        dept = input(f"Enter new Department (current: {employee['dept']}, press Enter to skip): ").strip()
        if dept:
            if self.is_department_exists(dept):
                updates["dept"] = dept
            else:
                print("Error: Department does not exist!")
        
        # Salary update with validation
        salary = input(f"Enter new Salary (current: {employee['salary']}, press Enter to skip): ").strip()
        if salary:
            is_valid, message = self.validate_salary(salary)
            if is_valid:
                updates["salary"] = int(salary)
            else:
                print(f"Error: {message}")
        
        # Email update with validation
        email = input(f"Enter new Email (current: {employee['email']}, press Enter to skip): ").strip()
        if email:
            is_valid, message = self.validate_email(email)
            if is_valid:
                updates["email"] = email
            else:
                print(f"Error: {message}")
        
        if updates:
            updates["updated_at"] = datetime.now()
            try:
                result = self.employees.update_one(
                    {"emp_id": emp_id}, 
                    {"$set": updates}
                )
                if result.modified_count > 0:
                    print(f"Employee {emp_id} updated successfully!")
                else:
                    print("No changes made!")
            except Exception as e:
                print(f"Error updating employee: {e}")
        else:
            print("No updates provided!")
    
    def delete_employee(self):
        """Delete employee"""
        print("\n--- Delete Employee ---")
        
        emp_id = input("Enter Employee ID to delete: ").strip()
        if not self.is_employee_exists(emp_id):
            print("Error: Employee not found!")
            return
        
        confirm = input(f"Are you sure you want to delete employee {emp_id}? (yes/no): ").strip().lower()
        if confirm == 'yes':
            try:
                result = self.employees.delete_one({"emp_id": emp_id})
                if result.deleted_count > 0:
                    print(f"Employee {emp_id} deleted successfully!")
                else:
                    print("Failed to delete employee!")
            except Exception as e:
                print(f"Error deleting employee: {e}")
        else:
            print("Deletion cancelled!")
    
    def list_employees(self):
        """List all employees"""
        print("\n--- Employee List ---")
        
        try:
            employees = list(self.employees.find({}, {"_id": 0, "emp_id": 1, "name": 1, "dept": 1, "salary": 1, "email": 1}))
            
            if not employees:
                print("No employees found!")
                return
            
            print(f"{'ID':<8} {'Name':<20} {'Department':<12} {'Salary':<10} {'Email':<25}")
            print("-" * 80)
            for emp in employees:
                print(f"{emp['emp_id']:<8} {emp['name']:<20} {emp['dept']:<12} {emp['salary']:<10} {emp['email']:<25}")
        
        except Exception as e:
            print(f"Error fetching employees: {e}")
    
    def get_employees_by_department(self):
        """Get employees by department (One-to-Many relationship demonstration)"""
        print("\n--- Employees by Department ---")
        
        dept = input("Enter Department name: ").strip()
        if not self.is_department_exists(dept):
            print("Error: Department does not exist!")
            return
        
        try:
            employees = list(self.employees.find(
                {"dept": dept}, 
                {"_id": 0, "emp_id": 1, "name": 1, "salary": 1, "email": 1}
            ))
            
            if not employees:
                print(f"No employees found in {dept} department!")
                return
            
            print(f"\nEmployees in {dept} department:")
            print(f"{'ID':<8} {'Name':<20} {'Salary':<10} {'Email':<25}")
            print("-" * 65)
            for emp in employees:
                print(f"{emp['emp_id']:<8} {emp['name']:<20} {emp['salary']:<10} {emp['email']:<25}")
            
            print(f"\nTotal employees in {dept}: {len(employees)}")
        
        except Exception as e:
            print(f"Error fetching employees by department: {e}")