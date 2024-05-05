from ManageEmployee import ManageEmployee

def main():
    manager = ManageEmployee()
    while True:
        print("Select an option:")
        print("1. Add New Employee")
        print("2. Edit employee information")
        print("3. Delete employee ")
       
        print("5. Show Employees")
        print("6. calculate employee salary ")

        print("9. Show the list of employees with the highest revenue in the month")
        print("99. Quit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            manager.add_employee()
        elif choice == "2":
            id = input("Enter employee id: ")
            manager.sua_nhan_vien(id)
        elif choice == "3":
            id = input("Enter employee id: ")
            manager.xoa_nhan_vien(id)
        elif choice == "9":
            n= input("Nhập số n nhân viên cần thống kê: ")
            n = int(n)
            manager.hien_thi_nhan_vien_doanh_thu_cao_nhat(n)
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
        elif choice == "99":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()