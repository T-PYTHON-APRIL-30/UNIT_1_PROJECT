from manager import cheackScore , cheackTime , pointsDeduction , Answer
from functools import reduce
import time

class Hint(Answer):
    def __init__(self, answer: str) :
        super().__init__(answer)
    def correctAnswer(self):
        return super().correctAnswer()
    
    def hintOne(self):
        return print("\n\tMy daughter become older than me!\n")
    
    def hintTwo(self):
        return print("\n\tI'm an inestigative movie!\n")
    
    def hintThree(self):
        return print("\n\tAvada Kedavra!\n")

questionOneAnswer = Hint("Interstellar")
questionTwoAnswer = Hint("Prisoners")
questionThreeAnswer = Hint("Harry Potter")

def puzzle():
    '''This function will display the questions of the game'''
    score = [0]
    hintCounter = 0
    start = time.time()
    print("\n\tThey sent me to space for science!\n")
    print("Who am I?")
    firstGuess = input("[ 'J' -> Joker Or 'I' -> Interstellar Or 'D' -> Django Or 'B' -> Batman ]\n'h' -> for a hint\nEnter: ").lower()
    if firstGuess == "i":
        score.append(1.5)
    elif firstGuess == "h":
        score.append(-0.25)
        hintCounter+=1
        questionOneAnswer.hintOne()
        print("Who am I?")
        firstHintGuess = input("[ 'J' -> Joker - 'I' -> Interstellar - 'D' -> Django - 'B' -> Batman ]\nEnter: ").lower()
        if firstHintGuess == "i":
            score.append(1.5)
        elif firstHintGuess != "i":
            print("\nWrong Guess...")
            questionOneAnswer.correctAnswer()
    elif firstGuess != "i" and firstGuess != "h":
        print("\nWrong Guess...")
        questionOneAnswer.correctAnswer()

    print("\n\tThey kidnapped my little girl!\n")
    print("Who am I?")
    secondGuess = input("[ 'N' -> NoBody Or 'S' -> Scarface Or 'D' -> Django Or 'P' -> Prisoners ]\n'h' -> for a hint\nEnter: ").lower()
    if secondGuess == "p":
        score.append(1.5)
    elif secondGuess == "h":
        score.append(-0.25)
        hintCounter+=1
        questionTwoAnswer.hintTwo()
        print("Who am I?")
        secondHintGuess = input("[ 'N' -> NoBody Or 'S' -> Scarface Or 'D' -> Django Or 'P' -> Prisoners ]\nEnter: ").lower()
        if secondHintGuess == "p":
            score.append(1.5)
        elif secondHintGuess != "p":
            print("\nWrong Guess...")
            questionTwoAnswer.correctAnswer()
    elif secondGuess != "p" and secondGuess != "h":
        print("\nWrong Guess...")
        questionTwoAnswer.correctAnswer()

    print("\n\tI'm the killing spell!\n")
    print("Who am I?")
    thirdGuess = input("[ 'A' -> Avatar - 'N' -> the Nun - 'F' -> Fargo - 'P' -> Harry Potter ]\n'h' -> for a hint\nEnter: ").lower()
    if thirdGuess == "p":
        score.append(2)
    elif thirdGuess == "h":
        score.append(-0.25)
        hintCounter+=1
        questionThreeAnswer.hintThree()
        print("Who am I?")
        thirdHintGuess = input("[ 'A' -> Avatar - 'N' -> the Nun - 'F' -> Fargo - 'P' -> Harry Potter ]\nEnter: ").lower()
        if thirdHintGuess == "p":
            score.append(2)
        elif thirdHintGuess != "p":
            print("\nWrong Guess...")
            questionThreeAnswer.correctAnswer()
    elif thirdGuess != "p" and thirdGuess != "h":
        print("\nWrong Guess...")
        questionThreeAnswer.correctAnswer()
    
    end = time.time()
    timeTaken = round((end - start),2)
    scoreFun = reduce(lambda a,b:a+b,score)
    cheackTime(timeTaken)
    cheackScore(scoreFun,timeTaken)
    pointsDeduction(scoreFun,hintCounter,timeTaken)