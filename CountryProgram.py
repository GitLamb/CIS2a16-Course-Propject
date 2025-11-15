## A program that manages a list of countries with their codes.

def display_menu():
    print("The Country List Program\n")
    print("COMMAND MENU")
    print("view - View a country")
    print("add  - Add a country")
    print("del  - Delete a country")
    print("exit - Exit program\n")

def initialize_countries():
    return {
        "US": "United States",
        "CA": "Canada",
        "GB": "United Kingdom"
    }

def view_country(countries):
    print("IN\n")
    for code in countries:
        print(code)
    print()
    code = input("Enter country code: ").upper()
    if code in countries:
        print(f"Country name: {countries[code]}\n")
    else:
        print("Country code not found.\n")

def add_country(countries):
    code = input("Enter country code: ").upper()
    if code in countries:
        print("Country code already exists.\n")
    else:
        name = input("Enter country name: ")
        countries[code] = name
        print(f"{name} was added.\n")

def delete_country(countries):
    code = input("Enter country code: ").upper()
    if code in countries:
        name = countries.pop(code)
        print(f"{name} was deleted.\n")
    else:
        print("Country code not found.\n")

def main():
    countries = initialize_countries()
    display_menu()

    while True:
        command = input("Command: ").strip().lower()
        print()
        if command == "view":
            view_country(countries)
        elif command == "add":
            add_country(countries)
        elif command == "del":
            delete_country(countries)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.\n")

if __name__ == "__main__":
    main()
