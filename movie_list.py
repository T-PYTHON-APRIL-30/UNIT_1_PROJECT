from rich.console import Console
from rich.table import Table
from colorama import Fore

from modules import display_packages


class Display:
    '''this class to display user movie list'''

    def __init__(self, movie_data: list):
        self.movie_data = movie_data
    
    
    def display(self):
        if len(self.movie_data) == 0:
            print("You haven't added a movie 😞")
            import main
        else:
            table = Table(title = "My Movie List")
            table.add_column("Movie")
            table.add_column("Reviwe")
            table.add_column("Rating")


        for data in self.movie_data:
            table.add_row(data["movie"], data["reviwe"], data["rating"])

        console = Console()
        return console.print(table)


class DisplayMenu(Display):
    def __init__(self, movie_data: list):
        super().__init__(movie_data)
    
    def display(self):
        super().display()
        return list_menu(self.movie_data)


def list_menu(movie_data: list):
    '''this function to enter a specific list'''

    # the section menu
    user_input = input("""
        Choose from the list, by typing the number:
        1. watching list
        2. completed list
        3. plan to watch list
        0. Back

    > """)


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
        import main
    else:
        txt = Fore.RED + "Try again..."
        raise Exception(txt)