from game import *            
from functions import *

def recommend_game():
    flag:bool=True
    while flag:
        try:
            print("\nWelcome to the Video Game Recommendation System!")
            print("Please answer a few questions to help us recommend a game for you.\n")
        
            genre_input:str = input("What is your favorite game genre?(Shooter/Narrative/Sports/Platformer): ")
            #Check the entered value
            if not check_genre_input(genre_input):
                raise ValueError("\nInvalid Genre! please type in the genre from the following list: Shooter, Narrative, Sports or Platformer\n")
            rating_input:float = float(input("What is the minimum rating you would like the game to have (out of 10)? "))
            #Check the entered type/value
            if not check_rating_input(rating_input):
                raise TypeError("\nInvalid Number! please provide a valid number\n")
            platform_input:str = input("What platform do you want to play the game on?(PC/PlayStation/Xbox/Nintendo Switch): ")
            #Check the entered value
            if not check_platform_input(platform_input):
                raise ValueError ("\nInvalid Platform! please type in the platform from the following list: PC, PlayStation, Xbox, Nintendo Switch\n")
            
            recommended_games:list=[]
            #Filter the games list
            filtered_by_genre:list = filter_by_genre(games, genre_input)
            filtered_by_platform:list = filter_by_platform(filtered_by_genre, platform_input)
            filtered_by_rating:list= filter_by_rating(filtered_by_platform,rating_input)
            # Sort the filtered list of games by rating and return the top 10
            recommended_games:list = sort_by_rating(filtered_by_rating, 10)
            if len(recommended_games) == 0:
                print("Sorry, we could not find any games that match your criteria.")
            # Print the recommended games
            else:
                print(f"\nHere are some '{platform_input}' games we recommend for '{genre_input}' fans:\n")
                for game in recommended_games:
                    print(game.display_information(platform_input))
                
                while True:    
                    choice1:str=input("\nDo you want more information about the games we have recommend for you? (y/n)  ")
                    #Check the entered value
                    if not check_choices(choice1):
                        print("\nInvalid value! please entr 'y' for yes or 'n' for no\n")
                        continue
                    elif choice1.lower() == 'y':
                        selected_game:str=input("Please choose the title of the game you want to display(from the previous list): ")
                        if not select_an_image(recommended_games,selected_game):
                            print("\nInvalid value! please entr the correct title from the previous list\n")
                            continue

                    choice2:str = input("\nWould you like to search for other games? (y/n)  ")
                    #Check the entered value
                    if not check_choices(choice2):
                        print("\nInvalid value! please enter 'y' for yes or 'n' for no\n")
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
print("\nThank you for using the Video Game Recommendation System!\n")

