#packages
from colorama import Fore
from modules import display_packages


def list_menu(movie_data: list):
    '''this function to enter a specific list'''

    # the section menu
    txt1 = """
        Choose from the list, by typing the number:
        1. watching list
        2. completed list
        3. plan to watch list
        0. Back

    > """

    txt2 = Fore.WHITE + txt1 # change menu color
    user_input = input(txt2)


    if user_input == "1":
        display_packages.display_watching(movie_data)
        list_menu(movie_data)
    elif user_input == "2":
        display_packages.display_completed(movie_data)
        list_menu(movie_data)
    elif user_input == "3":
        display_packages.display_plan(movie_data)
        list_menu(movie_data)
    elif user_input == "0":
        return 0
    else:
        txt = Fore.RED + "Try again..."
        raise Exception(txt)