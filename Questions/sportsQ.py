from manager import cheackScore , cheackTime , pointsDeduction , Answer
from functools import reduce
import time
    
class Hint(Answer):
    def __init__(self, answer: str) :
        super().__init__(answer)
    def correctAnswer(self):
        return super().correctAnswer()
    
    def hintOne(self):
        return print("\n\tSiiuuuu!\n")
    
    def hintTwo(self):
        return print("\n\tPart of my name it's from my city!\n")
    
    def hintThree(self):
        return print("\n\tMy country are famous in spaghetti!\n")

questionOneAnswer = Hint("Cristiano Ronaldo")
questionTwoAnswer = Hint("Real Madrid")
questionThreeAnswer = Hint("Italy")

def puzzle():
    '''This function will display the questions of the game'''
    score = [0]
    hintCounter = 0
    start = time.time()
    print("\n\tI'm well known worldwide and play in an Saudi leage!\n")
    print("Who am I?")
    firstGuess = input("[ 'M' -> Mohammed Noor - 'Z' -> Zlatan - 'C' -> Cristiano Ronaldo - 'L' -> Lionel Messi ]\n'h' -> For a hint\nEnter: ").lower()
    if firstGuess == "c":
        score.append(1.5)
    elif firstGuess == "h":
        score.append(-0.25)
        hintCounter+=1
        questionOneAnswer.hintOne()
        print("Who am I?")
        firstHintGuess = input("[ 'M' -> Mohammed Salah - 'Z' -> Zlatan - 'C' -> Cristiano Ronaldo - 'L' -> Lionel Messi ]\nEnter: ").lower()
        if firstHintGuess == "c":
            score.append(1.5)
        elif firstHintGuess != "c":
            print("\nWrong Guess...")
            questionOneAnswer.correctAnswer()
    elif firstGuess != "c" and firstGuess != "h":
        print("\nWrong Guess...")
        questionOneAnswer.correctAnswer()

    print("\n\tI have the most championsleague!\n")
    print("Who am I?")
    secondGuess = input("[ 'C' -> Chelsea - 'R' -> Real Madrid - 'N' -> Napoli - 'L' -> Liverpool ]\n'h' -> For a hint\nEnter: ").lower()
    if secondGuess == "r":
        score.append(1.5)
    elif secondGuess == "h":
        score.append(-0.25)
        hintCounter+=1
        questionTwoAnswer.hintTwo()
        print("Who am I?")
        secondHintGuess = input("[ 'C' -> Chelsea - 'R' -> Real Madrid - 'N' -> Napoli - 'L' -> Liverpool ]\nEnter: ").lower()
        if secondHintGuess == "r":
            score.append(1.5)
        elif secondHintGuess != "r":
            print("\nWrong Guess...")
            questionTwoAnswer.correctAnswer()
    elif secondGuess != "r" and secondGuess != "h":
        print("\nWrong Guess...")
        questionTwoAnswer.correctAnswer()
        
    print("\n\tI won the 2006 worldcup!\n")
    print("Who am I?")
    thirdGuess = input("[ 'S' -> Saudi Arabia - 'F' -> France - 'B' -> Brazil - 'I' -> Italy ]\n'h' -> For a hint\nEnter: ").lower()
    if thirdGuess == "i":
        score.append(2)
    elif thirdGuess == "h":
        score.append(-0.25)
        hintCounter+=1
        questionThreeAnswer.hintThree()
        print("Who am I?")
        thirdHintGuess = input("[ 'S' -> Saudi Arabia - 'F' -> France - 'B' -> Brazil - 'I' -> Italy ]\nEnter: ").lower()
        if thirdHintGuess == "i":
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