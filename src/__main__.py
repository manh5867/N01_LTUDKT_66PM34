from ManageEmployee import ManageEmployee

def main():
    manager = ManageEmployee()
    while True:
        print("Select an option:")
        print("1. Add New Employee")
        print("5. Show Employees")
        print("99. Quit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            manager.add_employee()
        elif choice == "5":
            manager.show_employee_by_job_position()
        elif choice == "99":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()