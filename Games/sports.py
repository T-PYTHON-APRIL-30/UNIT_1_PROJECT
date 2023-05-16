from Questions import sportsQ
def sportsGame():
    while True:
        print("You have to guess what is the sport !")
        print("Are you ready?")
        start_game = str(input("'Y' -> Yes to start the game \n'N' -> No to choose another game\nEnter: ")).lower()
        if not start_game.isdigit() and len(start_game) == 1 :
            if start_game == "y" :
                print("The game is starts...")
                sportsQ.puzzle()
            elif start_game == "n" :
                break
            else:
                print("\nWrong entry.. Try again !")
        else:
            print("\nWrong entrt.. Try again !")