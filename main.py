from cfonts import say
from colorama import Fore

from movie_list import DisplayMenu
from add_movie import add_menu
from remove_movie import remove_menu


movie_data = [
    {
        "movie": "SpiderMan",
        "reviwe": "Good!!",
        "rating": "★★★★☆",
        "section": "watching"
    }, {
        "movie": "SpiderMan2",
        "reviwe": "Good!!",
        "rating": "★★★★☆",
        "section": "watching"
    }, {
        "movie": "SpiderMan3",
        "reviwe": "Good!!",
        "rating": "★★★★☆",
        "section": "plan to watch"
    }
]

say('My Movie List', colors=['blue', 'yellow'], align='center')
txt = Fore.YELLOW + 'Track your movies, anytime anywhere'
print(txt.center(175), end = "\n")

main_menu = input("""
    Choose from the list, by typing the number:
    1. My list
    2. Add new movie
    3. Remove movie
    0. Exist

> """)


if int(main_menu) == 1:
    display = DisplayMenu(movie_data)
    display.display()
elif int(main_menu) == 2:
    add_menu(movie_data)
elif int(main_menu) == 3:
    remove_menu(movie_data)
elif int(main_menu) == 0:
    pass