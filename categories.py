from Questions import sportsQ , moviesQ , citiesQ
from manager import countingThree , rules

def sportsGame():
    while True:
        print("You have to guess what is the sport !")
        print("Are you ready?")
        start_game = str(input("'Y' -> Yes to start the game \n'N' -> No to choose another game\nEnter: ")).lower()
        if start_game.isalpha() and len(start_game) == 1 :
            if start_game == "y" :
                print("The game is starts in",end=" ")
                countingThree()
                sportsQ.puzzle()
            elif start_game == "n" :
                break
            else:
                print("\nWrong entry.. Try again !\n")
        else:
            print("\nWrong entry.. Try again !\n")

def moviesGame():
    while True:
        print("You have to guess what is the movie !")
        print("Are you ready?")
        start_game = str(input("'Y' -> Yes to start the game \n'N' -> No to choose another game\nEnter: ")).lower()
        if start_game.isalpha() and len(start_game) == 1 :
            if start_game == "y" :
                print("The game is starts in",end=" ")
                countingThree()
                moviesQ.puzzle()
            elif start_game == "n" :
                break
            else:
                print("\nWrong entry.. Try again !\n")
        else:
            print("\nWrong entry.. Try again !\n")

def citiesGame():
    while True:
        print("You have to guess what is the city !")
        print("Are you ready?")
        start_game = str(input("'Y' -> Yes to start the game \n'N' -> No to choose another game\nEnter: ")).lower()
        if start_game.isalpha() and len(start_game) == 1 :
            if start_game == "y" :
                print("The game is starts in",end=" ")
                countingThree()
                citiesQ.puzzle()
            elif start_game == "n" :
                break
            else:
                print("\nWrong entry.. Try again !\n")
        else:
            print("\nWrong entry.. Try again !\n")

def chooseCategory():
    while True:
        print("What category do you prefere?")
        start_game = str(input("'s' -> Sports \n'm' -> Movies \n'c' -> Cities\n'e' -> Exit\nEnter: ")).lower()
        if start_game.isalpha() and len(start_game) == 1 :
            if start_game == "s" :
                print("You choose sports")
                rules()
                sportsGame() 
            elif start_game == "m" :
                print("You choose movies")
                rules()
                moviesGame()
            elif start_game == "c" :
                print("You choose cities")
                rules()
                citiesGame()
            elif start_game == "e" :
                break
            else:
                print("\nWrong entry.. Try again !\n")
        else:
            print("\nWrong entry.. Try again !\n")