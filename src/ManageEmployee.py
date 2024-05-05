from Employee import Manager, Salesperson
from datetime import datetime

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
        print("\n--------------------------------")

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
        print("\n--------------------------------")
    #YC2.3 Xóa nhân viên
    def xoa_nhan_vien(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                self.employees.remove(employee)
                print("Detele success!")
                return
        print("No employees found with this ID.")
        print("\n--------------------------------")
    # YC2.4. Search employee by id, name
    def search_employee(self): 
        search_key = input("Enter employee name or ID: ").lower()
        found_employees = []
        for employee in self.employees:
            if search_key in employee.employee_id.lower() or search_key in employee.employee_name.lower():
                found_employees.append(employee)
        if found_employees:
            print("Found Employees:")
            for employee in found_employees:
                print("--------------------")
                employee.display_information()
                print("--------------------")
        else:
            print("No employee found with the provided name or ID.")
        print("\n--------------------------------")
    
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
            
    #YC2.7. Tổng doanh thu, các loại doanh thu trung bình của shop trong tháng hiện tại
    def calculate_shoprevenue(self):
        current_month = datetime.now().month
        total_revenue = 0
        total_count = 0
        for employee in self.employees:
            if datetime.now().month == current_month:
                if isinstance(employee, Salesperson):
                    total_revenue += float(employee.revenue)
                    total_count += 1
                elif isinstance(employee, Manager):
                    total_revenue += float(employee.total_revenue)
                    total_count += 1

        if total_revenue == 0:  
            print("No sales revenue data available for the current month.")
        else:
            average_revenue = total_revenue / total_count if total_count != 0 else 0 
            print(f"Total revenue for the current month: {total_revenue}")
            print(f"Average revenue for the current month: {average_revenue}")
        print("\n--------------------------------")
        
    #YC2.8. Tính tổng lương cửa hàng phải trả cho nhân viên trong tháng hiện tại
    def calculate_total_salary(self):
        current_month = datetime.now().month
        total_salary = 0
        for employee in self.employees:
            if datetime.now().month == current_month:
                total_salary += employee.calculate_salary()
        print(f"Total salary to be paid in current month: {total_salary}")
        print("\n--------------------------------")

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

    #YC2.10. Thống kê danh sách nhân viên có lương thấp hoặc cao hơn trung bình
    def display_employees_by_salary(self, option):
        if not self.employees:
            print("No employees available.")
            return
        total_salary = sum(employee.calculate_salary() for employee in self.employees)
        average_salary = total_salary / len(self.employees)

        if option == "lower":
            print(f"Employees with salaries lower than the average salary ({average_salary}):")
            for employee in self.employees:
                if employee.calculate_salary() < average_salary:
                    print(f"Employee ID: {employee.employee_id}")
                    print(f"Employee Name: {employee.employee_name}")
                    print(f"Position: {employee.position}")
                    print(f"Average Salary: {average_salary}")
                    print("--------------------")
        elif option == "higher":
            print(f"Employees with salaries higher than the average salary ({average_salary}):")
            for employee in self.employees:
                if employee.calculate_salary() > average_salary:
                    print(f"Employee ID: {employee.employee_id}")
                    print(f"Employee Name: {employee.employee_name}")
                    print(f"Position: {employee.position}")
                    print(f"Average Salary: {average_salary}")
                    print("--------------------")
        else:
            print("Invalid option. Please choose 'lower' or 'higher'.")
            print("\n--------------------------------")
            
    #YC2.11. Hiển thị nhóm có tổng doanh thu cao nhất
    def display_highest_revenue_management_team(self):
        manager_teams = {}  
        for employee in self.employees:
            if isinstance(employee, Manager):
                if employee.managing_team not in manager_teams:
                    manager_teams[employee.managing_team] = 0
                manager_teams[employee.managing_team] += int(employee.total_revenue)

        if not manager_teams:
            print("No manager data available.")
            return

        highest_revenue_team = max(manager_teams, key=manager_teams.get)
        highest_revenue = manager_teams[highest_revenue_team]

        print(f"Highest revenue management team: {highest_revenue_team}")
        print(f"Total revenue: {highest_revenue}")
        print("\n--------------------------------")
        
    #2 chức năng được thêm vào dựa vào dữ liệu có sẵn
    def display_manager_salaries(self):
        print("Manager Salaries:")
        for employee in self.employees:
            if isinstance(employee, Manager):
                print(f"Manager Name: {employee.employee_name}")
                print(f"Manager ID: {employee.employee_id}")
                print(f"Total Team Revenue: {employee.total_revenue}")
                print(f"Salary: {employee.calculate_salary()}")
                print("--------------------")
                
    def display_salesperson_salaries(self):
        print("Salesperson Salaries:")
        for employee in self.employees:
            if isinstance(employee, Salesperson):
                print(f"Salesperson Name: {employee.employee_name}")
                print(f"Salesperson ID: {employee.employee_id}")
                print(f"Position: {employee.position}")
                print(f"Salary: {employee.calculate_salary()}")
                print("--------------------")


        
