from Games import sports,movies,cities

def rules():
    print("\n\tThis is the rules:")
    print("\tQuestion 1 has 1.5 points")
    print("\tQuestion 2 has 1.5 points")
    print("\tQuestion 3 has 2 points")
    print("\tAny hints it cost 0.5 points\n")

def chooseCategory():
    while True:
        print("What category do you prefere?")
        start_game = str(input("'s' -> Sports \n'm' -> Movies \n'c' -> Cities\n'e' -> Exit\nEnter: ")).lower()
        if not start_game.isdigit() and len(start_game) == 1 :
            if start_game == "s" :
                print("You choose sports")
                rules()
                sports.sportsGame() 
            elif start_game == "m" :
                print("You choose movies")
                rules()
                movies.moviesGame()
            elif start_game == "c" :
                print("You choose cities")
                rules()
                cities.citiesGame()
            elif start_game == "e" :
                break
            else:
                print("\nWrong entry.. Try again !")
        else:
            print("\nWrong entrt.. Try again !")