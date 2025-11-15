## Movie List Program

def display_menu():
    print("The Movie List program\n")
    print("COMMAND MENU")
    print("list - List all movies")
    print("add  - Add a movie")
    print("del  - Delete a movie")
    print("exit - Exit program\n")

def list_movies(movies):
    if not movies:
        print("No movies in the list.\n")
    else:
        for i, movie in enumerate(movies, start=1):
            print(f"{i}. {movie}")
        print()

def add_movie(movies):
    name = input("Name: ")
    movies.append(name)
    print(f"{name} was added.\n")

def delete_movie(movies):
    try:
        number = int(input("Number: "))
        if 1 <= number <= len(movies):
            removed = movies.pop(number - 1)
            print(f"{removed} was deleted.\n")
        else:
            print("Invalid movie number.\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")

def main():
    movies = [
        "Monty Python and the Holy Grail",
        "On the Waterfront",
        "Cat on a Hot Tin Roof"
    ]

    display_menu()

    while True:
        command = input("Command: ").strip().lower()
        print()
        if command == "list":
            list_movies(movies)
        elif command == "add":
            add_movie(movies)
        elif command == "del":
            delete_movie(movies)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.\n")

if __name__ == "__main__":
    main()
