#packages
from rich.console import Console
from rich.table import Table
from colorama import Fore


data_list: list = [] #list to store specific section

def display_watching(movie_data: list):
    '''this function to display the watching list'''

    # Split the main movie list
    data_list.clear()
    for data in movie_data:
        if data["section"] == "watching":
            data_list.append(data)


    # display watching list
    if len(data_list) == 0:
        print(Fore.YELLOW + "You haven't added a movie 😞")
    else:
        table = Table(title = "My Watching List")
        table.add_column("Movie")
        table.add_column("Reviwe")
        table.add_column("Rating")

        for data in data_list:
            table.add_row(data["movie"], data["reviwe"], data["rating"])
        
        console = Console()
        return console.print(table)


def display_completed(movie_data: list):
    '''this function to display the completed list'''

    # Split the main movie list
    data_list.clear()
    for data in movie_data:
        if data["section"] == "completed":
            data_list.append(data)


    # display watching list
    if len(data_list) == 0:
        print(Fore.YELLOW + "You haven't added a movie 😞")
    else:
        table = Table(title = "My Completed List")
        table.add_column("Movie")
        table.add_column("Reviwe")
        table.add_column("Rating")

        for data in data_list:
            table.add_row(data["movie"], data["reviwe"], data["rating"])
        
        console = Console()
        return console.print(table)


def display_plan(movie_data: list):
    '''this function to display the paln to watch list'''

    # Split the main movie list
    data_list.clear()
    for data in movie_data:
        if data["section"] == "plan to watch":
            data_list.append(data)


    # display watching list
    if len(data_list) == 0:
        print(Fore.YELLOW + "You haven't added a movie 😞")
    else:
        table = Table(title = "My plan to watch List")
        table.add_column("Movie")
        table.add_column("Reviwe")
        table.add_column("Rating")

        for data in data_list:
            table.add_row(data["movie"], data["reviwe"], data["rating"])
        
        console = Console()
        return console.print(table)