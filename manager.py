import time

class Answer:
    def __init__(self,answer:str):
        self.answer = answer
    def correctAnswer(self):
        return print(f"\n\tThe correct naswer is ( {self.answer} ).\n")

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
    if time <= 10.0 :
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
        print(f"\n\tBad luck ! You didn't get any answer correct!\n")
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
    late = 0.25
    hint = 0.25
    deduction = float(hintUsed*hint)
    if score > 0 :
        if hintUsed == 1 :
            score+= deduction
            if timeTaken > 30.0 :
                print(f"\nYour score was {score} but you used {hintUsed} hint ({deduction}) and you were late ({late}).\n")
            else:
                print(f"\nYour score was {score} but you used {hintUsed} hint ({deduction}).\n")
    
        elif hintUsed == 2:
            score+= deduction
            if timeTaken > 30.0 :
                print(f"\nYour score was {score} but you used {hintUsed} hints ({deduction}) and you were late ({late}).\n")
            else:
                print(f"\nYour score was {score} but you used {hintUsed} hints ({deduction}).\n")
    
        elif hintUsed == 3:
            score+= deduction
            if timeTaken > 30.0 :
                print(f"\nYour score was {score} but you used {hintUsed} hints ({deduction}) and you were late ({late}).\n")
            else:
                print(f"\nYour score was {score} but you used {hintUsed} hints ({deduction}).\n")
    
        elif timeTaken > 30.0 :
                print(f"\nYour score was {score} but you were late ({late}).\n")