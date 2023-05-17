import categories
print("Guessing Game")
while True :
    print("Do you want to start the game?")
    start_game = str(input("'Y' -> Yes \n'N' -> No \nEnter: ")).lower()
    if start_game.isalpha() and len(start_game) == 1 :
        if start_game == "y" :
            categories.chooseCategory()
        elif start_game == "n" :
            print("\n\tSee You Soon (;\n")
            break
        else:
            print("\nWrong entry.. Try again !\n")
    else:
        print("\nWrong entrt.. Try again ! 1\n")