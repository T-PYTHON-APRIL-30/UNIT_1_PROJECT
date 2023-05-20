import colorama
from colorama import Fore, Back, Style
from game import *            
from functions import *
colorama.init(autoreset=True)

def recommend_game():
    flag:bool=True
    while flag:
        try:
            print(f"{Style.BRIGHT}{Fore.MAGENTA}\nWelcome to the Video Game Recommendation System!")
            print(f"{Style.BRIGHT}{Fore.MAGENTA}Please answer a few questions to help us recommend a game for you.\n")
        
            genre_input:str = input(f"{Fore.BLUE}What is your favorite game genre?({Fore.GREEN}Shooter{Fore.BLUE}/{Fore.GREEN}Narrative{Fore.BLUE}/{Fore.GREEN}Sports{Fore.BLUE}/{Fore.GREEN}Platformer{Fore.BLUE}):{Fore.GREEN} ")
            #Check the entered value
            if not check_genre_input(genre_input):
                raise ValueError(f"{Fore.RED}\nInvalid Genre! please type in the genre from the following list: Shooter, Narrative, Sports or Platformer\n")
            rating_input:float = float(input(f"{Fore.BLUE}What is the minimum rating you would like the game to have ({Fore.GREEN}out of 10{Fore.BLUE})? {Fore.GREEN}"))
            #Check the entered type/value
            if not check_rating_input(rating_input):
                raise TypeError(f"{Fore.RED}\nInvalid Number! please provide a valid number\n")
            platform_input:str = input(f"{Fore.BLUE}What platform do you want to play the game on?({Fore.GREEN}PC{Fore.BLUE}/{Fore.GREEN}PlayStation{Fore.BLUE}/{Fore.GREEN}Xbox{Fore.BLUE}/{Fore.GREEN}Nintendo Switch{Fore.BLUE}): {Fore.GREEN}")
            #Check the entered value
            if not check_platform_input(platform_input):
                raise ValueError (f"{Fore.RED}\nInvalid Platform! please type in the platform from the following list: PC, PlayStation, Xbox, Nintendo Switch\n")
            
            recommended_games:list=[]
            #Filter the games list
            filtered_by_genre:list = filter_by_genre(games, genre_input)
            filtered_by_platform:list = filter_by_platform(filtered_by_genre, platform_input)
            filtered_by_rating:list= filter_by_rating(filtered_by_platform,rating_input)
            # Sort the filtered list of games by rating and return the top 10
            recommended_games:list = sort_by_rating(filtered_by_rating, 10)
            if len(recommended_games) == 0:
                print(f"{Fore.RED}Sorry, we could not find any games that match your criteria.")
            # Print the recommended games
            else:
                print(f"{Fore.GREEN}\nHere are some{Fore.MAGENTA} '{platform_input}'{Fore.GREEN} games we recommend for {Fore.MAGENTA}'{genre_input}' {Fore.GREEN}fans:\n")
                for game in recommended_games:
                    print(game.display_information(platform_input))
                
                while True:    
                    choice1:str=input(f"{Fore.BLUE}\nDo you want more information about the games we have recommend for you? ({Fore.GREEN}y{Fore.BLUE}/{Fore.GREEN}n{Fore.BLUE}) {Fore.GREEN}")
                    #Check the entered value
                    if not check_choices(choice1):
                        print(f"{Fore.RED}\nInvalid value! please entr 'y' for yes or 'n' for no\n")
                        continue
                    elif choice1.lower() == 'y':
                        selected_game:str=input(f"{Fore.BLUE}Please choose the title of the game you want to display({Fore.GREEN}from the previous list{Fore.BLUE}):{Fore.GREEN} ")
                        if not select_an_image(recommended_games,selected_game):
                            print(f"{Fore.RED}\nInvalid value! please entr the correct title from the previous list\n")
                            continue

                    choice2:str = input(f"{Fore.BLUE}\nWould you like to search for other games? ({Fore.GREEN}y{Fore.BLUE}/{Fore.GREEN}n{Fore.BLUE}) {Fore.GREEN} ")
                    #Check the entered value
                    if not check_choices(choice2):
                        print(f"{Fore.RED}\nInvalid value! please enter 'y' for yes or 'n' for no\n")
                        continue
                    if choice2.lower() == 'y':
                        break
                    elif choice2.lower() == 'n':
                            flag =False
                            break

           
        except ValueError as e:
            print(e)
           
        except TypeError as e:
            print(e)
           


recommend_game()
print(f"{Style.BRIGHT}{Fore.MAGENTA}{Back.WHITE}\nThank you for using the Video Game Recommendation System!\n")

