import pygame
from game import *

def check_rating_input(number:float)->bool:
    flag:bool=False
    if type(number) == float:
        if number >0 and number <=10:
            flag =True
    return flag

def check_choices(choice_input:str)->bool:
    flag:bool =False
    if choice_input.lower()=='y':
        flag=True
    elif choice_input.lower()=='n':
        flag=True
    return flag

def check_genre_input(genre_input:str)->bool:
    flag:bool = False
    for genre in genre_list:
        if genre.lower() in genre_input.lower():
            flag=True
    return flag

def check_platform_input(platform_input:str)->bool:
    flag:bool =False
    for platform in platform_list:
        if platform.lower() in platform_input.lower():
            flag=True
    return flag        

def filter_by_genre(games:list, selected_genre:str)->list:
    '''This function takes two parameters one is a list from the class videoGame, and another is a genre chosen by the userand then filters the list by genre'''
    return [game for game in games if selected_genre.lower() in game.genre.lower()]

def filter_by_platform(games:list, selected_platform:str)->list:
    '''This function takes two parameters one is a list that was filtered by genre, and another is a platform chosen by the user and then filters the list by platform'''
    return [game for game in games if selected_platform.lower() in [p.lower() for p in game.platform]]

def filter_by_rating(games:list, selected_rating:float)->list:
    '''This function takes two parameters one is a list that was filtered by platform & genre, and another is a rating chosen by the user and then filters the list by rating'''
    return [game for game in games if game.rating >= selected_rating]

def sort_by_rating(games:list, n:int)->list:
    '''Ths function sort the filtered list of games by rating and return the top 10'''
    sorted_games = sorted(games, key=lambda x: x.rating, reverse=True)
    return sorted_games[:n]

'''def image_function(url_input:str):
    Function to display the image on the screen  by 'pygame' package

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
            pygame.display.update()'''

def image_function(url_input:str):
    '''Function to display the image on the screen  by 'pygame' package'''  
    
    pygame.init()

    # Load the image
    image = pygame.image.load(url_input)

    # Set the display mode and make the window the first window
    displayWidth ,displayHeight= image.get_width(), image.get_height()
    surface =pygame.display.set_mode((displayWidth,displayHeight))
    pygame.display.set_caption('Image')

    # Display the image
    surface.blit(image, (0, 0))
    pygame.display.flip()

    # Wait for the user to close the window
    running = True
    while running:
        surface.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit() 


def select_an_image(game_list:list,selected_game:str)->bool:
    flag:bool=False
    for game in game_list:
        if selected_game.lower() == game.title.lower():
            url_input=game.url
            flag=True
            image_function(url_input)
        
    return flag


