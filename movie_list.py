#packages
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