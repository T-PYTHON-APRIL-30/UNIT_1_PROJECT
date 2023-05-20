from Questions import sportsQ , moviesQ , citiesQ
from manager import countingThree , rules

def sportsGame():
    '''This function calls the questions of this game'''
    while True:
        print("\t You have to guess the names!")
        print("\t\tAre you ready?\n")
        userChoose = str(input("'Y' -> Yes to start the game \n'Q' -> quit to choose another game\nEnter: ")).lower().strip()
        if userChoose.isalpha() and len(userChoose) == 1 :
            if userChoose == "y" :
                print("\n\t  The game is starts in",end=" ")
                countingThree()
                try: # if i update the sports questions and i did something wrong the try will catch it
                    sportsQ.puzzle()
                except:
                    print("\n**Something went wrong in the sports questions!**\n")
            elif userChoose == "q" :
                break
            else:
                print("\nWrong entry.. Try again !\n")
        else:
            print("\nWrong entry.. Try again !\n")

def moviesGame():
    '''This function calls the questions of this game'''
    while True:
        print("    You have to guess the name of the movie!")
        print("\t\tAre you ready?\n")
        userChoose = str(input("'Y' -> Yes to start the game \n'Q' -> quit to choose another game\nEnter: ")).lower().strip()
        if userChoose.isalpha() and len(userChoose) == 1 :
            if userChoose == "y" :
                print("\n\t  The game is starts in",end=" ")
                countingThree()
                try: # if i update the movies questions and i did something wrong the try will catch it
                    moviesQ.puzzle()
                except:
                    print("\n**Something went wrong in the movies questions!**\n")
            elif userChoose == "q" :
                break
            else:
                print("\nWrong entry.. Try again !\n")
        else:
            print("\nWrong entry.. Try again !\n")

def citiesGame():
    '''This function calls the questions of this game'''
    while True:
        print("    You have to guess the name of the city!")
        print("\t\tAre you ready?\n")
        userChoose = str(input("'Y' -> Yes to start the game \n'Q' -> quit to choose another game\nEnter: ")).lower().strip()
        if userChoose.isalpha() and len(userChoose) == 1 :
            if userChoose == "y" :
                print("\n\t  The game is starts in",end=" ")
                countingThree()
                try: # if i update the cities questions and i did something wrong the try will catch it
                    citiesQ.puzzle()
                except:
                    print("\n**Something went wrong in the cities questions!**\n")
            elif userChoose == "q" :
                break
            else:
                print("\nWrong entry.. Try again !\n")
        else:
            print("\nWrong entry.. Try again !\n")

def chooseCategory():
    '''This function allows the player to choose his prefered game'''
    while True:
        print("\nWhat category do you prefer?")
        userChoose = str(input("'S' -> Sports \n'M' -> Movies \n'C' -> Cities\n'Q' -> quit\nEnter: ")).lower().strip()
        if userChoose.isalpha() and len(userChoose) == 1 :
            if userChoose == "s" :
                print("\n\t  You choosing sports game!")
                rules()
                try: # if i update the sports game and i did something wrong the try will catch it
                    sportsGame() 
                except:
                    print("\n**Something went wrong in the sports game!**\n")
            elif userChoose == "m" :
                print("\n\t  You choosing movies game!")
                rules()
                try: # if i update the movies game and i did something wrong the try will catch it
                    moviesGame()
                except:
                    print("\n**Something went wrong in the movies game!**\n")
            elif userChoose == "c" :
                print("\n\t  You choosing cities game!")
                rules()
                try: # if i update the cities game and i did something wrong the try will catch it
                    citiesGame() 
                except:
                    print("\n**Something went wrong in the cities game!**\n")
            elif userChoose == "q" :
                break
            else:
                print("\nWrong entry.. Try again!")
        else:
            print("\nWrong entry.. Try again!")