#Jason Lambert
#CSI261
#Course Project Phase 4

 File: user_auth_system.py

def load_existing_users(filename):
    """Load existing user IDs from the file into a list."""
    user_ids = []
    try:
        with open(filename, 'a+') as file:
            file.seek(0)
            for line in file:
                parts = line.strip().split('|')
                if len(parts) >= 1:
                    user_ids.append(parts[0])
    except FileNotFoundError:
        print("User file not found. A new one will be created.")
    return user_ids

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

def display_all_users(filename):
    """Display all users from the file."""
    print("\nRegistered Users:")
    print("-" * 40)
    try:
        with open(filename, 'r') as file:
            for line in file:
                user_id, password, auth_code = line.strip().split('|')
                print(f"User ID: {user_id}, Password: {password}, Authorization: {auth_code}")
    except FileNotFoundError:
        print("No user data found.")

def main():
    filename = 'user_data.txt'
    user_ids = load_existing_users(filename)
    add_users(filename, user_ids)
    display_all_users(filename)

if __name__ == "__main__":
    main()