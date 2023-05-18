import time

def rules():
    '''This function explains the rules of the game to the player'''
    print("\n\tThis is the rules:")
    print("\tQuestion 1 has 1.5 points")
    print("\tQuestion 2 has 1.5 points")
    print("\tQuestion 3 has 2 points")
    print("\tAny hints it cost 0.25 points")
    print("If you late more than 30 seconds it will cost 0.25\n")

def cheackTime(time:float):
    '''This function makes sure that the time is less than or equal to 30 seconds, otherwise 0.25 points will be deducted.'''
    if time < 5.0 :
        print(f"\n\tThat was fast ! You takes only {time} seconds.\n")
    elif time > 30.0 :
        print(f"\n\tThat was late ! You takes {time} seconds.\n")
    else:
        print(f"\n\tYou takes {time} seconds.\n")

def cheackScore(total:float,time:float):
    '''This function verifies the result and displays the appropriate answer for the score along with the final score'''
    if time > 30.0 :
        total -= 0.25
    if 0.0 >= total:
        total = 0
        print(f"\n\tBad luck ! You got {total}/5 !\n")
    elif 0.0 < total < 2.0 :
        print(f"\n\tUmmm ! You got {total}/5 !\n")
    elif 2.0 <= total < 4.0 :
        print(f"\n\tNice ! You got {total}/5 !\n")
    elif total >= 4.0 :
        print(f"\n\tBravo !! You got {total}/5 !\n")

def countingThree():
    '''This function counts down from 3 to 1 .'''
    time.sleep(1)
    print("3",end=" ")
    time.sleep(1)
    print("2",end=" ")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("")

def pointsDeduction (score:float,hintUsed:int,timeTaken:float):
    '''This function displays your result before the discount and explains the reason for the discount.'''
    if hintUsed == 1 :
        score+= 0.25
        if timeTaken > 30.0 :
            #score+= 0.25
            print(f"\nYour score was {score} but you used 1 hints (0.25) and you was late (0.25).\n")
        else:
            print(f"\nYour score was {score} but you used 1 hints (0.25).\n")
    elif hintUsed == 2:
        score+= 0.5
        if timeTaken > 30.0 :
            #score+= 0.25
            print(f"\nYour score was {score} but you used 2 hints (0.5) and you was late (0.25).\n")
        else:
            print(f"\nYour score was {score} but you used 2 hints (0.5).\n")
    elif hintUsed == 3:
        score+= 0.75
        if timeTaken > 30.0 :
            #score+= 0.25
            print(f"\nYour score was {score} but you used 3 hints (0.75) and you was late (0.25).\n")
        else:
            print(f"\nYour score was {score} but you used 3 hints (0.75).\n")