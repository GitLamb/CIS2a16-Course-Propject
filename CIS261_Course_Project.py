#Jason Lambert
#CIS261
#Course Project Phase 2

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

def calculate_pay(hours, rate, tax_rate):
    gross = hours * rate
    tax = gross * tax_rate
    net = gross - tax
    return gross, tax, net

def process_employees(records):
    totals = {"employees": 0, "hours": 0, "tax": 0, "net": 0}
    print("\n--- Employee Pay Summary ---")
    for record in records:
        from_date, to_date, name, hours, rate, tax_rate = record
        gross, tax, net = calculate_pay(hours, rate, tax_rate)
        print(f"\nFrom: {from_date}  To: {to_date}")
        print(f"Employee: {name}")
        print(f"Hours Worked: {hours}")
        print(f"Hourly Rate: ${rate:.2f}")
        print(f"Gross Pay: ${gross:.2f}")
        print(f"Tax Rate: {tax_rate:.2%}")
        print(f"Income Tax: ${tax:.2f}")
        print(f"Net Pay: ${net:.2f}")
        totals["employees"] += 1
        totals["hours"] += hours
        totals["tax"] += tax
        totals["net"] += net
    return totals

def display_totals(totals):
    print("\n--- Totals ---")
    print(f"Total Employees: {totals['employees']}")
    print(f"Total Hours: {totals['hours']}")
    print(f"Total Income Tax: ${totals['tax']:.2f}")
    print(f"Total Net Pay: ${totals['net']:.2f}")

def main():
    employee_records = []
    while True:
        from_date, to_date = get_work_dates()
        name, hours, rate, tax_rate = get_employee_data()
        employee_records.append([from_date, to_date, name, hours, rate, tax_rate])
        cont = input("Type 'End' to finish or press Enter to continue: ").strip().lower()
        if cont == "end":
            break
    totals = process_employees(employee_records)
    display_totals(totals)

if __name__ == "__main__":
    main()
