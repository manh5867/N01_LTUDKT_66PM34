class Employee:
    def __init__(self, employee_id, employee_name, phone_number, email, position):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.phone_number = phone_number
        self.email = email
        self.position = position

    def display_information(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Employee Name: {self.employee_name}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Email: {self.email}")
        print(f"Position: {self.position}")


class Manager(Employee):
    def __init__(self, employee_id, employee_name, phone_number, email, managing_team, number_of_employees, total_revenue):
        super().__init__(employee_id, employee_name, phone_number, email, "Manager")
        self.managing_team = managing_team
        self.number_of_employees = number_of_employees
        self.total_revenue = total_revenue

    def display_information(self):
        super().display_information()
        print(f"Managing Team: {self.managing_team}")
        print(f"Number of Employees in Team: {self.number_of_employees}")
        print(f"Total Team Revenue: {self.total_revenue}")


class Salesperson(Employee):
    def __init__(self, employee_id, employee_name, phone_number, email, revenue, months_worked):
        super().__init__(employee_id, employee_name, phone_number, email, "Salesperson")
        self.revenue = revenue
        self.months_worked = months_worked

    def display_information(self):
        super().display_information()
        print(f"Revenue: {self.revenue}")
        print(f"Months Worked: {self.months_worked}")