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
    
    score = 0.0
    
    print("\n\tThey sent me to space for science!\n")
    print("Who am I?")
    guess1 = input("[ 'J' -> Joker Or 'I' -> Interstellar Or 'D' -> Django Or 'B' -> Batman ]\n'h' -> for a hint\nEnter: ").lower()
    if guess1 == "i":
        score+=1.5
    elif guess1 == "h":
        score -= 0.5
        answer1.hintOne()
        print("Who am I?")
        guess1h = input("[ 'J' -> Joker - 'I' -> Interstellar - 'D' -> Django - 'B' -> Batman ]\nEnter: ").lower()
        if guess1h == "i":
            score+=1.5
        elif guess1h != "i":
            answer1.correctAnswer()
            print("*"*50)
    elif guess1 != "i" and guess1 != "h":
        answer1.correctAnswer()
        print("*"*50)

    print("\n\tThey kidnapped my little girl!\n")
    print("Who am I?")
    guess2 = input("[ 'N' -> NoBody Or 'S' -> Scarface Or 'D' -> Django Or 'P' -> Prisoners ]\n'h' -> for a hint\nEnter: ").lower()
    if guess2 == "p":
        score+=1.5
    elif guess2 == "h":
        score-=0.5
        answer2.hintTwo()
        print("Who am I?")
        guess2h = input("[ 'N' -> NoBody Or 'S' -> Scarface Or 'D' -> Django Or 'P' -> Prisoners ]\n'h' -> for a hint\nEnter: ").lower()
        if guess2h == "p":
            score+=1.5
        elif guess2h != "p":
            answer2.correctAnswer()
            print("*"*50)
    elif guess2 != "p" and guess2 != "h":
        answer2.correctAnswer()
        print("*"*50)

    print("\n\tI'm the killing spell!\n")
    print("Who am I?")
    guess3 = input("[ 'A' -> Avatar - 'N' -> the Nun - 'F' -> Fargo - 'P' -> Harry Potter ]\n'h' -> for a hint\nEnter: ").lower()
    if guess3 == "p":
        score+=2
    elif guess3 == "h":
        score-=0.5
        answer3.hintThree()
        print("Who am I?")
        guess3h = input("[ 'A' -> Avatar - 'N' -> the Nun - 'F' -> Fargo - 'P' -> Harry Potter ]\n'h' -> for a hint\nEnter: ").lower()
        if guess3h == "p":
            score+=2
        elif guess3h != "p":
            answer3.correctAnswer()
            print("*"*50)
    elif guess3 != "p" and guess3 != "h":
        answer3.correctAnswer()
        print("*"*50)
    
    print(f"You got {score}/5 !")