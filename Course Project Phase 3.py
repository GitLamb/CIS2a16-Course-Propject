#Jason Lambert
#CIS261
#Course Project Phase 3

import re

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
                    continue  # skip malformed lines

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

if __name__ == "__main__":
    main()