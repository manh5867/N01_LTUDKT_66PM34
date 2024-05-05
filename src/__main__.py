from ManageEmployee import ManageEmployee

def main():
    manager = ManageEmployee()
    while True:
        print("Select an option:")
        print("1. Add New Employee")
        print("2. Edit employee information")
        print("3. Delete employee ")
        print("4. Sreach employee by id or name")
        
        print("\n5. Show Employees")
        print("6. Calculate employee salary ")
        print("7. Calculate total and average store revenue")
        print("8. Total salary payable to employees")
        print("9. Show the list of employees with the highest revenue in the month")
        print("10. Statistics on the list of employees with lower or higher salaries than average")
        print("11. Displays the group with the highest total revenue")

        print("\n12. Display manager salary")
        print("13. Display saleperson salary")
        
        print("\n14. Quit")
        print("\n--------------------------------")
        choice = input("Enter your choice (1 to 14 ): ")

        if choice == "1":
            manager.add_employee()
        elif choice == "2":
            id = input("Enter employee id: ")
            manager.sua_nhan_vien(id)
        elif choice == "3":
            id = input("Enter employee id: ")
            manager.xoa_nhan_vien(id)
        elif choice == "4":
            manager.search_employee()
        elif choice == "5":
            manager.show_employee_by_job_position()
        elif choice == "6":
            id = input("Enter employee id: ")
            employee = manager.tim_nhan_vien(id)
            if employee:
                salary = employee.calculate_salary()
                print(f"Lương của nhân viên có ID {id}: {salary}")
            else:
                print(f"Không tìm thấy nhân viên có ID {id}.")
        elif choice == "7":
            manager.calculate_shoprevenue()
        elif choice == "8":
            manager.calculate_total_salary()
        elif choice == "9":
            n= input("Nhập số n nhân viên cần thống kê: ")
            n = int(n)
            manager.hien_thi_nhan_vien_doanh_thu_cao_nhat(n)
        elif choice == "10":
            option = input("Enter 'lower' or 'higher' to display employees with salaries lower or higher than the average: ")
            if option in ['lower', 'higher']:
                manager.display_employees_by_salary(option)
            else:
                print("Invalid option. Please enter 'lower' or 'higher'.")
        elif choice == "11":
            manager.display_highest_revenue_management_team()
        elif choice == "12":
            manager.display_manager_salaries()
        elif choice == "13":
            manager.display_salesperson_salaries()
        elif choice == "14":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
