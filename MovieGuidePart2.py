#Jason Lambert
#CIS261
#MovieGuidePart2

def display_menu():
    print("The Movie List program\n")
    print("COMMAND MENU")
    print("list - List all movies")
    print("add  - Add a movie")
    print("del  - Delete a movie")
    print("exit - Exit program\n")

def load_movies(filename):
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_movies(filename, movies):
    with open(filename, "w") as file:
        for movie in movies:
            file.write(movie + "\n")

def list_movies(movies):
    if not movies:
        print("No movies in the list.\n")
    else:
        for i, movie in enumerate(movies, start=1):
            print(f"{i}. {movie}")
        print()

def add_movie(movies):
    title = input("Movie: ")
    movies.append(title)
    print(f"{title} was added.\n")

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
    filename = "movies.txt"

    # Part 1: Create and populate the file initially (only if empty)
    if not load_movies(filename):
        initial_movies = [
            "Cat on a Hot Tin Roof",
            "On the Waterfront",
            "Monty Python and the Holy Grail"
        ]
        save_movies(filename, initial_movies)

    movies = load_movies(filename)
    display_menu()

    while True:
        command = input("Command: ").strip().lower()
        print()
        if command == "list":
            list_movies(movies)
        elif command == "add":
            add_movie(movies)
            save_movies(filename, movies)
            list_movies(movies)
        elif command == "del":
            delete_movie(movies)
            save_movies(filename, movies)
            list_movies(movies)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.\n")

if __name__ == "__main__":
    main()