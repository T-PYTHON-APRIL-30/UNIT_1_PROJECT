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
        return print("\n\tI'm mafia guy!\n")
    
    def hintThree(self):
        return print("\n\tAvada Kedavra!\n")

questionOneAnswer = Hint("Interstellar")
questionTwoAnswer = Hint("Scarface")
questionThreeAnswer = Hint("Harry Potter")

def puzzle():
    '''This function will display the questions of the game'''
    score = [0]
    hintCounter = 0
    start = time.time()
    print("\n\tThey sent me to space for science!\n")
    print("Who am I?")
    firstGuess = input("[ 'J' -> Joker - 'I' -> Interstellar - 'D' -> Django - 'B' -> Batman ]\n'H' -> for a hint\nEnter: ").lower().strip()
    if firstGuess == "i":
        score.append(1.5)
    elif firstGuess == "h":
        score.append(-0.25)
        hintCounter+=1
        questionOneAnswer.hintOne()
        print("Who am I?")
        firstHintGuess = input("[ 'J' -> Joker - 'I' -> Interstellar - 'D' -> Django - 'B' -> Batman ]\nEnter: ").lower().strip()
        if firstHintGuess == "i":
            score.append(1.5)
        elif firstHintGuess != "i":
            questionOneAnswer.correctAnswer()
    elif firstGuess != "i" and firstGuess != "h":
        questionOneAnswer.correctAnswer()

    print("\n\t'Say hello to My little frind!'\n")
    print("Who am I?")
    secondGuess = input("[ 'N' -> NoBody - 'S' -> Scarface - 'C' -> Creed - 'T' -> Tenet ]\n'H' -> for a hint\nEnter: ").lower().strip()
    if secondGuess == "s":
        score.append(1.5)
    elif secondGuess == "h":
        score.append(-0.25)
        hintCounter+=1
        questionTwoAnswer.hintTwo()
        print("Who am I?")
        secondHintGuess = input("[ 'N' -> NoBody - 'S' -> Scarface - 'C' -> Creed - 'T' -> Tenet ]\nEnter: ").lower().strip()
        if secondHintGuess == "s":
            score.append(1.5)
        elif secondHintGuess != "s":
            questionTwoAnswer.correctAnswer()
    elif secondGuess != "s" and secondGuess != "h":
        questionTwoAnswer.correctAnswer()

    print("\n\tI'm the killing spell!\n")
    print("Who am I?")
    thirdGuess = input("[ 'A' -> Avatar - 'N' -> the Nun - 'F' -> Fargo - 'P' -> Harry Potter ]\n'H' -> for a hint\nEnter: ").lower().strip()
    if thirdGuess == "p":
        score.append(2)
    elif thirdGuess == "h":
        score.append(-0.25)
        hintCounter+=1
        questionThreeAnswer.hintThree()
        print("Who am I?")
        thirdHintGuess = input("[ 'A' -> Avatar - 'N' -> the Nun - 'F' -> Fargo - 'P' -> Harry Potter ]\nEnter: ").lower().strip()
        if thirdHintGuess == "p":
            score.append(2)
        elif thirdHintGuess != "p":
            questionThreeAnswer.correctAnswer()
    elif thirdGuess != "p" and thirdGuess != "h":
        questionThreeAnswer.correctAnswer()
    
    end = time.time()
    timeTaken = round((end - start),2)
    scoreFun = reduce(lambda a,b:a+b,score)
    cheackTime(timeTaken)
    cheackScore(scoreFun,timeTaken)
    pointsDeduction(scoreFun,hintCounter,timeTaken)