from movie_list import DisplayMenu


def add_menu(movie_data):
    movie_name = input("""Enter the movie name:
> """)
    movie_section = input("""Choose from the list, by typing the number:
    1. watching
    2. completed
    3. plan to watch
> """)
    movie_reviwe = input("""Type your reviwe about it:
    - within 200 character-
> """)
    movie_rating = input("""Rate the movie, by choosing a number 1-5
    - Be aware that 1 means very bad movie -
> """)
    movie = {
        "movie": movie_name,
        "reviwe": movie_reviwe,
        "rating": movie_rating,
        "section": movie_section
    }
    
    check_add(movie, movie_name, movie_reviwe, movie_rating, movie_section)
    movie_data.append(movie)

    display = DisplayMenu(movie_data)
    display.display()


def check_add(movie, movie_name, movie_reviwe, movie_rating, movie_section):
    if type(movie_name) != str:
        raise Exception("Enter a real movie..")
    elif len(movie_reviwe) > 200:
        raise Exception("You have exceeded the limit!!")
    
    if movie_section == "1":
        movie["section"] = "watching"
    elif movie_section == "2":
        movie["section"] = "completed"
    elif movie_section == "3":
        movie["section"] = "plan to watch"
    else:
        raise Exception("type a correct number")
    
    if movie_rating == "1":
        movie["rating"] = "★☆☆☆☆"
    elif movie_rating == "2":
        movie["rating"] = "★★☆☆☆"
    elif movie_rating == "3":
        movie["rating"] = "★★★☆☆"
    elif movie_rating == "4":
        movie["rating"] = "★★★★☆"
    elif movie_rating == "5":
        movie["rating"] = "★★★★★"
    else:
        raise Exception("type a correct number")