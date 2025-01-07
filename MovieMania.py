import random


# Display Dictionary/List of Movies
def list_movies(movies_dict):
    """
    Displays the Movie and its Rating stored in the Movies Dictionary (movies_dict).

    Parameters:
        movies_dict["movie"] (string) : Name of the Movie
        movies_dict["rating"] (float) : Rating of the Movie

    Display:
        movie (string) : Name of the Movie
        rating (float) : Rating of the Movie
    """
    for movie, rating in movies_dict.items():
        print(f"{movie}, ({rating})")
    go_back_or_quit()


# Add a new Movie into the Dictionary/List of Movies
def add_movie(movies_dict):
    """
    Adds a new Movie and its Rating into the Movies Dictionary (movies_dict), after
    checking if it already exists or not.

    Parameters:
        movies_dict["movie"] (string) : Name of the Movie
        movies_dict["rating"] (float) : Rating of the Movie

    Display:
        Message: Movie already exists in the Movies Dictionary. OR
        Message: Movie has been added successfully in the Movies Dictionary.
    """
    movie_name = input("Enter Movie Name: ")
    if movie_name in movies_dict:                           # Check if the Movie already
        print()                                             # exists in the Dictionary/
        print(f"The Movie {movie_name} already exists")     # List of Movies
        go_back_or_quit()
    else:
        rating = float(input("Enter the Rating of the Movie: "))
        movies_dict[movie_name] = rating
        print()
        print("Movie added successfully")
        go_back_or_quit()


# Delete Movie from the Dictionary/List of Movies
def delete_movie(movies_dict):
    """
    Deletes a Movie and its Rating from the Movies Dictionary (movies_dict), after
    checking if it exists or not.

    Parameters:
        movies_dict["movie"] (string) : Name of the Movie

    Display:
        Message: Movie doesn't exist in the Movies Dictionary. OR
        Message: Movie has been deleted successfully from the Movies Dictionary.
    """
    movie_name = input("Enter the Movie Name you want to delete: ")
    if movie_name not in movies_dict:                                   # Check if the Movie
        print()                                                         # exists in the Dictionary/
        print(f"The Movie {movie_name} doesn't exist")                  # List of Movies
        go_back_or_quit()
    else:
        del movies_dict[movie_name]
        print()
        print("Movie deleted successfully")
        go_back_or_quit()


# Update the Rating of a Movie
def update_movie(movies_dict):
    """
    Updates the Rating of an existing Movie in the Movies Dictionary (movies_dict), after
    checking if it exists or not.

    Parameters:
        movies_dict["movie"] (string) : Name of the Movie
        movies_dict["rating"] (float) : Rating of the Movie

    Display:
        Message: Movie doesn't exist in the Movies Dictionary. OR
        Message: Movie has been updated successfully in the Movies Dictionary.
    """
    movie_name = input("Which Movie's Rating would you like to change? ")
    if movie_name not in movies_dict:                                         # Check if the Movie
        print()                                                               # exists in the Dictionary/
        print(f"The Movie {movie_name} doesn't exist")                        # List of Movies
        go_back_or_quit()
    else:
        rating = float(input("Enter the Rating of the Movie: "))
        movies_dict[movie_name] = rating
        print()
        print("Movie's Rating changed successfully")
        go_back_or_quit()


# Display Statistics of the Dictionary7List of Movies
def stats(movies_dict):
    """
    Shows the Stats of the Movies from the Movies Dictionary (movies_dict),
    based on the Movie's Rating

    Parameters:
        movies_dict["movie"] (string): Name of the Movie
        movies_dict["rating"] (float): Rating of the Movie

    Display:
        Message: Number of Movies in the Movies Dictionary.
        Message: Average Rating of all Movies.
        Message: Median Rating of all Movies
        Message: Best Movie/s.
        Message: Worst Movie/s.
    """
    # Declaration and Initialization of Variables
    best_movie_list = []
    worst_movie_list = []
    highest_rating = 0          # has to be initialized with 0, because can go only upwards.
    lowest_rating = 10          # has to be initialized with 10, because can go only downwards.
    movie_rating_list = movies_dict.values()

    for movie, rating in movies_dict.items():
        if rating == highest_rating:
            best_movie_list.append(movie)
        elif rating > highest_rating:
            highest_rating = rating
            best_movie_list.clear()
            best_movie_list.append(movie)
        elif rating < lowest_rating:
            lowest_rating = rating
            worst_movie_list.clear()
            worst_movie_list.append(movie)
        elif rating == lowest_rating:
            worst_movie_list.append(movie)

    average_rating = sum(movie_rating_list) / len(movies_dict)

    sorted_movie_rating_list = sorted(movie_rating_list)
    if len(sorted_movie_rating_list) % 2 == 0:
        middle_index = int(len(sorted_movie_rating_list) / 2)
        median_rating = (sorted_movie_rating_list[middle_index-1] + sorted_movie_rating_list[middle_index]) / 2
    else:
        middle_index = len(sorted_movie_rating_list) // 2
        median_rating = sorted_movie_rating_list[middle_index]

    print(f"Total Number of Movies available is: {len(movies_dict)}")
    print(f"Average Rating of all Movies is: {average_rating}")
    print(f"Median Rating of all Movies is: {median_rating}")
    print(f"Best Movie/s of all: {best_movie_list} with a Rating of {highest_rating}")
    print(f"Worst Movie/s of all: {worst_movie_list} with a Rating of {lowest_rating}")
    go_back_or_quit()


# Display a Random Movie from the Dictionary/List of Movies
def select_random_movie(movies_dict):
    """
    Selects a random Movie from the Movies Dictionary (movies_dict).

    Parameters:
        movies_dict["movie"] (string) : Name of the Movie
        movies_dict["rating"] (float) : Rating of the Movie

    Display:
        Message: Random Movie and its Rating from the Movies Dictionary.
    """
    random_movie = random.choice(list(movies_dict.items()))
    print(f"Your Movie for tonight is: {random_movie[0]} and its Rating is: {random_movie[1]}")
    go_back_or_quit()


# Search for a specific Movie in the Dictionary/List of Movies
def search_movie(movies_dict):
    """
    Searches a Movie entered by the User in the Movies Dictionary (movies_dict).

    Parameters:
        movies_dict["movie"] (string) : Name of the Movie
        movies_dict["rating"] (float) : Rating of the Movie

    Display:
        Message: Movie and its Rating from the Movies Dictionary.
        Message: Movie not found from the Movies Dictionary.
    """
    movie_name = input("Which Movie are you looking for? ")
    # Initialization of Variables
    movie_found = ""
    movie_rating = 0
    for movie, rating in movies_dict.items():
        if movie_name in movie:
            movie_found = movie
            movie_rating = rating
            break

    if movie_found != "":
        print()
        print(f"The Movie {movie_found} is available and has a Rating of {movie_rating}")
    else:
        print()
        print(f"The Movie {movie_name} is not found")
    go_back_or_quit()


# Display the sorted Dictionary/List of Movies by Rating
def movies_sorted_by_rating(movies_dict):
    """
    Sorts the Movies by its Rating from the Movies Dictionary (movies_dict).

    Parameters:
        movies_dict["movie"] (string) : Name of the Movie
        movies_dict["rating"] (float) : Rating of the Movie

    Display:
        Message: Sorted Movie List by its Rating from the Movies Dictionary.
    """
    movies_dict_copy = movies_dict.copy()
    sorted_list = []
    for count in range(len(movies_dict)):
        best_rating = 0
        best_movie = ""
        for movie, rating in movies_dict_copy.items():
            if rating > best_rating:
                best_rating = rating
                best_movie = movie
        sorted_list.append([best_movie, best_rating])
        del movies_dict_copy[best_movie]
    for index in range(len(sorted_list)):
        print(f"{sorted_list[index][0]}: {sorted_list[index][1]}")
    go_back_or_quit()


# Function to quit the Program while in Execution
def go_back_or_quit():
    """
    Asks the User if he/she wants to quit or carry-on using the Program.

    Display:
        Message: Thanks the User for using the Program or carries on with
        the Program Menu.
    """
    print()
    user_input = input("Go Back to Menu (Y) or Quit (N): ")
    user_input_lower = user_input.lower()
    if user_input_lower == "n":
        print()
        print("**********-----> THANK  YOU  FOR  USING  MOVIE  MANIA <-----**********")
        print()
        quit()
    elif user_input_lower != "y":
        print("Wrong Input !!!")
        go_back_or_quit()


def main():
    """
    Asks the User which Function of the Program he/she wants to execute.
    The Function calls the relevant Functions and executes it.
    """
    # Dictionary to store the movies and the rating
    movies = {
        "The Shawshank Redemption": 9.5,
        "Pulp Fiction": 8.8,
        "The Room": 3.6,
        "The Godfather": 9.2,
        "The Godfather: Part II": 9.0,
        "The Dark Knight": 9.0,
        "12 Angry Men": 8.9,
        "Everything Everywhere All At Once": 8.9,
        "Forrest Gump": 8.8,
        "Star Wars: Episode V": 8.7
    }

    user_input = ""

    while user_input != "0":
        print()
        print("**********----->  WELCOME  TO  MOVIE  MANIA <-----**********")
        print()
        print("MENU:")
        print()
        print("1. List Movies")
        print("2. Add Movie")
        print("3. Delete Movie")
        print("4. Update Movie")
        print("5. Stats")
        print("6. Random Movie")
        print("7. Search Movie")
        print("8. Movies sorted by Rating")
        print("0. Exit")
        print()

        user_input = input("Enter Choice (0-8): ")
        print()

        if user_input == "1":
            list_movies(movies)
        elif user_input == "2":
            add_movie(movies)
        elif user_input == "3":
            delete_movie(movies)
        elif user_input == "4":
            update_movie(movies)
        elif user_input == "5":
            stats(movies)
        elif user_input == "6":
            select_random_movie(movies)
        elif user_input == "7":
            search_movie(movies)
        elif user_input == "8":
            movies_sorted_by_rating(movies)
        elif user_input == "0":
            print("**********-----> THANK  YOU  FOR  USING  MOVIE  MANIA <-----**********")
            print()
        else:
            print("Wrong Input !!!")
            go_back_or_quit()


if __name__ == "__main__":
    main()
