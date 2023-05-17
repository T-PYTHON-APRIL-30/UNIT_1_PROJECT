from rich.console import Console
from rich.table import Table


data_list: list = [] #list to store specific section

def display_watching(movie_data: list):
    '''this function to display the watching list'''

    data_list.clear()
    for data in movie_data:
        if data["section"] == "watching":
            data_list.append(data)


    if len(data_list) == 0:
        print("You haven't added a movie 😞")
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

    data_list.clear()
    for data in movie_data:
        if data["section"] == "completed":
            data_list.append(data)


    if len(data_list) == 0:
        print("You haven't added a movie 😞")
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

    data_list.clear()
    for data in movie_data:
        if data["section"] == "plan to watch":
            data_list.append(data)


    if len(data_list) == 0:
        print("You haven't added a movie 😞")
    else:
        table = Table(title = "My plan to watch List")
        table.add_column("Movie")
        table.add_column("Reviwe")
        table.add_column("Rating")

        for data in data_list:
            table.add_row(data["movie"], data["reviwe"], data["rating"])
        
        console = Console()
        return console.print(table)