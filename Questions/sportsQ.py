from manager import cheackScore , cheackTime , pointsDeduction
from functools import reduce
import time
class Answer:
    def __init__(self,answer:str):
        self.answer = answer
    def correctAnswer(self):
        return print(f"\nWrong Guess...\n\tThe correct naswer is ( {self.answer} ).\n")
    
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

answer1 = Hint("Cristiano Ronaldo")
answer2 = Hint("Real Madrid")
answer3 = Hint("Italy")

def puzzle():
    score = [0]
    hintCounter = 0
    start = time.time()
    print("\n\tI'm well known worldwide and play in an Saudi leage!\n")
    print("Who am I?")
    guess1 = input("[ 'M' -> Mohammed Noor - 'Z' -> Zlatan - 'C' -> Cristiano Ronaldo - 'L' -> Lionel Messi ]\n'h' -> For a hint\nEnter: ").lower()
    if guess1 == "c":
        score.append(1.5)
    elif guess1 == "h":
        score.append(-0.25)
        hintCounter+=1
        answer1.hintOne()
        print("Who am I?")
        guess1h = input("[ 'M' -> Mohammed Noor - 'Z' -> Zlatan - 'C' -> Cristiano Ronaldo - 'L' -> Lionel Messi ]\nEnter: ").lower()
        if guess1h == "c":
            score.append(1.5)
        elif guess1h != "c":
            answer1.correctAnswer()
    elif guess1 != "c" and guess1 != "h":
        answer1.correctAnswer()

    print("\n\tI have the most championsleague!\n")
    print("Who am I?")
    guess2 = input("[ 'C' -> Chelsea - 'R' -> Real Madrid - 'N' -> Napoli - 'L' -> Liverpool ]\n'h' -> For a hint\nEnter: ").lower()
    if guess2 == "r":
        score.append(1.5)
    elif guess2 == "h":
        score.append(-0.25)
        hintCounter+=1
        answer2.hintTwo()
        print("Who am I?")
        guess2h = input("[ 'C' -> Chelsea - 'R' -> Real Madrid - 'N' -> Napoli - 'L' -> Liverpool ]\nEnter: ").lower()
        if guess2h == "r":
            score.append(1.5)
        elif guess2h != "r":
            answer2.correctAnswer()
    elif guess2 != "r" and guess2 != "h":
        answer2.correctAnswer()
        
    print("\n\tI won the 2006 worldcup!\n")
    print("Who am I?")
    guess3 = input("[ 'S' -> Saudi Arabia - 'F' -> France - 'B' -> Brazil - 'I' -> Italy ]\n'h' -> For a hint\nEnter: ").lower()
    if guess3 == "i":
        score.append(2)
    elif guess3 == "h":
        score.append(-0.25)
        hintCounter+=1
        answer3.hintThree()
        print("Who am I?")
        guess3h = input("[ 'S' -> Saudi Arabia - 'F' -> France - 'B' -> Brazil - 'I' -> Italy ]\nEnter: ").lower()
        if guess3h == "i":
            score.append(2)
        elif guess3h != "i":
            answer3.correctAnswer()
    elif guess3 != "i" and guess3 != "h":
        answer3.correctAnswer()
        
    end = time.time()
    timeTaken = round((end - start),2)
    scoreFun = reduce(lambda a,b:a+b,score)
    cheackScore(scoreFun,timeTaken)
    cheackTime(timeTaken)
    pointsDeduction(scoreFun,hintCounter,timeTaken)