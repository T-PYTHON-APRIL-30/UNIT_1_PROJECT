#packages
from colorama import Fore

from modules import check_input
from movie_list import Display, DisplayMenu


def section_menu(movie_data: list):
    '''this function to edit movie list'''

    display = Display(movie_data)
    display2 = DisplayMenu(movie_data)
    display.display()


    txt1 = """Enter the movie name:
> """
    txt2 = """Choose from the list, by typing the number:
    1. watching
    2. completed
    3. plan to watch
> """
    txt3 = """Type your reviwe about it:
    - within 200 character-
> """
    txt4 = """Rate the movie, by choosing a number 1-5
    - Be aware that 1 means very bad movie -
> """

    # change text color
    txt1_1 = Fore.WHITE + txt1
    txt1_2 = Fore.WHITE + txt2
    txt1_3 = Fore.WHITE + txt3
    txt1_4 = Fore.WHITE + txt4

    # the edit list menu
    movie_name = input(txt1_1)
    movie_section = input(txt1_2)
    movie_reviwe = input(txt1_3)
    movie_rating = input(txt1_4)

    movie2: dict = {
        "movie": movie_name,
        "reviwe": movie_reviwe,
        "rating": movie_rating,
        "section": movie_section
    }
    
    check_input.check_add(movie2, movie_name, movie_reviwe, movie_rating, movie_section)

    # update the movie list
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
        txt5 = Fore.RED + "Try again..."
        raise Exception(txt5)

    return display2.display()