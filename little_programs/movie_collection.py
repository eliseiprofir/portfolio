def main():
    print("–––––––––––––––––––––––––")
    print("Welcome to my little program for managing a movie collection.\n")
    global all_movies
    all_movies = []
    print("This is your current collection.\n")
    for movie in all_movies:
        print(print_movie(movie))
    while True:
        operation = input("\nChoose your operation 'add', 'delete', 'view', 'find'. When you want to stop the program, type 'stop'. ").lower()
        if operation == 'add':
            add_movie()
        elif operation == 'view':
            view_movies()
        elif operation == 'delete':
            delete_movie()
        elif operation == 'find':
            find_movies()
        elif operation == 'stop':
            print("\nThis is your collection now.\n")
            for movie in all_movies:
                print(print_movie(movie))
            print("\nThank you for using my program! 😊")
            print("–––––––––––––––––––––––––")
            break
        else:
            print("Operation not found. Try again. ")
            print("–––––––––––––––––––––––––")


def add_movie():
    print("\nEnter the movie's informations.", end=" ")
    while True:
        movie_add = input("\nHit enter to add movie or type 'stop' when you're done. ").lower()
        if movie_add != 'stop':
            name = input("Name: ").title()
            year = input("Year: ")
            genre = input("Genre: ").title()
            all_movies.append({
                "Name":  name,
                "Year":  year,
                "Genre": genre
            })
        else:
            print("–––––––––––––––––––––––––")
            break


def delete_movie():
    while True:
        print("")
        for movie in all_movies:
            print(f"Movie: {movie['Name']}, Year: {movie['Year']}, Genre: {movie['Genre']}")
        print("")
        movie_del = input("Enter the movie title you want to delete, or 'stop' when you're done: ")
        if movie_del != 'stop':
            for movie in all_movies:
                if movie_del.title() == movie['Name']:
                    all_movies.remove(movie)
                    break
        else:
            print("–––––––––––––––––––––––––")
            break


def print_movie(movie):
    return f"Name: {movie['Name']}, Year: {movie['Year']}, Genre: {movie['Genre']}"


def view_movies():
    print("")
    for movie in all_movies:
        print(print_movie(movie))
    print("–––––––––––––––––––––––––")


def find_movies():
    found = []
    while True:
        criteria = input("\nWhat criteria do you want to use in search. Name, year or genre? (type 'stop' when you're done) ").title()
        if criteria == 'Stop':
            break
        elif criteria not in ["Name", "Year", "Genre"]:
            print("Criteria not found")
        else:
            search_by = input(f"Enter the {criteria}: ").title()
            for movie in all_movies:
                if search_by == movie[criteria]:
                    found.append(movie)
    print("")
    print("All movies matching your criteria(s) are:")
    for movie in found:
        print(print_movie(movie))
    print("–––––––––––––––––––––––––")


if __name__ == "__main__":
    main()