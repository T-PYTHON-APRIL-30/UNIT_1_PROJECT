from functools import reduce
import time
from manager import cheackScore , cheackTime , pointsDeduction
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
        return print("\n\tMy daughter become older than me!\n")
    
    def hintTwo(self):
        return print("\n\tI'm an inestigative movie!\n")
    
    def hintThree(self):
        return print("\n\tAvada Kedavra!\n")

answer1 = Hint("Interstellar")
answer2 = Hint("Prisoners")
answer3 = Hint("Harry Potter")

def puzzle():    
    score = [0]
    hintCounter = 0
    start = time.time()
    print("\n\tThey sent me to space for science!\n")
    print("Who am I?")
    guess1 = input("[ 'J' -> Joker Or 'I' -> Interstellar Or 'D' -> Django Or 'B' -> Batman ]\n'h' -> for a hint\nEnter: ").lower()
    if guess1 == "i":
        score.append(1.5)
    elif guess1 == "h":
        score.append(-0.25)
        hintCounter+=1
        answer1.hintOne()
        print("Who am I?")
        guess1h = input("[ 'J' -> Joker - 'I' -> Interstellar - 'D' -> Django - 'B' -> Batman ]\nEnter: ").lower()
        if guess1h == "i":
            score.append(1.5)
        elif guess1h != "i":
            answer1.correctAnswer()
    elif guess1 != "i" and guess1 != "h":
        answer1.correctAnswer()

    print("\n\tThey kidnapped my little girl!\n")
    print("Who am I?")
    guess2 = input("[ 'N' -> NoBody Or 'S' -> Scarface Or 'D' -> Django Or 'P' -> Prisoners ]\n'h' -> for a hint\nEnter: ").lower()
    if guess2 == "p":
        score.append(1.5)
    elif guess2 == "h":
        score.append(-0.25)
        hintCounter+=1
        answer2.hintTwo()
        print("Who am I?")
        guess2h = input("[ 'N' -> NoBody Or 'S' -> Scarface Or 'D' -> Django Or 'P' -> Prisoners ]\nEnter: ").lower()
        if guess2h == "p":
            score.append(1.5)
        elif guess2h != "p":
            answer2.correctAnswer()
    elif guess2 != "p" and guess2 != "h":
        answer2.correctAnswer()

    print("\n\tI'm the killing spell!\n")
    print("Who am I?")
    guess3 = input("[ 'A' -> Avatar - 'N' -> the Nun - 'F' -> Fargo - 'P' -> Harry Potter ]\n'h' -> for a hint\nEnter: ").lower()
    if guess3 == "p":
        score.append(2)
    elif guess3 == "h":
        score.append(-0.25)
        hintCounter+=1
        answer3.hintThree()
        print("Who am I?")
        guess3h = input("[ 'A' -> Avatar - 'N' -> the Nun - 'F' -> Fargo - 'P' -> Harry Potter ]\nEnter: ").lower()
        if guess3h == "p":
            score.append(2)
        elif guess3h != "p":
            answer3.correctAnswer()
    elif guess3 != "p" and guess3 != "h":
        answer3.correctAnswer()
    
    end = time.time()
    timeTaken = round((end - start),2)
    scoreFun = reduce(lambda a,b:a+b,score)
    cheackTime(timeTaken)
    cheackScore(scoreFun,timeTaken)
    pointsDeduction(scoreFun,hintCounter,timeTaken)