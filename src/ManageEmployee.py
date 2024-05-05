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


    #YC2.2 Sửa thông tin nhân viên
    def sua_nhan_vien(self, employee_id):
       
        employee_name = input("Enter Employee Name: ")
        phone_number = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        position = input("Enter position (Manager or Sales person): ")
        for employee in self.employees:

            if employee.employee_id == employee_id:
                if employee_name:
                    employee.employee_name = employee_name
                if phone_number:
                    employee.phone_number = phone_number
                if email:
                    employee.email = email
                if position:
                    employee.position = position
                if position == 'Manager':
                
                    employee.managing_team = input("Enter Managing Team: ")
                
                    employee.number_of_employees = input("Enter Number of Employees: ")
               
                    employee.total_revenue = input("Enter Total Revenue: ")
                elif position == 'Salesperson':
                
                    employee.revenue = input("Enter Revenue: ")
                
                    employee.months_worked = input("Enter Months Worked: ")
        else:
            print("No employees found with this ID.")
    
    #YC2.3 Xóa nhân viên
    def xoa_nhan_vien(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                self.employees.remove(employee)
                print("Detele success!")
                return
        print("No employees found with this ID.")
    
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


    # YC2.9. Hiển thị danh sách n nhân viên có doanh thu cao nhất
    def hien_thi_nhan_vien_doanh_thu_cao_nhat(self, n):
        salespeople = [employee for employee in self.employees if isinstance(employee, Salesperson)]
        sorted_salespeople = sorted(salespeople, key=lambda x: x.revenue, reverse=True)
        print(f"Danh sách {n} nhân viên Salesperson có doanh thu cao nhất:")
        for i in range(min(n, len(sorted_salespeople))):
            print(f"Employee ID: {sorted_salespeople[i].employee_id}")
            print(f"Employee Name: {sorted_salespeople[i].employee_name}")
            print(f"Phone Number: {sorted_salespeople[i].phone_number}")
            print(f"Email: {sorted_salespeople[i].email}")
            print(f"Position: {sorted_salespeople[i].position}")
            print(f"Revenue: {sorted_salespeople[i].revenue}")
            print()  # In ra một dòng trống để phân tách giữa các nhân viên

    def tim_nhan_vien(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee
        return None

        