import categories

print("\n\t Guess Game\n")
while True :
    print("Do you want to start the game?")
    start_game = str(input("'Y' -> Yes \n'Q' -> quit \nEnter: ")).lower().strip()
    if start_game.isalpha() and len(start_game) == 1 :
        if start_game == "y" :
            try:
                categories.chooseCategory()
            except:
                print("Something went wrong in the Categories!")
        elif start_game == "q" :
            print("\n\tSee You Soon (;\n")
            break
        else:
            print("\nWrong entry.. Try again !\n")
    else:
        print("\nWrong entry.. Try again ! \n")