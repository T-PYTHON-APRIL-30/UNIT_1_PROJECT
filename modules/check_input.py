# packages
from colorama import Fore


def check_add(movie: dict, movie_name: str, movie_reviwe: str, movie_rating: str, movie_section: str):
    '''this class check user input'''

    # check name and reviwe
    if type(movie_name) != str:
        txt = Fore.RED + "Enter a real movie.."
        raise Exception(txt)
    elif len(movie_reviwe) > 200:
        txt1 = Fore.RED + "You have exceeded the limit 200 character!!"
        raise Exception(txt1)
    

    # check section and change the input
    if movie_section == "1":
        movie["section"] = "watching"
    elif movie_section == "2":
        movie["section"] = "completed"
    elif movie_section == "3":
        movie["section"] = "plan to watch"
    else:
        txt2 = Fore.RED + "type a correct number"
        raise Exception(txt2)
    
    
    # check rating and change the input
    if movie_rating == "1":
        movie["rating"] = "★☆☆☆☆"
    elif movie_rating == "2":
        movie["rating"] = "★★☆☆☆"
    elif movie_rating == "3":
        movie["rating"] = "★★★☆☆"
    elif movie_rating == "4":
        movie["rating"] = "★★★★☆"
    elif movie_rating == "5":
        movie["rating"] = "★★★★★"
    else:
        txt3 = Fore.RED + "type a correct number"
        raise Exception(txt3)