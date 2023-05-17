from modules import check_input
from movie_list import Display, DisplayMenu


def section_menu(movie_data):
    display = Display(movie_data)
    display2 = DisplayMenu(movie_data)
    display.display()
    movie_name = input("""
        Enter the movie name:
        - whit the same spelling -
    > """)
    movie_section = input("""
        Choose from the list, by typing the number:
        1. watching
        2. completed
        3. plan to watch
    > """)
    movie_reviwe = input("""
        Type your reviwe about it:
        - within 200 character-
    > """)
    movie_rating = input("""
        Rate the movie, by choosing a number 1-5
        - Be aware that 1 means very bad movie -
    > """)
    movie2 = {
        "movie": movie_name,
        "reviwe": movie_reviwe,
        "rating": movie_rating,
        "section": movie_section
    }
    check_input.check_add(movie2, movie_name, movie_reviwe, movie_rating, movie_section)
    count = len(movie_data)
    if movie_name == "0":
        import main
    else:
        for data in movie_data:
            if data["movie"] != movie_name:
                count -= 1
            else:
                data.update(movie2)

    if count == 0:
        print(count)
        raise Exception("Try again...")

    return display2.display()