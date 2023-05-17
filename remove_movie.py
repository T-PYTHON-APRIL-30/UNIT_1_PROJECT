#packages
from colorama import Fore
from movie_list import Display


def remove_menu(movie_data: list):
    '''this function to remove a movie from the list'''

    display = Display(movie_data)
    display.display() # Display movies list


    if len(movie_data) != 0:
        txt = Fore.YELLOW + 'Delete movie from your list'
        print(txt.center(175), end = "\n")
        
        txt = """
        Type the movie name that you whant to remove it from the list
        - whit the same spelling - 
        - to return to the previous list type 0 -
        > """
        
        txt1 = Fore.WHITE + txt # change text color
        movie_name = input(txt1)


        # Remove movie form the list
        count: int = len(movie_data)
        if movie_name == "0":
            return 0
        else:
            for data in movie_data:
                if data["movie"] != movie_name:
                    count -= 1
                else:
                    movie_data.remove(data)


        if count == 0:
            txt2 = Fore.RED + "Try again..."
            raise Exception(txt2)

        if len(movie_data) != 0:
            return display.display()
        else:
            return print(Fore.YELLOW + "Deleted successfully 👍")