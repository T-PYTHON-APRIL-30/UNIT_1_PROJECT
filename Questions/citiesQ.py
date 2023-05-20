from manager import cheackScore , cheackTime , pointsDeduction , Answer
from functools import reduce
import time

class Hint(Answer):
    def __init__(self, answer: str) :
        super().__init__(answer)
    def correctAnswer(self):
        return super().correctAnswer()
    
    def hintOne(self):
        return print("\n\tI've also the Red See Mall!\n")
    
    def hintTwo(self):
        return print("\n\tI'm so crowded in Ramadan!\n")
    
    def hintThree(self):
        return print("\n\tI'm a kingdom!\n")

questionOneAnswer = Hint("Jeddah")
questionTwoAnswer = Hint("Mecca")
questionThreeAnswer = Hint("Riyadh")

def puzzle():
    '''This function will display the questions of the game'''
    score = [0]
    hintCounter = 0
    start = time.time()
    print("\n\tThey call me 'Red Sea Bride'!\n")
    print("Who am I?")
    firstGuess = input("[ 'N' -> Neum - 'A' -> Abha - 'J' -> Jeddah - 'Y' -> Yanbu ]\n'H' -> For a hint\nEnter: ").lower().strip()
    if firstGuess == "j":
        score.append(1.5)
    elif firstGuess == "h":
        score.append(-0.25)
        hintCounter+=1
        questionOneAnswer.hintOne()
        print("Who am I?")
        firstHintGuess = input("[ 'N' -> Neum - 'A' -> Abha - 'J' -> Jeddah - 'Y' -> Yanbu ]\nEnter: ").lower().strip()
        if firstHintGuess == "j":
            score.append(1.5)
        elif firstHintGuess != "j":
            questionOneAnswer.correctAnswer()
    elif firstGuess != "j" and firstGuess != "h":
        questionOneAnswer.correctAnswer()

    print("\n\tMy visitores are more than my population!\n")
    print("Who am I?")
    secondGuess = input("[ 'Q' -> Qassim - 'M' -> Mecca - 'K' -> Kuwait - 'A' -> Alain ]\n'H' -> For a hint\nEnter: ").lower().strip()
    if secondGuess == "m":
        score.append(1.5)
    elif secondGuess == "h":
        score.append(-0.25)
        hintCounter+=1
        questionTwoAnswer.hintTwo()
        print("Who am I?")
        secondHintGuess = input("[ 'Q' -> Qassim - 'M' -> Mecca - 'K' -> Kuwait - 'A' -> Alain ]\nEnter: ").lower().strip()
        if secondHintGuess == "m":
            score.append(1.5)
        elif secondHintGuess != "m":
            questionTwoAnswer.correctAnswer()
    elif secondGuess != "m" and secondGuess != "h":
        questionTwoAnswer.correctAnswer()
        
    print("\n\tI have metro to transportation in me!\n")
    print("Who am I?")
    thirdGuess = input("[ 'R' -> Riyadh - 'T' -> Taif - 'M' -> Madinah - 'B' -> Bahrain ]\n'H' -> For a hint\nEnter: ").lower().strip()
    if thirdGuess == "r":
        score.append(2)
    elif thirdGuess == "h":
        score.append(-0.25)
        hintCounter+=1
        questionThreeAnswer.hintThree()
        print("Who am I?")
        thirdHintGuess = input("[ 'R' -> Riyadh - 'T' -> Taif - 'M' -> Madinah - 'B' -> Bahrain ]\nEnter: ").lower().strip()
        if thirdHintGuess == "r":
            score.append(2)
        elif thirdHintGuess != "r":
            questionThreeAnswer.correctAnswer()
    elif thirdGuess != "r" and thirdGuess != "h":
        questionThreeAnswer.correctAnswer()
    
    end = time.time()
    timeTaken = round((end - start),2)
    scoreFun = reduce(lambda a,b:a+b,score)
    cheackScore(scoreFun,timeTaken)
    cheackTime(timeTaken)
    pointsDeduction(scoreFun,hintCounter,timeTaken)