#Jason Lambert
#CSI261
#Course Project Phase 4

#Sedcured card app
import re

class Login:
   def __init__(self, user_id, password, authorization):
       self.user_id = user_id
       self.password = password
       self.authorization = authorization

def load_user_credentials(filename):
    """Load user credentials from file into a list of dictionaries."""
    users = []
    try:
        with open(filename, 'r') as file:
                 for line in file:
                    user_id, password, auth = line.strip().split('|')
                    users.append({'user_id': user_id, 'password': password, 'auth': auth})
    except FileNotFoundError:
        print("User data file not found.")
    return users

def add_users(filename, existing_user_ids):
    """Prompt for user input and add new users to the file."""
    while True:
        user_id = input("Enter User ID (or type 'End' to finish): ").strip()
        if user_id.lower() == 'end':
            break
        if user_id in existing_user_ids:
            print("This User ID already exists. Please try a different one.")
            continue

        password = input("Enter Password: ").strip()
        auth_code = input("Enter Authorization Code (Admin/User): ").strip().capitalize()

        if auth_code not in ['Admin', 'User']:
            print("Invalid authorization code. Please enter 'Admin' or 'User'.")
            continue

        with open(filename, 'a') as file:
            file.write(f"{user_id}|{password}|{auth_code}\n")
        existing_user_ids.append(user_id)
        print(f"User '{user_id}' added successfully.\n")

def login_process(filename):
    """Authenticate user and return a Login object if successful."""
    users = load_user_credentials(filename)
    user_ids = [user['user_id'] for user in users]

    user_id = input("Enter your User ID: ").strip()
    if user_id not in user_ids:
        print("User ID not found. Access denied.")
        return None

    password = input("Enter your Password: ").strip()
    user_record = next((u for u in users if u['user_id'] == user_id), None)

    if user_record and user_record['password'] == password:
        print("Login successful.\n")
        return Login(user_id, password, user_record['auth'])
    else:
        print("Incorrect password. Access denied.")
        return None

def display_data(filename):
    """Display all user records from the file."""
    print("\nUser Records:")
    print("-" * 40)
    try:
        with open(filename, 'r') as file:
            for line in file:
                user_id, password, auth = line.strip().split('|')
                print(f"User ID: {user_id}, Password: {password}, Authorization: {auth}")
    except FileNotFoundError:
        print("No user data found.")

#Payroll Functions
def run_payroll_module():
    filename = "employee_data.txt"
    while True:
        from_date, to_date = get_work_dates()
        name, hours, rate, tax_rate = get_employee_data()
        record = [from_date, to_date, name, hours, rate, tax_rate]
        write_record_to_file(filename, record)

        cont = input("Type 'End' to finish or press Enter to continue: ").strip().lower()
        if cont == "end":
            break

    generate_report(filename)

def get_work_dates():
    from_date = input("Enter FROM date (mm/dd/yyyy): ")
    to_date = input("Enter TO date (mm/dd/yyyy): ")
    return from_date, to_date

def get_employee_data():
    name = input("Enter employee name: ")
    hours = float(input("Enter total hours worked: "))
    rate = float(input("Enter hourly rate: "))
    tax_rate = float(input("Enter income tax rate (as decimal, e.g., 0.2 for 20%): "))
    return name, hours, rate, tax_rate

def write_record_to_file(filename, record):
    with open(filename, "a") as file:
        file.write("|".join(str(field) for field in record) + "\n")

def calculate_pay(hours, rate, tax_rate):
    gross = hours * rate
    tax = gross * tax_rate
    net = gross - tax
    return gross, tax, net

def is_valid_date(date_str):
    return bool(re.match(r"^\d{2}/\d{2}/\d{4}$", date_str))

def generate_report(filename):
    report_date = input("Enter FROM date for report (mm/dd/yyyy or 'All'): ").strip()
    print()

    if report_date.lower() != "all" and not is_valid_date(report_date):
        print("Invalid date format. Please use mm/dd/yyyy.\n")
        return

    totals = {"employees": 0, "hours": 0, "tax": 0, "net": 0}

    try:
        with open(filename, "r") as file:
            for line in file:
                fields = line.strip().split("|")
                if len(fields) != 6:
                    continue

                from_date, to_date, name, hours, rate, tax_rate = fields
                hours, rate, tax_rate = float(hours), float(rate), float(tax_rate)

                if report_date.lower() == "all" or from_date == report_date:
                    gross, tax, net = calculate_pay(hours, rate, tax_rate)
                    print(f"From: {from_date}  To: {to_date}")
                    print(f"Employee: {name}")
                    print(f"Hours Worked: {hours}")
                    print(f"Hourly Rate: ${rate:.2f}")
                    print(f"Gross Pay: ${gross:.2f}")
                    print(f"Tax Rate: {tax_rate:.2%}")
                    print(f"Income Tax: ${tax:.2f}")
                    print(f"Net Pay: ${net:.2f}\n")

                    totals["employees"] += 1
                    totals["hours"] += hours
                    totals["tax"] += tax
                    totals["net"] += net
    except FileNotFoundError:
        print("No data file found.\n")
        return

    print("--- Totals ---")
    print(f"Total Employees: {totals['employees']}")
    print(f"Total Hours: {totals['hours']}")
    print(f"Total Income Tax: ${totals['tax']:.2f}")
    print(f"Total Net Pay: ${totals['net']:.2f}\n")

def main():
    user_file = "user_data.txt"
    user = login_process(user_file)

    if user:
        if user.authorization == 'Admin':
            while True:
                print("\n--- Admin Menu ---")
                print("1. Manage Users")
                print("2. Run Payroll Module")
                print("3. Logout")
                choice = input("Choose an option: ").strip()

                if choice == '1':
                    existing_ids = [u['user_id'] for u in load_user_credentials(user_file)]
                    add_users(user_file, existing_ids)
                    display_data(user_file)
                elif choice == '2':
                    run_payroll_module()
                elif choice == '3':
                    print("Logging out...\n")
                    break
                else:
                    print("Invalid choice. Try again.")
        elif user.authorization == 'User':
            print("\nAccess Level: User - You can view user records only.")
            display_data(user_file)
        else:
            print("Unknown authorization level. Access denied.")
if __name__ == "__main__":
    main()
