import time

class Answer:
    def __init__(self,answer:str):
        self.answer = answer
    def correctAnswer(self):
        return print(f"\n\t\tWrong guess..\n\tThe correct naswer is ( {self.answer} ).")

def rules():
    '''This function explains the rules of the game to the player'''
    print("\n\t     This is the rules:\n")
    print("\t  Question 1 has 1.5 points")
    print("\t  Question 2 has 1.5 points")
    print("\t   Question 3 has 2 points")
    print("\t   Any hint will cost 0.25")
    print("If you late more than 30 seconds will cost 0.25\n")

def cheackScore(total:float,time:float):
    '''This function verifies the result and displays the appropriate answer for the score along with the final score'''
    if time > 30.0 :
        total -= 0.25
    
    if 0.0 >= total:
        print(f"\n   Bad luck! You didn't get any answer correct!")
    elif 0.0 < total < 2.0 :
        print(f"\n\t     Ummm! You got {total}/5 !")
    elif 2.0 <= total < 4.0 :
        print(f"\n\t     Nice! You got {total}/5 !")
    elif 4.0 <= total < 5.0 : 
        print(f"\n\t   Bravo!! You got {total}/5 !")
    elif total == 5.0 : 
        print(f"\n\tSuper Amazing!!! You got {total}/5 !")

def cheackTime(time:float):
    '''This function makes sure that the time is less than or equal to 30 seconds, otherwise 0.25 points will be deducted.'''
    if time < 15.0 :
        print(f"\n   That was fast ! You takes only {time} seconds.")
    elif time > 30.0 :
        print(f"\n   That was late ! You takes {time} seconds.")
    else:
        print(f"\n\t    You takes {time} seconds.")

def countingThree():
    '''This function counts down from 3 to 1 .'''
    time.sleep(1)
    for i in range(3,0,-1):
        print(i,end=" ")
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
                print(f"\n  Your score was {score} but you used {hintUsed} hint ({deduction}).\n")
    
        elif hintUsed == 2:
            score+= deduction
            if timeTaken > 30.0 :
                print(f"\nYour score was {score} but you used {hintUsed} hints ({deduction}) and you were late ({late}).\n")
            else:
                print(f"\n  Your score was {score} but you used {hintUsed} hints ({deduction}).\n")
    
        elif hintUsed == 3:
            score+= deduction
            if timeTaken > 30.0 :
                print(f"\nYour score was {score} but you used {hintUsed} hints ({deduction}) and you were late ({late}).\n")
            else:
                print(f"\n  Your score was {score} but you used {hintUsed} hints ({deduction}).\n")
    
        elif timeTaken > 30.0 :
                print(f"\n  Your score was {score} but you were late ({late}).\n")