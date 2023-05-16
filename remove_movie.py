from movie_list import Display


def remove_menu(movie_data):
    display = Display(movie_data)
    display.display()

    movie_name = input("""
    Type the movie name that you whant to remove it from the list
    - whit the same spelling - 
    - to return to the previous list type 0 -
    > """)

    for data in movie_data:
        if data["movie"] == movie_name:
            print("Deleted successfully..")
        elif movie_name == "0":
            import main
    if data not in movie_data:
        raise Exception("Try again...")

    movie_data.remove(data)