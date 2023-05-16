from game import games,VideoGame

'''def add_recommend(new_list:list,game:VideoGame):
    length=len(game)
    index_number=0
    for obj in game:
        if index_number <= length:
            new_list[index_number]=obj
            index_number+=1'''
            

def recommend_game():
    while True:
        print("\nWelcome to the Video Game Recommendation System!")
        print("Please answer a few questions to help us recommend a game for you.\n")
        
        genre = input("What is your favorite game genre? ")
        rating = int(input("What is the minimum rating you would like the game to have (out of 10)? "))
        platform = input("What platform do you want to play the game on? ")

        recommended_games = []
        
        for game1 in games:
            if  genre.lower() in game1.genre.lower() and game1.rating >= rating and platform in game1.platform:
                recommended_games.append(game1)
        print(recommended_games)
        if len(recommended_games) == 0:
            print("Sorry, we could not find any games that match your criteria.")
        else:
            print(f"Here are some {platform} games we recommend for {genre} fans:")
            for game in recommended_games:
                game.display_information()
        
        choice = input("\nWould you like to search for another game? (y/n) ")
        if choice.lower() != 'y':
            break

print("Thank you for using the Video Game Recommendation System!")
recommend_game()


'''     '''