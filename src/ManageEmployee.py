from Employee import Manager, Salesperson

class ManageEmployee:
    def __init__(self):
        self.employees = []

    # Add an employee
    def add_employee(self):
        print("Select employee type:")
        print("1. Add New Manager")
        print("2. Add New Sales Person")
        employee_type = input("Enter your choice (1 or 2): ")

        if employee_type == "1":
            employee_id = input("Enter Employee ID: ")
            employee_name = input("Enter Employee Name: ")
            phone_number = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            managing_team = input("Enter Managing Team: ")
            number_of_employees = input("Enter Number of Employees: ")
            total_revenue = input("Enter Total Revenue: ")
            new_employee = Manager(employee_id, employee_name, phone_number, email, managing_team, number_of_employees,
                                   total_revenue)
            self.employees.append(new_employee)
            print("You added a new manager !")

        elif employee_type == "2":
            employee_id = input("Enter Employee ID: ")
            employee_name = input("Enter Employee Name: ")
            phone_number = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            revenue = input("Enter Revenue: ")
            months_worked = input("Enter Months Worked: ")
            new_employee = Salesperson(employee_id, employee_name, phone_number, email, revenue, months_worked)
            self.employees.append(new_employee)
            print("You added a new sale person !")
        else:
            print("Invalid choice !!!")
    
    

        