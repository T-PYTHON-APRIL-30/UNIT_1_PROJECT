from manager import cheackScore , cheackTime , pointsDeduction , Answer
from functools import reduce
import time

class Hint(Answer):
    def __init__(self, answer: str) :
        super().__init__(answer)
    def correctAnswer(self):
        return super().correctAnswer()
    
    def hintOne(self):
        return print("\n\tI've a sea!\n")
    
    def hintTwo(self):
        return print("\n\tI'm so crowded in Ramadan!\n")
    
    def hintThree(self):
        return print("\n\tThere's country in me!\n")

questionOneAnswer = Hint("Jeddah")
questionTwoAnswer = Hint("Mecca")
questionThreeAnswer = Hint("Vatican city")

def puzzle():
    '''This function will display the questions of the game'''
    score = [0]
    hintCounter = 0
    start = time.time()
    print("\n\tI'm hot in the summer and hot in the winter !\n")
    print("Who I am?")
    firstGuess = input("[ 'R' -> Riyadh - 'A' -> Abha - 'J' -> Jeddah - 'T' -> Taif ]\n'h' -> For a hint\nEnter: ").lower()
    if firstGuess == "j":
        score.append(1.5)
    elif firstGuess == "h":
        score.append(-0.25)
        hintCounter+=1
        questionOneAnswer.hintOne()
        print("Who am I?")
        firstHintGuess = input("[ 'R' -> Riyadh - 'H' -> Hail - 'J' -> Jeddah - 'T' -> Taif ]\nEnter: ").lower()
        if firstHintGuess == "j":
            score.append(1.5)
        elif firstHintGuess != "j":
            print("\nWrong Guess...")
            questionOneAnswer.correctAnswer()
    elif firstGuess != "j" and firstGuess != "h":
        print("\nWrong Guess...")
        questionOneAnswer.correctAnswer()

    print("\n\tMy visitores are more than my population!\n")
    print("Who I am?")
    secondGuess = input("[ 'Q' -> Qassim - 'M' -> Mecca - 'K' -> Kuwait - 'A' -> Alain ]\n'h' -> For a hint\nEnter: ").lower()
    if secondGuess == "m":
        score.append(1.5)
    elif secondGuess == "h":
        score.append(-0.25)
        hintCounter+=1
        questionTwoAnswer.hintTwo()
        print("Who am I?")
        secondHintGuess = input("[ 'Q' -> Qassim - 'M' -> Mecca - 'K' -> Kuwait - 'A' -> Alain ]\nEnter: ").lower()
        if secondHintGuess == "m":
            score.append(1.5)
        elif secondHintGuess != "m":
            print("\nWrong Guess...")
            questionTwoAnswer.correctAnswer()
    elif secondGuess != "m" and secondGuess != "h":
        print("\nWrong Guess...")
        questionTwoAnswer.correctAnswer()

    print("\n\tI'm the smallest city in the world!\n")
    print("Who I am?")
    thirdGuess = input("[ 'V' -> Vatican city - 'Y' -> Yanbu - 'M' -> Madrid - 'B' -> Bahrain ]\n'h' -> For a hint\nEnter: ").lower()
    if thirdGuess == "v":
        score.append(2)
    elif thirdGuess == "h":
        score.append(-0.25)
        hintCounter+=1
        questionThreeAnswer.hintThree()
        print("Who am I?")
        thirdHintGuess = input("[ 'V' -> Vatican city - 'Y' -> Yanbu - 'M' -> Madrid - 'B' -> Bahrain ]\nEnter: ").lower()
        if thirdHintGuess == "v":
            score.append(2)
        elif thirdHintGuess != "i":
            print("\nWrong Guess...")
            questionThreeAnswer.correctAnswer()
    elif thirdGuess != "i" and thirdGuess != "h":
        print("\nWrong Guess...")
        questionThreeAnswer.correctAnswer()
    
    end = time.time()
    timeTaken = round((end - start),2)
    scoreFun = reduce(lambda a,b:a+b,score)
    cheackScore(scoreFun,timeTaken)
    cheackTime(timeTaken)
    pointsDeduction(scoreFun,hintCounter,timeTaken)