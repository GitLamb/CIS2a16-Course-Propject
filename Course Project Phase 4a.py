#Jason Lambert
#CSI261
#Course Project Phase 4

#File:Secure_card_app.apy
 
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

def enter_data(filename, existing_user_ids):
    """Allow admin to enter new user records."""
    while True:
        user_id = input("Enter new User ID (or type 'End' to stop): ").strip()
        if user_id.lower() == 'end':
            break
        if user_id in existing_user_ids:
            print("This User ID already exists.")
            continue

        password = input("Enter Password: ").strip()
        auth = input("Enter Authorization Code (Admin/User): ").strip().capitalize()
        if auth not in ['Admin', 'User']:
            print("Invalid authorization code.")
            continue

        with open(filename, 'a') as file:
            file.write(f"{user_id}|{password}|{auth}\n")
        existing_user_ids.append(user_id)
        print("User added successfully.\n")

def main():
    filename = 'user_data.txt'
    user = login_process(filename)

    if user:
        print(f"Logged in as: {user.user_id}")
        print(f"Authorization: {user.authorization}")
        print(f"Password: {user.password}\n")

        if user.authorization == 'Admin':
            print("Access Level: Admin — You can enter and view data.")
            existing_ids = [u['user_id'] for u in load_user_credentials(filename)]
            enter_data(filename, existing_ids)
            display_data(filename)
        elif user.authorization == 'User':
            print("Access Level: User — You can view data only.")
            display_data(filename)
        else:
            print("Unknown authorization level. Access denied.")

if __name__ == "__main__":
    main()