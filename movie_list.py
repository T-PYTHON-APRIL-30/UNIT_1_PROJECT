# packages
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
            print(Fore.YELLOW + "You haven't added a movie 😞")
            return 0
        else:
            table = Table(title = "My Movie List")
            table.add_column("Movie")
            table.add_column("Reviwe")
            table.add_column("Rating")


        for data in self.movie_data:
            table.add_row(data["movie"], data["reviwe"], data["rating"])

        console = Console()
        return console.print(table)
    

    def list_menu(self):
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
            display_packages.display_watching(self.movie_data)
            self.list_menu()
        elif user_input == "2":
            display_packages.display_completed(self.movie_data)
            self.list_menu()
        elif user_input == "3":
            display_packages.display_plan(self.movie_data)
            self.list_menu()
        elif user_input == "0":
            return 0
        else:
            txt = Fore.RED + "Try again..."
            raise Exception(txt)