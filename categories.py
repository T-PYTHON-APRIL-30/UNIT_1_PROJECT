from Questions import sportsQ , moviesQ , citiesQ
from manager import countingThree , rules

def sportsGame():
    '''This function calls the questions of this game'''
    while True:
        print("You have to guess what is the sport !")
        print("Are you ready?")
        userChoose = str(input("'Y' -> Yes to start the game \n'N' -> No to choose another game\nEnter: ")).lower()
        if userChoose.isalpha() and len(userChoose) == 1 :
            if userChoose == "y" :
                print("The game is starts in",end=" ")
                countingThree()
                try: # if i update the sports questions and i did something wrong the try will catch it
                    sportsQ.puzzle()
                except:
                    print("Something went wrong in the sports questions!")
            elif userChoose == "n" :
                break
            else:
                print("\nWrong entry.. Try again !\n")
        else:
            print("\nWrong entry.. Try again !\n")

def moviesGame():
    '''This function calls the questions of this game'''
    while True:
        print("You have to guess what is the movie !")
        print("Are you ready?")
        userChoose = str(input("'Y' -> Yes to start the game \n'N' -> No to choose another game\nEnter: ")).lower()
        if userChoose.isalpha() and len(userChoose) == 1 :
            if userChoose == "y" :
                print("The game is starts in",end=" ")
                countingThree()
                try: # if i update the movies questions and i did something wrong the try will catch it
                    moviesQ.puzzle()
                except:
                    print("Something went wrong in the movies questions!")
            elif userChoose == "n" :
                break
            else:
                print("\nWrong entry.. Try again !\n")
        else:
            print("\nWrong entry.. Try again !\n")

def citiesGame():
    '''This function calls the questions of this game'''
    while True:
        print("You have to guess what is the city !")
        print("Are you ready?")
        userChoose = str(input("'Y' -> Yes to start the game \n'N' -> No to choose another game\nEnter: ")).lower()
        if userChoose.isalpha() and len(userChoose) == 1 :
            if userChoose == "y" :
                print("The game is starts in",end=" ")
                countingThree()
                try: # if i update the cities questions and i did something wrong the try will catch it
                    citiesQ.puzzle()
                except:
                    print("Something went wrong in the cities questions!")
            elif userChoose == "n" :
                break
            else:
                print("\nWrong entry.. Try again !\n")
        else:
            print("\nWrong entry.. Try again !\n")

def chooseCategory():
    '''This function allows the player to choose his prefered game'''
    while True:
        print("What category do you prefer?")
        userChoose = str(input("'s' -> Sports \n'm' -> Movies \n'c' -> Cities\n'e' -> Exit\nEnter: ")).lower()
        if userChoose.isalpha() and len(userChoose) == 1 :
            if userChoose == "s" :
                print("You choose sports")
                rules()
                try: # if i update the sports game and i did something wrong the try will catch it
                    sportsGame() 
                except:
                    print("Something went wrong in the sports game!")
            elif userChoose == "m" :
                print("You choose movies")
                rules()
                try: # if i update the movies game and i did something wrong the try will catch it
                    moviesGame()
                except:
                    print("Something went wrong in the movies game!")
            elif userChoose == "c" :
                print("You choose cities")
                rules()
                try: # if i update the cities game and i did something wrong the try will catch it
                    citiesGame() 
                except:
                    print("Something went wrong in the cities game!")
            elif userChoose == "e" :
                break
            else:
                print("\nWrong entry.. Try again !\n")
        else:
            print("\nWrong entry.. Try again !\n")