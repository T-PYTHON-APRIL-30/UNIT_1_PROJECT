import pygame
from game import games,VideoGame
            

'''def recommend_game():
    while True:
        print("\nWelcome to the Video Game Recommendation System!")
        print("Please answer a few questions to help us recommend a game for you.\n")
        
        genre_input = input("What is your favorite game genre?(Shooter/Narrative/Sports/Platformer): ")
        rating_input = int(input("What is the minimum rating you would like the game to have (out of 10)? "))
        platform_input = input("What platform do you want to play the game on?(PC/PlayStation/Xbox/Nintendo Switch): ")

        recommended_games = []

        for game1 in games:
            if  genre_input.lower() in game1.genre.lower() and game1.rating >= rating_input:
                for value in  game1.platform:
                    if value == platform_input:
                        recommended_games.append(game1)
        print(recommended_games)
        if len(recommended_games) == 0:
            print("Sorry, we could not find any games that match your criteria.")
        else:
            print(f"Here are some {platform_input} games we recommend for {genre_input} fans:")
            for game in recommended_games:
                game.display_information()
        
        choice = input("\nWould you like to search for another game? (y/n) ")
        if choice.lower() != 'y':
            break

print("Thank you for using the Video Game Recommendation System!")
recommend_game()
'''
'''def image_function(url_input):
    displayWidth = 0
    displayHeight =0
    surface =pygame.display.set_mode((displayWidth,displayHeight))
    pygame.display.set_caption('Image')
    displayImage=pygame.image.load(url_input)
    while True:
        surface.fill((255,255,255))
        surface.blit(displayImage,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
'''

def image_function(url_input):
    displayImage=pygame.image.load(url_input)
    displayWidth ,displayHeight= displayImage.get_width(), displayImage.get_height()
    surface =pygame.display.set_mode((displayWidth,displayHeight))
    pygame.display.set_caption('Image')
    while True:
        surface.fill((255,255,255))
        surface.blit(displayImage,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
'''def image_function(url_input):
    displayImage=pygame.image.load(url_input)
    displayWidth ,displayHeight= displayImage.get_width(), displayImage.get_height()
    # Set the display mode and make the window the first window
    screen = pygame.display.set_mode((displayWidth,displayHeight), pygame.NOFRAME | pygame.SCALED)
    pygame.display.set_caption('Image Window')
    pygame.display.set_icon(displayImage)
    pygame.display.set_mode((1, 1))
    pygame.display.set_mode((displayWidth,displayHeight), pygame.NOFRAME | pygame.SCALED)

    # Display the image
    while True:
        screen.fill((255,255,255))
        screen.blit(displayImage,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()'''


def filter_by_genre(games, selected_genre):
    return [game for game in games if selected_genre.lower() in game.genre.lower()]

def filter_by_platform(games, selected_platform):
    return [game for game in games if selected_platform.lower() in [p.lower() for p in game.platform]]

def sort_by_rating(games, n):
    sorted_games = sorted(games, key=lambda x: x.rating, reverse=True)
    return sorted_games[:n]

def filter_by_rating(games, selected_rating):
    return [game for game in games if game.rating >= selected_rating]

def select_an_image(game_list:list,selected_game:str):
    for game in game_list:
        if selected_game.lower() == game.title.lower():
            url_input=game.url
            image_function(url_input)
            
 
    

def recommend_game():
    while True:
        try:
            print("\nWelcome to the Video Game Recommendation System!")
            print("Please answer a few questions to help us recommend a game for you.\n")
        
            genre_input = input("What is your favorite game genre?(Shooter/Narrative/Sports/Platformer): ")
            rating_input = int(input("What is the minimum rating you would like the game to have (out of 10)? "))
            platform_input = input("What platform do you want to play the game on?(PC/PlayStation/Xbox/Nintendo Switch): ")
            
            recommended_games=[]
            #if not genre_input.isspace() and type(rating_input) != int and not platform_input.isspace():
            filtered_by_genre = filter_by_genre(games, genre_input)
            filtered_by_platform = filter_by_platform(filtered_by_genre, platform_input)
            filtered_by_rating= filter_by_rating(filtered_by_platform,rating_input)
            # Sort the filtered list of games by rating and return the top 10
            recommended_games = sort_by_rating(filtered_by_rating, 10)
            if len(recommended_games) == 0:
                print("Sorry, we could not find any games that match your criteria.")
            # Print the recommended games
            else:
                print(f"Here are some '{platform_input}' games we recommend for '{genre_input}' fans:")
                for game in recommended_games:
                    print(game.display_information())
                    #print(f"{game.title} - Rating: {game.rating}")
                choice1=input("\nDo you want more information about the games we have recommend for you? (y/n)  ")
                if choice1.lower() != 'n':
                    selected_game=input("Please choose the title of the game you want to display(from the previous list) ")
                    select_an_image(recommended_games,selected_game)

        except Exception:
            print("Please provide valid value")
        else:
            choice2 = input("\nWould you like to search for another games? (y/n)  ")
            if choice2.lower() != 'y':
                break

recommend_game()
print("\nThank you for using the Video Game Recommendation System!\n")
#check for each user input 