from Employee import Manager, Salesperson

class ManageEmployee:
    def __init__(self):
        self.employees = []

    #YC2.1 Add an employee
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
    
    
    # YC2.5. Show Employee by job position
    def show_employee_by_job_position(self):
        job_positions = {
            "1": "Manager",
            "2": "Salesperson"
        }

        print("Select a job position:")
        for key, value in job_positions.items():
            print(f"{key}. {value}")

        choice = input("Enter your choice: ")

        if choice in job_positions:
            matching_employees = [employee for employee in self.employees if employee.position == job_positions[choice]]

            if len(matching_employees) == 0:
                print(f"No employees found with the job position '{job_positions[choice]}'.")
            else:
                print(f"Employees with the job position '{job_positions[choice]}':")
                for employee in matching_employees:
                    print("--------------------")
                    employee.display_information()
                    print("--------------------")
        else:
            print("Invalid choice. Please try again.")
         
        