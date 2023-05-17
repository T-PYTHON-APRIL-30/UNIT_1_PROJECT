from movie_list import DisplayMenu
from modules import check_input


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
    
    check_input.check_add(movie, movie_name, movie_reviwe, movie_rating, movie_section)
    movie_data.append(movie)

    display = DisplayMenu(movie_data)
    display.display()