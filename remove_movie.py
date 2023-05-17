from colorama import Fore
from movie_list import Display, DisplayMenu


def remove_menu(movie_data: list):
    '''this function to remove a movie from the list'''

    display = Display(movie_data)
    display2 = DisplayMenu(movie_data)
    display.display()


    txt = """
    Type the movie name that you whant to remove it from the list
    - whit the same spelling - 
    - to return to the previous list type 0 -
    > """
    
    txt1 = Fore.WHITE + txt
    movie_name = input(txt1)


    count: int = len(movie_data)
    if movie_name == "0":
        import main
    else:
        for data in movie_data:
            if data["movie"] != movie_name:
                count -= 1
            else:
                movie_data.remove(data)


    if count == 0:
        txt2 = Fore.RED + "Try again..."
        raise Exception(txt2)

    return display2.display()