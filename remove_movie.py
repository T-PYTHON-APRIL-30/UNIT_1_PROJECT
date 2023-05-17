from movie_list import Display, DisplayMenu


def remove_menu(movie_data):
    display = Display(movie_data)
    display2 = DisplayMenu(movie_data)
    display.display()

    movie_name = input("""
    Type the movie name that you whant to remove it from the list
    - whit the same spelling - 
    - to return to the previous list type 0 -
    > """)

    count = len(movie_data)
    if movie_name == "0":
        import main
    else:
        for data in movie_data:
            if data["movie"] != movie_name:
                count -= 1
            else:
                movie_data.remove(data)

    if count == 0:
        raise Exception("Try again...")

    return display2.display()