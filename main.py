#packages
from cfonts import say
from colorama import Fore

from movie_list import Display
from add_movie import add_menu
from remove_movie import remove_menu
from list_sections import section_menu
from statistics_list import status
from modules import section_menu


movie_data: list = [] # list to store user data

# Display logo
say('My Movie List', colors=['blue', 'yellow'], align='center')
txt = Fore.YELLOW + 'Track your movies, anytime anywhere'
print(txt.center(175), end = "\n")

while True:
    # the main list menu
    txt1 = """
        Choose from the list, by typing the number:
        1. My list
        2. Add new movie
        3. Remove movie
        4. edit the list
        5. My list stats
        0. Exist

    > """
    txt2 = Fore.BLUE + txt1 # change main menu color
    main_menu = input(txt2)
    
    # Move to other lists
    try:
        if main_menu == "1":
            display = Display(movie_data)
            display.display()
            if len(movie_data) != 0:
                section_menu.list_menu(movie_data)
        elif main_menu == "2":
            add_menu(movie_data)
        elif main_menu == "3":
            remove_menu(movie_data)
        elif main_menu == "4":
            section_menu(movie_data)
        elif main_menu == "5":
            status(movie_data)
        elif main_menu == "0":
            txt = Fore.YELLOW + 'Developed by Yousef-Alsaadan ©'
            print(txt.center(175), end = "\n")
            break
        else:
            txt3 = Fore.RED + "Try again..."
            raise Exception(txt3)
    except Exception as e:
        print(e)