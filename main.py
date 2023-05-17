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

recommended_games=[]

genre_input = input("What is your favorite game genre?(Shooter/Narrative/Sports/Platformer): ")
rating_input = int(input("What is the minimum rating you would like the game to have (out of 10)? "))
platform_input = input("What platform do you want to play the game on?(PC/PlayStation/Xbox/Nintendo Switch): ")

def filter_by_genre(games, selected_genre):
    return [game for game in games if selected_genre.lower() in game.genre.lower()]

def filter_by_platform(games, selected_platform):
    return [game for game in games if selected_platform.lower() in [p.lower() for p in game.platform]]

def sort_by_rating(games, n):
    sorted_games = sorted(games, key=lambda x: x.rating, reverse=True)
    return sorted_games[:n]

def filter_by_rating(games, selected_rating):
    return [game for game in games if game.rating >= selected_rating]


filtered_by_genre = filter_by_genre(games, genre_input)
filtered_by_platform = filter_by_platform(filtered_by_genre, platform_input)
filtered_by_rating= filter_by_rating(filtered_by_platform,rating_input)
# Sort the filtered list of games by rating and return the top 10
recommended_games = sort_by_rating(filtered_by_rating, 10)

# Print the recommended games
print(f"Here are some '{platform_input}' games we recommend for '{genre_input}' fans:")
for game in recommended_games:
    print(f"{game.title} - Rating: {game.rating}")