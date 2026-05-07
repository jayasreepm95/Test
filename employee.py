class Employee:
    def __init__(self, emp_id, name, email, department, salary, status="ACTIVE"):
        self.id = emp_id
        self.name = name
        self.email = email
        self.department = department
        self.salary = salary
        self.status = status

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Email: {self.email}, Dept: {self.department}, Salary: {self.salary}, Status: {self.status}"


class EmployeeManagementSystem:
    def __init__(self):
        self.employees = {}


    def add_employee(self, emp):

        for e in self.employees.values():
            if e.email == emp.email:
                print(" Email already exists!")
                return

        self.employees[emp.id] = emp
        print(" Employee added successfully")


    def get_employee_by_id(self, emp_id):
        emp = self.employees.get(emp_id)
        if emp:
            print(emp)
        else:
            print("Employee not found")


    def get_active_employees(self):
        active = [e for e in self.employees.values() if e.status == "ACTIVE"]

        if not active:
            print("No active employees found")
        else:
            for emp in active:
                print(emp)


    def update_employee(self, emp_id, name=None, email=None, department=None, salary=None):
        emp = self.employees.get(emp_id)

        if not emp:
            print(" Employee not found")
            return


        if email:
            for e in self.employees.values():
                if e.email == email and e.id != emp_id:
                    print(" Email already exists!")
                    return
            emp.email = email

        if name:
            emp.name = name
        if department:
            emp.department = department
        if salary:
            emp.salary = salary

        print(" Employee updated successfully")


    def delete_employee(self, emp_id):
        emp = self.employees.get(emp_id)

        if not emp:
            print(" Employee not found")
            return

        emp.status = "INACTIVE"
        print("Employee marked as INACTIVE")



if __name__ == "__main__":
    system = EmployeeManagementSystem()

    e1 = Employee(1, "Johny", "johny@example.com", "IT", 50000)
    e2 = Employee(2, "Anie", "anie@example.com", "HR", 45000)

    system.add_employee(e1)
    system.add_employee(e2)

    print("\n Fetch by ID:")
    system.get_employee_by_id(1)

    print("\n Active Employees:")
    system.get_active_employees()

    print("\nUpdate Employee:")
    system.update_employee(1, salary=55000)

    print("\n Delete Employee:")
    system.delete_employee(1)

    print("\n Active Employees After Deletion:")
    system.get_active_employees()