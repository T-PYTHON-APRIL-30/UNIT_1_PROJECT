#packages
from colorama import Fore

from movie_list import Display
from modules import check_input


def add_menu(movie_data: list):
    '''this function to add a movie in the list'''

    txt = Fore.YELLOW + 'Add new movie to your list'
    print(txt.center(175), end = "\n")

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

    # the add movie menu
    movie_name = input(txt1_1)
    movie_section = input(txt1_2)
    movie_reviwe = input(txt1_3)
    movie_rating = input(txt1_4)
    
    movie: dict = {
        "movie": movie_name,
        "reviwe": movie_reviwe,
        "rating": movie_rating,
        "section": movie_section
    }
    
    check_input.check_add(movie, movie_name, movie_reviwe, movie_rating, movie_section)
    movie_data.append(movie) # add new movie to the list

    display = Display(movie_data)
    return display.display()